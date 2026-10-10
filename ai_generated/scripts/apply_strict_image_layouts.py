import re
import sys
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 1. UPDATE CSS IN assets/css/styles.css
# ==============================================================================
with open('assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Define strict, professional image boundary styles
strict_media_css = '''/* ==========================================================================
   STRICT BOUNDARY-CONSTRAINED MEDIA & CAROUSEL LAYOUTS
   All images are strictly constrained within fixed boundary dimensions.
   ========================================================================== */

/* Universal image boundary rule */
img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Ensure no media wrapper ever allows unconstrained overflow */
.card-img-wrapper,
.mini-carousel,
.carousel-track,
.carousel-slide,
.timeline-media-card,
.timeline-media-thumb,
.album-thumb-img-wrapper,
.album-thumb-item,
.hero-avatar-wrapper {
  overflow: hidden !important;
  box-sizing: border-box !important;
}

/* Standardized Mini-Carousel Component (Uniform 110px boundary) */
.mini-carousel {
  position: relative;
  width: 100%;
  height: 110px;
  border-radius: var(--radius-sm);
  overflow: hidden !important;
  margin-bottom: 12px;
  background-color: #0f172a;
  border: 1px solid var(--border-light);
  user-select: none;
  box-shadow: inset 0 0 0 1px rgba(0, 0, 0, 0.05);
}

.carousel-track {
  width: 100%;
  height: 100%;
  position: relative;
}

.carousel-slide {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.25s ease, visibility 0.25s ease;
  cursor: pointer;
  background-color: #0f172a;
  display: flex;
  align-items: center;
  justify-content: center;
}

.carousel-slide.active {
  opacity: 1;
  visibility: visible;
  z-index: 1;
}

.carousel-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transition: transform var(--transition-fast);
}

.carousel-slide:hover img {
  transform: scale(1.04);
}

.carousel-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 3;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: rgba(15, 23, 42, 0.75);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2);
  font-size: 11px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  opacity: 0;
  transition: all var(--transition-fast);
  backdrop-filter: blur(4px);
}

.mini-carousel:hover .carousel-btn {
  opacity: 1;
}

.carousel-btn:hover {
  background: var(--accent-primary);
  border-color: var(--accent-primary);
}

.carousel-btn.prev { left: 6px; }
.carousel-btn.next { right: 6px; }

.carousel-dots {
  position: absolute;
  bottom: 6px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 3;
  display: flex;
  gap: 4px;
}

.carousel-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.45);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.carousel-dot.active {
  background: #ffffff;
  width: 12px;
  border-radius: 3px;
}

.carousel-slide-badge {
  position: absolute;
  top: 6px;
  left: 6px;
  z-index: 2;
  background: rgba(15, 23, 42, 0.8);
  color: #ffffff;
  font-size: 0.625rem;
  font-weight: 600;
  padding: 2px 7px;
  border-radius: var(--radius-full);
  backdrop-filter: blur(4px);
  pointer-events: none;
  border: 1px solid rgba(255, 255, 255, 0.15);
}

.carousel-zoom-hint {
  position: absolute;
  top: 6px;
  right: 6px;
  z-index: 2;
  background: rgba(15, 23, 42, 0.8);
  color: #ffffff;
  font-size: 0.625rem;
  padding: 2px 6px;
  border-radius: var(--radius-full);
  opacity: 0;
  transition: opacity var(--transition-fast);
  pointer-events: none;
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.15);
}

.carousel-slide:hover .carousel-zoom-hint {
  opacity: 1;
}

/* Fallback single-photo card wrapper */
.card-img-wrapper {
  position: relative;
  width: 100%;
  height: 110px;
  border-radius: var(--radius-sm);
  overflow: hidden !important;
  background-color: #0f172a;
  border: 1px solid var(--border-light);
  margin-bottom: 12px;
}

.card-img-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transition: transform var(--transition-fast);
}

.card-img-wrapper:hover img {
  transform: scale(1.04);
}

.img-zoom-btn {
  position: absolute;
  top: 6px;
  right: 6px;
  background: rgba(15, 23, 42, 0.8);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.15);
  font-size: 11px;
  padding: 2px 6px;
  border-radius: var(--radius-full);
  cursor: pointer;
  opacity: 0;
  transition: opacity var(--transition-fast);
  backdrop-filter: blur(4px);
}

.card-img-wrapper:hover .img-zoom-btn {
  opacity: 1;
}

/* ==========================================================================
   CONFERENCE TIMELINE BOUNDARY-CONSTRAINED MEDIA CARDS
   ========================================================================== */
.timeline-media-card {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  max-width: 330px;
  height: 58px;
  padding: 6px 10px;
  margin: 10px 0 12px 0;
  background-color: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all var(--transition-fast);
  box-shadow: var(--shadow-sm);
  overflow: hidden !important;
  box-sizing: border-box;
}

.timeline-media-card:hover {
  border-color: var(--accent-primary);
  background-color: var(--accent-light);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

.timeline-media-thumb {
  position: relative;
  width: 66px;
  height: 44px;
  border-radius: 4px;
  overflow: hidden !important;
  background-color: #0f172a;
  flex-shrink: 0;
  border: 1px solid var(--border-light);
}

.timeline-media-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transition: transform var(--transition-fast);
}

.timeline-media-card:hover .timeline-media-thumb img {
  transform: scale(1.08);
}

.timeline-media-zoom-overlay {
  position: absolute;
  inset: 0;
  background: rgba(15, 23, 42, 0.45);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  opacity: 0;
  transition: opacity var(--transition-fast);
}

.timeline-media-card:hover .timeline-media-zoom-overlay {
  opacity: 1;
}

.timeline-media-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 0;
  overflow: hidden;
}

.timeline-media-badge {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.timeline-media-hint {
  font-size: 0.6875rem;
  color: var(--accent-primary);
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 4px;
}

/* ==========================================================================
   THEMATIC COLLAPSIBLE ALBUMS (STRICT UNIFORM THUMBNAIL CELLS)
   ========================================================================== */
.gallery-controls-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 20px;
  padding: 12px 18px;
  background-color: var(--bg-tertiary);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
}

.gallery-stats-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-secondary);
}

.album-toggle-all-btn {
  font-size: 0.8125rem;
  font-weight: 600;
  padding: 5px 14px;
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  cursor: pointer;
  color: var(--accent-primary);
  transition: all var(--transition-fast);
}

.album-toggle-all-btn:hover {
  background: var(--accent-light);
  border-color: var(--accent-primary);
}

.gallery-albums-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.gallery-album-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  overflow: hidden !important;
  box-shadow: var(--shadow-sm);
  transition: border-color var(--transition-fast);
}

.gallery-album-card:hover {
  border-color: var(--border-subtle);
}

.album-header {
  padding: 14px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  user-select: none;
  background-color: #ffffff;
  transition: background-color var(--transition-fast);
}

.album-header:hover {
  background-color: var(--bg-tertiary);
}

.album-header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.album-icon {
  font-size: 1.25rem;
  line-height: 1;
}

.album-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-primary);
}

.album-count-badge {
  font-size: 0.6875rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: var(--radius-full);
  background: var(--bg-tertiary);
  color: var(--text-muted);
  border: 1px solid var(--border-light);
}

.album-header-right {
  display: flex;
  align-items: center;
  gap: 10px;
}

.album-state-hint {
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--accent-primary);
}

.album-chevron {
  font-size: 0.875rem;
  color: var(--text-muted);
  transition: transform var(--transition-fast);
}

.gallery-album-card.open .album-chevron {
  transform: rotate(180deg);
}

/* Album Body & Compact Grid */
.album-body {
  padding: 16px 18px;
  border-top: 1px solid var(--border-light);
  background-color: var(--bg-tertiary);
  display: none;
}

.gallery-album-card.open .album-body {
  display: block;
}

.album-desc {
  font-size: 0.8125rem;
  color: var(--text-secondary);
  margin-bottom: 14px;
}

.album-thumbs-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 12px;
}

@media (max-width: 1100px) {
  .album-thumbs-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (max-width: 768px) {
  .album-thumbs-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 480px) {
  .album-thumbs-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

.album-thumb-item {
  position: relative;
  border-radius: var(--radius-sm);
  overflow: hidden !important;
  background: #ffffff;
  border: 1px solid var(--border-light);
  cursor: pointer;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), border-color var(--transition-fast);
  display: flex;
  flex-direction: column;
  box-shadow: var(--shadow-sm);
}

.album-thumb-item:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
  border-color: var(--accent-primary);
}

.album-thumb-img-wrapper {
  position: relative;
  width: 100%;
  height: 82px;
  overflow: hidden !important;
  background-color: #0f172a;
}

.album-thumb-img-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transition: transform var(--transition-fast);
}

.album-thumb-item:hover .album-thumb-img-wrapper img {
  transform: scale(1.08);
}

.album-thumb-label {
  height: 28px;
  line-height: 28px;
  padding: 0 8px;
  font-size: 0.6875rem;
  font-weight: 600;
  color: var(--text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  background: #ffffff;
  border-top: 1px solid var(--border-light);
}

.album-thumb-overlay-btn {
  position: absolute;
  top: 4px;
  right: 4px;
  font-size: 9px;
  padding: 1px 5px;
  border-radius: 4px;
  background: rgba(15, 23, 42, 0.8);
  color: #fff;
  opacity: 0;
  transition: opacity var(--transition-fast);
  backdrop-filter: blur(2px);
}

.album-thumb-item:hover .album-thumb-overlay-btn {
  opacity: 1;
}

/* Lightbox Modal */
.lightbox-modal {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.94);
  backdrop-filter: blur(8px);
  z-index: 2000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 24px;
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--transition-fast);
}

.lightbox-modal.active {
  opacity: 1;
  pointer-events: auto;
}

.lightbox-img-wrapper {
  max-width: 90vw;
  max-height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lightbox-img {
  max-width: 100%;
  max-height: 80vh;
  border-radius: var(--radius-md);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
  object-fit: contain;
}

.lightbox-caption {
  color: #ffffff;
  margin-top: 14px;
  font-size: 0.9375rem;
  text-align: center;
  max-width: 700px;
  font-weight: 500;
  line-height: 1.4;
}

.lightbox-close-btn {
  position: absolute;
  top: 24px;
  right: 24px;
  background: none;
  border: none;
  color: #ffffff;
  font-size: 2rem;
  cursor: pointer;
  line-height: 1;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
}'''

# Replace the media section in styles.css
start_idx = css.find('/* ==========================================================================\n   ULTRA-COMPACT MEDIA')
if start_idx == -1:
    start_idx = css.find('/* ==========================================================================\n   STRICT BOUNDARY-CONSTRAINED')

end_idx = css.find('/* Lightbox Modal */')
if end_idx != -1:
    # find closing bracket of lightbox-close-btn
    close_btn_end = css.find('}', css.find('.lightbox-close-btn', end_idx)) + 1
    css = css[:start_idx] + strict_media_css + css[close_btn_end:]
    with open('assets/css/styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated styles.css with strict media & boundary constraint rules!")
else:
    print("Could not locate media section in styles.css")

# ==============================================================================
# 2. UPDATE index.html: Setups, Facilities, Conferences
# ==============================================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Setup 2 Mini-Carousel (Magnetoelectric Bench)
old_setup_2_img = '''          <div class="card-img-wrapper" style="height: 135px; margin-bottom: 12px;" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_01.jpg" data-caption="Magnetoelectric Voltage Measurement Facility: dynamic ME coefficient testing bench">
            <img src="assets/images/sites/experimental_setups/experimental_setups_01.jpg" alt="Magnetoelectric Voltage Facility" loading="lazy">
            <button class="img-zoom-btn" aria-label="Enlarge photo">🔍</button>
          </div>'''

new_setup_2_carousel = '''          <!-- Standardized Mini-Carousel -->
          <div class="mini-carousel" data-carousel>
            <div class="carousel-track">
              <div class="carousel-slide active" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_01.jpg" data-caption="Magnetoelectric Voltage Measurement Facility: dynamic ME coefficient testing bench with lock-in detection and AC/DC bias">
                <img src="assets/images/sites/experimental_setups/experimental_setups_01.jpg" alt="Magnetoelectric Voltage Facility" loading="lazy">
                <span class="carousel-slide-badge">1/2 • Dynamic ME Bench</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/gallery/gallery_05.jpg" data-caption="High-frequency characterization and multiferroic thin film standardization bench">
                <img src="assets/images/sites/gallery/gallery_05.jpg" alt="Thin Film Standardization" loading="lazy">
                <span class="carousel-slide-badge">2/2 • Multiferroic Probe Stage</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
            </div>
            <button class="carousel-btn prev" aria-label="Previous slide">&#10094;</button>
            <button class="carousel-btn next" aria-label="Next slide">&#10095;</button>
            <div class="carousel-dots"></div>
          </div>'''

html = html.replace(old_setup_2_img, new_setup_2_carousel)

# Setup 3 Mini-Carousel (Miniature Electromagnet)
old_setup_3_img = '''          <div class="card-img-wrapper" style="height: 135px; margin-bottom: 12px;" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_02.jpg" data-caption="Miniature Electromagnet (800 Oe @ 1A) engineered for high frequency RF probe stations">
            <img src="assets/images/sites/experimental_setups/experimental_setups_02.jpg" alt="Miniature Electromagnet" loading="lazy">
            <button class="img-zoom-btn" aria-label="Enlarge photo">🔍</button>
          </div>'''

new_setup_3_carousel = '''          <!-- Standardized Mini-Carousel -->
          <div class="mini-carousel" data-carousel>
            <div class="carousel-track">
              <div class="carousel-slide active" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_02.jpg" data-caption="Miniature Electromagnet (800 Oe @ 1A) engineered for high frequency RF probe stations">
                <img src="assets/images/sites/experimental_setups/experimental_setups_02.jpg" alt="Miniature Electromagnet" loading="lazy">
                <span class="carousel-slide-badge">1/2 • 800 Oe Electromagnet</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/gallery/gallery_04.jpg" data-caption="Electromagnet integration with wafer probe station and coplanar waveguide stage">
                <img src="assets/images/sites/gallery/gallery_04.jpg" alt="Probe Stage Integration" loading="lazy">
                <span class="carousel-slide-badge">2/2 • Wafer Probe Integration</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
            </div>
            <button class="carousel-btn prev" aria-label="Previous slide">&#10094;</button>
            <button class="carousel-btn next" aria-label="Next slide">&#10095;</button>
            <div class="carousel-dots"></div>
          </div>'''

html = html.replace(old_setup_3_img, new_setup_3_carousel)

# Facility 5 Mini-Carousel (Ion Beam Accelerator Facility)
old_fac_5_img = '''          <div class="card-img-wrapper" style="height: 135px; margin-bottom: 14px;" data-zoom-src="assets/images/sites/gallery/gallery_07.jpg" data-caption="Swift Heavy Ion (SHI) Irradiation Beamline Experiment at Inter-University Accelerator Centre (IUAC), New Delhi">
            <img src="assets/images/sites/gallery/gallery_07.jpg" alt="SHI Beamline at IUAC" loading="lazy">
            <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
          </div>'''

new_fac_5_carousel = '''          <!-- Standardized Mini-Carousel -->
          <div class="mini-carousel" data-carousel>
            <div class="carousel-track">
              <div class="carousel-slide active" data-zoom-src="assets/images/sites/gallery/gallery_07.jpg" data-caption="Swift Heavy Ion (SHI) Irradiation Beamline Experiment at Inter-University Accelerator Centre (IUAC), New Delhi">
                <img src="assets/images/sites/gallery/gallery_07.jpg" alt="SHI Beamline at IUAC" loading="lazy">
                <span class="carousel-slide-badge">1/2 • Pelletron Beamline</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/experience/experience_18.jpg" data-caption="Low-temperature PPMS magnetometry and post-irradiation characterization">
                <img src="assets/images/sites/experience/experience_18.jpg" alt="PPMS Post-Irradiation Analysis" loading="lazy">
                <span class="carousel-slide-badge">2/2 • PPMS Magnetometry</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
            </div>
            <button class="carousel-btn prev" aria-label="Previous slide">&#10094;</button>
            <button class="carousel-btn next" aria-label="Next slide">&#10095;</button>
            <div class="carousel-dots"></div>
          </div>'''

html = html.replace(old_fac_5_img, new_fac_5_carousel)

# Update all 9 Timeline items in #conferences using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
conf_sec = soup.find('section', id='conferences')
if conf_sec:
    boxes = conf_sec.find_all('div', class_='timeline-thumb-box')
    print(f"Replacing {len(boxes)} timeline-thumb-box elements with boundary-constrained timeline-media-cards...")
    for box in boxes:
        img_el = box.find('img')
        src = img_el.get('src') if img_el else ""
        caption = box.find('div', class_='timeline-thumb').get('data-caption', '') if box.find('div', class_='timeline-thumb') else ""
        title_el = box.find('div', class_='timeline-thumb-title')
        title = title_el.text.strip() if title_el else "Document / Photo"

        card_html = f'''<div class="timeline-media-card" data-zoom-src="{src}" data-caption="{caption}" title="Click to view full image in high resolution">
              <div class="timeline-media-thumb">
                <img src="{src}" alt="{title}" loading="lazy">
                <div class="timeline-media-zoom-overlay">🔍</div>
              </div>
              <div class="timeline-media-info">
                <span class="timeline-media-badge">{title}</span>
                <span class="timeline-media-hint">View Document / Photo ↗</span>
              </div>
            </div>'''
        
        new_tag = BeautifulSoup(card_html, 'html.parser').find('div')
        box.replace_with(new_tag)

    html = str(soup)
    print("Replaced all timeline thumb boxes with .timeline-media-card!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully!")

