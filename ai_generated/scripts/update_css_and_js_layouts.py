import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update assets/css/styles.css
with open('assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

strict_compact_media_css = '''/* ==========================================================================
   STRICT COMPACT MEDIA & MOUSE-HOVER ZOOM STYLES
   All images are small, compact and non-intrusive. Mouse hover reveals large preview.
   Single screen row displays 4-6 images in gallery. Zero border overflow.
   ========================================================================== */

/* Universal image boundary protection */
*, *::before, *::after {
  box-sizing: border-box !important;
}

img {
  max-width: 100% !important;
  height: auto;
  display: block;
}

/* Ensure no media wrapper or card ever allows unconstrained overflow */
.setup-card,
.facility-card,
.timeline-content,
.gallery-card,
.card-img-wrapper,
.mini-carousel,
.carousel-track,
.carousel-slide,
.timeline-proof-badge,
.proof-badge-thumb,
.hero-avatar-wrapper {
  overflow: hidden !important;
  box-sizing: border-box !important;
  min-width: 0 !important;
  max-width: 100% !important;
}

/* Ultra-Compact Mini-Carousel Component (Constrained to 52px preview bar) */
.mini-carousel {
  position: relative;
  width: 100%;
  height: 52px;
  border-radius: var(--radius-sm);
  overflow: hidden !important;
  margin-bottom: 8px;
  background-color: #0f172a;
  border: 1px solid var(--border-light);
  user-select: none;
  cursor: pointer;
  box-sizing: border-box;
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
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: rgba(15, 23, 42, 0.75);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2);
  font-size: 8px;
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

.carousel-btn.prev { left: 4px; }
.carousel-btn.next { right: 4px; }

.carousel-dots {
  position: absolute;
  bottom: 3px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 3;
  display: flex;
  gap: 3px;
}

.carousel-dot {
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.45);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.carousel-dot.active {
  background: #ffffff;
  width: 8px;
  border-radius: 2px;
}

.carousel-slide-badge {
  position: absolute;
  top: 3px;
  left: 4px;
  z-index: 2;
  background: rgba(15, 23, 42, 0.85);
  color: #ffffff;
  font-size: 0.5rem;
  font-weight: 600;
  padding: 1px 4px;
  border-radius: var(--radius-full);
  backdrop-filter: blur(4px);
  pointer-events: none;
  border: 1px solid rgba(255, 255, 255, 0.15);
}

.carousel-zoom-hint {
  position: absolute;
  top: 3px;
  right: 4px;
  z-index: 2;
  background: rgba(15, 23, 42, 0.85);
  color: #ffffff;
  font-size: 0.5rem;
  padding: 1px 4px;
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

/* Fallback single-photo card wrapper (Constrained to 52px preview bar) */
.card-img-wrapper {
  position: relative;
  width: 100%;
  height: 52px;
  border-radius: var(--radius-sm);
  overflow: hidden !important;
  background-color: #0f172a;
  border: 1px solid var(--border-light);
  margin-bottom: 8px;
  cursor: pointer;
  box-sizing: border-box;
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
  transform: scale(1.05);
}

.card-img-wrapper:hover .carousel-zoom-hint {
  opacity: 1;
}

/* ==========================================================================
   CONFERENCE TIMELINE PROOF BADGE (SMALL 28px INLINE PILL)
   ========================================================================== */
.timeline-proof-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  max-width: 100%;
  height: 28px;
  padding: 2px 8px 2px 3px;
  margin: 6px 0 8px 0;
  background-color: var(--bg-tertiary);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-full);
  cursor: pointer;
  transition: all var(--transition-fast);
  width: fit-content;
  box-sizing: border-box;
  overflow: hidden !important;
}

.timeline-proof-badge:hover {
  background-color: var(--accent-light);
  border-color: var(--accent-primary);
  transform: translateY(-1px);
}

.proof-badge-thumb {
  width: 24px;
  height: 20px;
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
  font-size: 0.6875rem;
  font-weight: 600;
  color: var(--text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 220px;
}

.proof-badge-hint {
  font-size: 0.625rem;
  color: var(--accent-primary);
  font-weight: 600;
  margin-left: 2px;
  white-space: nowrap;
}

/* ==========================================================================
   CURATED VISUAL EVIDENCE GALLERY (4-6 IMAGES PER SCREEN ROW)
   ========================================================================== */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr); /* Exactly 5 images per screen row on desktop */
  gap: 12px;
  width: 100%;
  box-sizing: border-box;
}

@media (max-width: 1200px) {
  .gallery-grid {
    grid-template-columns: repeat(4, 1fr); /* 4 images per row on compact laptops */
  }
}

@media (max-width: 840px) {
  .gallery-grid {
    grid-template-columns: repeat(3, 1fr); /* 3 images per row on tablets */
  }
}

@media (max-width: 520px) {
  .gallery-grid {
    grid-template-columns: repeat(2, 1fr); /* 2 images per row on mobile */
  }
}

.gallery-card {
  background: #ffffff;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  overflow: hidden !important;
  box-sizing: border-box;
  transition: all var(--transition-fast);
  cursor: pointer;
  display: flex;
  flex-direction: column;
  box-shadow: var(--shadow-sm);
  min-width: 0 !important;
}

.gallery-card:hover {
  transform: translateY(-2px);
  border-color: var(--accent-primary);
  box-shadow: var(--shadow-md);
}

.gallery-card-img-box {
  position: relative;
  width: 100%;
  height: 60px; /* Small 60px thumbnail height */
  background-color: #0f172a;
  overflow: hidden !important;
  box-sizing: border-box;
}

.gallery-card-img-box img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transition: transform var(--transition-fast);
}

.gallery-card:hover .gallery-card-img-box img {
  transform: scale(1.08);
}

.gallery-card-zoom-btn {
  position: absolute;
  top: 3px;
  right: 3px;
  font-size: 8px;
  padding: 1px 4px;
  border-radius: 3px;
  background: rgba(15, 23, 42, 0.8);
  color: #fff;
  opacity: 0;
  transition: opacity var(--transition-fast);
  backdrop-filter: blur(2px);
}

.gallery-card:hover .gallery-card-zoom-btn {
  opacity: 1;
}

.gallery-card-body {
  padding: 6px 8px;
  background: #ffffff;
  border-top: 1px solid var(--border-light);
  box-sizing: border-box;
  min-width: 0;
}

.gallery-card-title {
  font-size: 0.6875rem;
  font-weight: 700;
  color: var(--text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1.25;
}

.gallery-card-tag {
  font-size: 0.5625rem;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-top: 1px;
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
  max-width: calc(100vw - 24px);
  overflow: hidden !important;
  box-sizing: border-box;
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
  overflow: hidden !important;
  width: 320px;
  max-width: 100%;
  box-sizing: border-box;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
}

.hover-zoom-img-wrapper {
  position: relative;
  width: 100%;
  height: 190px;
  background-color: #0f172a;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden !important;
  box-sizing: border-box;
}

.hover-zoom-img-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}

.hover-zoom-lens-badge {
  position: absolute;
  bottom: 6px;
  right: 6px;
  font-size: 0.625rem;
  font-weight: 600;
  background: rgba(15, 23, 42, 0.85);
  color: #ffffff;
  padding: 2px 7px;
  border-radius: var(--radius-full);
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.hover-zoom-caption {
  padding: 8px 12px;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--text-primary);
  background: #ffffff;
  border-top: 1px solid var(--border-light);
  line-height: 1.35;
  box-sizing: border-box;
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

start_idx = css.find('/* ==========================================================================\n   STRICT COMPACT MEDIA')
end_idx = css.find('.lightbox-close-btn')
if start_idx != -1 and end_idx != -1:
    close_btn_end = css.find('}', end_idx) + 1
    css = css[:start_idx] + strict_compact_media_css + css[close_btn_end:]
    with open('assets/css/styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated styles.css with strict 4-6 image grid, small image sizes, and anti-overflow rules!")
else:
    print("Warning: could not locate CSS section for replacement.")

# 2. Update assets/js/main.js
with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# In initHoverZoom(), refine cardWidth to 320 and clamp positions
hover_zoom_clamp = '''    const cardWidth = 320;
    const cardHeight = 250;
    const margin = 12;

    let x = clientX + 16;
    let y = clientY - 80;

    // Viewport collision handling
    if (x + cardWidth + margin > window.innerWidth) {
      x = clientX - cardWidth - 16;
    }
    if (x < margin) x = margin;

    if (y + cardHeight + margin > window.innerHeight) {
      y = window.innerHeight - cardHeight - margin;
    }
    if (y < margin) y = margin;

    preview.style.left = `${Math.round(x)}px`;
    preview.style.top = `${Math.round(y)}px`;'''

old_clamp_pattern = r'const cardWidth = 360;[\s\S]*?preview\.style\.top = `\$\{y\}px`;'
if re.search(old_clamp_pattern, js):
    js = re.sub(old_clamp_pattern, hover_zoom_clamp, js, count=1)
    print("Updated hover zoom positioning in main.js!")

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated main.js successfully!")

