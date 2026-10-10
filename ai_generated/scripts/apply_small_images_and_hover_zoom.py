import re
import sys
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 1. UPDATE index.html: Transform timeline-media-cards to timeline-proof-badges
# ==============================================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
conf_sec = soup.find('section', id='conferences')
if conf_sec:
    cards = conf_sec.find_all('div', class_='timeline-media-card')
    print(f"Found {len(cards)} timeline-media-card elements to convert into .timeline-proof-badge...")
    for card in cards:
        src = card.get('data-zoom-src', '')
        caption = card.get('data-caption', '')
        badge_el = card.find('span', class_='timeline-media-badge')
        badge_title = badge_el.text.strip() if badge_el else "Document / Photo"

        proof_badge_html = f'''<div class="timeline-proof-badge" data-zoom-src="{src}" data-caption="{caption}" title="Hover to preview certificate • Click for full screen">
              <div class="proof-badge-thumb">
                <img src="{src}" alt="{badge_title}" loading="lazy">
              </div>
              <span class="proof-badge-text">📜 {badge_title}</span>
              <span class="proof-badge-hint">🔍 Hover to Zoom</span>
            </div>'''
        new_tag = BeautifulSoup(proof_badge_html, 'html.parser').find('div')
        card.replace_with(new_tag)

html = str(soup)

# Also ensure hover-zoom-preview element is present right before </body>
if 'id="hover-zoom-preview"' not in html:
    hover_zoom_container = '''  <!-- Floating Mouse Hover Zoom Lens -->
  <div id="hover-zoom-preview" class="hover-zoom-preview" aria-hidden="true">
    <div class="hover-zoom-card">
      <div class="hover-zoom-img-wrapper">
        <img id="hover-zoom-img" src="" alt="Zoom preview">
        <div class="hover-zoom-lens-badge">🔍 Click for Full Screen</div>
      </div>
      <div id="hover-zoom-caption" class="hover-zoom-caption"></div>
    </div>
  </div>

</body>'''
    html = html.replace('</body>', hover_zoom_container)
    print("Added hover-zoom-preview element before </body> in index.html!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully!")


# ==============================================================================
# 2. UPDATE assets/css/styles.css: Small image styles & hover zoom popover
# ==============================================================================
with open('assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

strict_compact_css = '''/* ==========================================================================
   STRICT COMPACT MEDIA & MOUSE-HOVER ZOOM STYLES
   All images are small, compact and non-intrusive. Mouse hover reveals large preview.
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
.timeline-proof-badge,
.proof-badge-thumb,
.album-thumb-img-wrapper,
.album-thumb-item,
.hero-avatar-wrapper {
  overflow: hidden !important;
  box-sizing: border-box !important;
}

/* Ultra-Compact Mini-Carousel Component (Constrained to 70px preview bar) */
.mini-carousel {
  position: relative;
  width: 100%;
  height: 70px;
  border-radius: var(--radius-sm);
  overflow: hidden !important;
  margin-bottom: 10px;
  background-color: #0f172a;
  border: 1px solid var(--border-light);
  user-select: none;
  cursor: pointer;
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
  transform: scale(1.05);
}

.carousel-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 3;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: rgba(15, 23, 42, 0.75);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2);
  font-size: 9px;
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

.carousel-btn.prev { left: 5px; }
.carousel-btn.next { right: 5px; }

.carousel-dots {
  position: absolute;
  bottom: 4px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 3;
  display: flex;
  gap: 3px;
}

.carousel-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.45);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.carousel-dot.active {
  background: #ffffff;
  width: 10px;
  border-radius: 2px;
}

.carousel-slide-badge {
  position: absolute;
  top: 4px;
  left: 4px;
  z-index: 2;
  background: rgba(15, 23, 42, 0.85);
  color: #ffffff;
  font-size: 0.5625rem;
  font-weight: 600;
  padding: 1px 5px;
  border-radius: var(--radius-full);
  backdrop-filter: blur(4px);
  pointer-events: none;
  border: 1px solid rgba(255, 255, 255, 0.15);
}

.carousel-zoom-hint {
  position: absolute;
  top: 4px;
  right: 4px;
  z-index: 2;
  background: rgba(15, 23, 42, 0.85);
  color: #ffffff;
  font-size: 0.5625rem;
  padding: 1px 5px;
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
  height: 70px;
  border-radius: var(--radius-sm);
  overflow: hidden !important;
  background-color: #0f172a;
  border: 1px solid var(--border-light);
  margin-bottom: 10px;
  cursor: pointer;
}

.card-img-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}

/* ==========================================================================
   CONFERENCE TIMELINE PROOF BADGE (SMALL, SLEEK INLINE PILL)
   ========================================================================== */
.timeline-proof-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  height: 32px;
  padding: 3px 10px 3px 4px;
  margin: 6px 0 10px 0;
  background-color: var(--bg-tertiary);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-full);
  cursor: pointer;
  transition: all var(--transition-fast);
  width: fit-content;
  box-sizing: border-box;
}

.timeline-proof-badge:hover {
  background-color: var(--accent-light);
  border-color: var(--accent-primary);
  transform: translateY(-1px);
}

.proof-badge-thumb {
  width: 32px;
  height: 24px;
  border-radius: var(--radius-full);
  overflow: hidden !important;
  background-color: #0f172a;
  flex-shrink: 0;
  border: 1px solid var(--border-light);
}

.proof-badge-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}

.proof-badge-text {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-primary);
  white-space: nowrap;
}

.proof-badge-hint {
  font-size: 0.6875rem;
  color: var(--accent-primary);
  font-weight: 600;
  margin-left: 2px;
}

/* ==========================================================================
   THEMATIC COLLAPSIBLE ALBUMS (SMALL MICRO-THUMBNAILS)
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
  padding: 12px 18px;
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
  font-size: 0.9375rem;
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
  padding: 14px 18px;
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
  margin-bottom: 12px;
}

.album-thumbs-grid {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  gap: 8px;
}

@media (max-width: 1100px) {
  .album-thumbs-grid {
    grid-template-columns: repeat(6, 1fr);
  }
}

@media (max-width: 768px) {
  .album-thumbs-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (max-width: 480px) {
  .album-thumbs-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.album-thumb-item {
  position: relative;
  border-radius: var(--radius-sm);
  overflow: hidden !important;
  background: #ffffff;
  border: 1px solid var(--border-light);
  cursor: pointer;
  transition: all var(--transition-fast);
  display: flex;
  flex-direction: column;
}

.album-thumb-item:hover {
  transform: translateY(-2px);
  border-color: var(--accent-primary);
  box-shadow: var(--shadow-sm);
}

.album-thumb-img-wrapper {
  position: relative;
  width: 100%;
  height: 52px;
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
  height: 20px;
  line-height: 20px;
  padding: 0 4px;
  font-size: 0.625rem;
  font-weight: 600;
  color: var(--text-secondary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  background: #ffffff;
  border-top: 1px solid var(--border-light);
  text-align: center;
}

.album-thumb-overlay-btn {
  position: absolute;
  top: 2px;
  right: 2px;
  font-size: 8px;
  padding: 1px 4px;
  border-radius: 3px;
  background: rgba(15, 23, 42, 0.8);
  color: #fff;
  opacity: 0;
  transition: opacity var(--transition-fast);
  backdrop-filter: blur(2px);
}

.album-thumb-item:hover .album-thumb-overlay-btn {
  opacity: 1;
}

/* ==========================================================================
   INSTANT MOUSE-HOVER ZOOM POPOVER (HIGH-RESOLUTION MAGNIFIER)
   ========================================================================== */
.hover-zoom-preview {
  position: fixed;
  z-index: 3000;
  pointer-events: none;
  opacity: 0;
  visibility: hidden;
  transform: scale(0.94) translateY(6px);
  transition: opacity 0.16s ease, transform 0.16s ease, visibility 0.16s ease;
  filter: drop-shadow(0 14px 28px rgba(0, 0, 0, 0.28));
}

.hover-zoom-preview.active {
  opacity: 1;
  visibility: visible;
  transform: scale(1) translateY(0);
}

.hover-zoom-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  overflow: hidden;
  width: 360px;
  max-width: 90vw;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
}

.hover-zoom-img-wrapper {
  position: relative;
  width: 100%;
  height: 220px;
  background-color: #0f172a;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.hover-zoom-img-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}

.hover-zoom-lens-badge {
  position: absolute;
  bottom: 8px;
  right: 8px;
  font-size: 0.6875rem;
  font-weight: 600;
  background: rgba(15, 23, 42, 0.85);
  color: #ffffff;
  padding: 3px 8px;
  border-radius: var(--radius-full);
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.hover-zoom-caption {
  padding: 10px 14px;
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--text-primary);
  background: #ffffff;
  border-top: 1px solid var(--border-light);
  line-height: 1.35;
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

start_idx = css.find('/* ==========================================================================\n   STRICT BOUNDARY-CONSTRAINED')
if start_idx == -1:
    start_idx = css.find('/* ==========================================================================\n   STRICT COMPACT MEDIA')

end_idx = css.find('.lightbox-close-btn')
if end_idx != -1:
    close_btn_end = css.find('}', end_idx) + 1
    css = css[:start_idx] + strict_compact_css + css[close_btn_end:]
    with open('assets/css/styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated styles.css with compact media & hover zoom styles!")
else:
    print("Could not locate CSS section to replace in styles.css")

# ==============================================================================
# 3. UPDATE assets/js/main.js: Add initHoverZoom() and connect lightbox
# ==============================================================================
with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add initHoverZoom to DOMContentLoaded if not present
if 'initHoverZoom();' not in js:
    js = js.replace('  initLightbox();', '  initLightbox();\n  initHoverZoom();')

# Update initLightbox trigger to include .timeline-proof-badge
old_trigger_pattern = r'const trigger = e\.target\.closest\([^)]+\);'
new_trigger_line = 'const trigger = e.target.closest(\'[data-zoom-src], .timeline-proof-badge, .proof-badge-thumb, .carousel-slide.active, .album-thumb-item, .card-img-wrapper\');'
js = re.sub(old_trigger_pattern, new_trigger_line, js, count=1)

# Append initHoverZoom function implementation
hover_zoom_js = '''
/* --------------------------------------------------------------------------
   MOUSE HOVER ZOOM LENS (INSTANT FLOATING PREVIEW)
   -------------------------------------------------------------------------- */
function initHoverZoom() {
  if (window.matchMedia('(pointer: coarse)').matches) return; // Skip on touch-only devices

  const preview = document.getElementById('hover-zoom-preview');
  const zoomImg = document.getElementById('hover-zoom-img');
  const zoomCaption = document.getElementById('hover-zoom-caption');
  if (!preview || !zoomImg) return;

  let isVisible = false;
  let currentTarget = null;

  function updatePosition(clientX, clientY) {
    if (!isVisible) return;
    const cardWidth = 360;
    const cardHeight = 280;
    const margin = 16;

    let x = clientX + 22;
    let y = clientY - 110;

    // Viewport collision handling
    if (x + cardWidth + margin > window.innerWidth) {
      x = clientX - cardWidth - 22;
    }
    if (x < margin) x = margin;

    if (y + cardHeight + margin > window.innerHeight) {
      y = window.innerHeight - cardHeight - margin;
    }
    if (y < margin) y = margin;

    preview.style.left = `${x}px`;
    preview.style.top = `${y}px`;
  }

  document.addEventListener('mouseover', (e) => {
    if (e.target.closest('#lightbox-modal, #hover-zoom-preview')) return;

    const target = e.target.closest('[data-zoom-src], .timeline-proof-badge, .album-thumb-item, .carousel-slide');
    if (target && !target.closest('#hover-zoom-preview')) {
      currentTarget = target;
      const src = target.getAttribute('data-zoom-src') || 
                  target.querySelector('img')?.getAttribute('data-zoom-src') || 
                  target.querySelector('img')?.getAttribute('src');
      const caption = target.getAttribute('data-caption') || 
                      target.querySelector('img')?.getAttribute('data-caption') || 
                      target.querySelector('img')?.getAttribute('alt') || '';

      if (src) {
        zoomImg.src = src;
        if (zoomCaption) zoomCaption.textContent = caption;
        preview.classList.add('active');
        isVisible = true;
        updatePosition(e.clientX, e.clientY);
      }
    }
  });

  document.addEventListener('mousemove', (e) => {
    if (isVisible) {
      requestAnimationFrame(() => updatePosition(e.clientX, e.clientY));
    }
  }, { passive: true });

  document.addEventListener('mouseout', (e) => {
    const target = e.target.closest('[data-zoom-src], .timeline-proof-badge, .album-thumb-item, .carousel-slide');
    if (target && target === currentTarget) {
      preview.classList.remove('active');
      isVisible = false;
      currentTarget = null;
    }
  });

  window.addEventListener('scroll', () => {
    if (isVisible) {
      preview.classList.remove('active');
      isVisible = false;
    }
  }, { passive: true });

  document.addEventListener('click', () => {
    if (isVisible) {
      preview.classList.remove('active');
      isVisible = false;
    }
  });
}
'''

# Remove any previous initHoverZoom definition if present
if 'function initHoverZoom()' in js:
    js = js[:js.find('/* --------------------------------------------------------------------------\n   MOUSE HOVER ZOOM')]

js += hover_zoom_js

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated main.js with initHoverZoom implementation!")

