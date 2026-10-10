import re

# 1. Update CSS in assets/css/styles.css
with open('assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace carousel and gallery styles with ultra-compact and collapsible styles
old_gallery_css_start = '/* Multi-photo slider / grid for setups */'
old_gallery_css_end = '@media (max-width: 480px) {\n  .gallery-grid {\n    grid-template-columns: 1fr;\n  }\n}'

new_compact_css = '''/* ==========================================================================
   ULTRA-COMPACT MEDIA & CAROUSEL STYLES (IMAGES NEVER DOMINATE)
   ========================================================================== */

/* Multi-photo slider / grid for setups */
.setup-photo-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
  margin-bottom: 10px;
}

.setup-photo-grid .card-img-wrapper {
  height: 85px;
  margin-bottom: 0;
}

.card-img-wrapper {
  position: relative;
  width: 100%;
  height: 100px;
  border-radius: var(--radius-sm);
  overflow: hidden;
  background-color: var(--bg-tertiary);
  border: 1px solid var(--border-light);
  margin-bottom: 10px;
}

.card-img-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--transition-fast);
}

.card-img-wrapper:hover img {
  transform: scale(1.04);
}

.img-zoom-btn {
  position: absolute;
  top: 6px;
  right: 6px;
  background: rgba(15, 23, 42, 0.75);
  color: #ffffff;
  border: none;
  font-size: 11px;
  padding: 3px 6px;
  border-radius: var(--radius-full);
  cursor: pointer;
  opacity: 0;
  transition: opacity var(--transition-fast);
  backdrop-filter: blur(4px);
}

.card-img-wrapper:hover .img-zoom-btn {
  opacity: 1;
}

/* Compact Mini-Carousel Component */
.mini-carousel {
  position: relative;
  width: 100%;
  height: 100px;
  border-radius: var(--radius-sm);
  overflow: hidden;
  margin-bottom: 10px;
  background-color: var(--bg-tertiary);
  border: 1px solid var(--border-light);
  user-select: none;
}

.carousel-track {
  width: 100%;
  height: 100%;
  position: relative;
}

.carousel-slide {
  position: absolute;
  inset: 0;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.25s ease, visibility 0.25s ease;
  cursor: pointer;
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
  transition: transform var(--transition-fast);
}

.carousel-slide:hover img {
  transform: scale(1.03);
}

.carousel-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 3;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: rgba(15, 23, 42, 0.7);
  color: #ffffff;
  border: none;
  font-size: 10px;
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
}

.carousel-btn.prev { left: 5px; }
.carousel-btn.next { right: 5px; }

.carousel-dots {
  position: absolute;
  bottom: 5px;
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
  background: rgba(255, 255, 255, 0.5);
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
  top: 5px;
  left: 5px;
  z-index: 2;
  background: rgba(15, 23, 42, 0.75);
  color: #ffffff;
  font-size: 0.625rem;
  font-weight: 600;
  padding: 1px 6px;
  border-radius: var(--radius-full);
  backdrop-filter: blur(4px);
  pointer-events: none;
}

.carousel-zoom-hint {
  position: absolute;
  top: 5px;
  right: 5px;
  z-index: 2;
  background: rgba(15, 23, 42, 0.75);
  color: #ffffff;
  font-size: 0.625rem;
  padding: 1px 5px;
  border-radius: var(--radius-full);
  opacity: 0;
  transition: opacity var(--transition-fast);
  pointer-events: none;
}

.carousel-slide:hover .carousel-zoom-hint {
  opacity: 1;
}

/* ==========================================================================
   INLINE TIMELINE MEDIA PILL (ZERO INTRUSION)
   ========================================================================== */
.timeline-photo-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 3px 10px;
  font-size: 0.75rem;
  font-weight: 600;
  border-radius: var(--radius-full);
  background-color: var(--bg-tertiary);
  border: 1px solid var(--border-light);
  color: var(--accent-primary);
  cursor: pointer;
  margin: 6px 0 10px 0;
  transition: all var(--transition-fast);
  width: fit-content;
}

.timeline-photo-pill:hover {
  background-color: var(--accent-light);
  border-color: var(--accent-primary);
  transform: translateY(-1px);
}

.timeline-photo-pill img {
  width: 22px;
  height: 16px;
  border-radius: 2px;
  object-fit: cover;
}

/* ==========================================================================
   COLLAPSIBLE THEMATIC ALBUMS (GALLERY NEVER DOMINATES)
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
  padding: 5px 12px;
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
  overflow: hidden;
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
  grid-template-columns: repeat(6, 1fr);
  gap: 10px;
}

@media (max-width: 1024px) {
  .album-thumbs-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (max-width: 640px) {
  .album-thumbs-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

.album-thumb-item {
  position: relative;
  border-radius: var(--radius-sm);
  overflow: hidden;
  background: #ffffff;
  border: 1px solid var(--border-light);
  cursor: pointer;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast);
  display: flex;
  flex-direction: column;
}

.album-thumb-item:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
  border-color: var(--accent-primary);
}

.album-thumb-img-wrapper {
  position: relative;
  width: 100%;
  height: 80px;
  overflow: hidden;
  background: #000;
}

.album-thumb-img-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--transition-fast);
}

.album-thumb-item:hover .album-thumb-img-wrapper img {
  transform: scale(1.08);
}

.album-thumb-label {
  padding: 6px 8px;
  font-size: 0.6875rem;
  font-weight: 600;
  color: var(--text-primary);
  line-height: 1.25;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  background: #ffffff;
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
}

.album-thumb-item:hover .album-thumb-overlay-btn {
  opacity: 1;
}

/* Lightbox Modal */
.lightbox-modal {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.92);
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
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
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

# Replace in styles.css
start_idx = css.find('/* Multi-photo slider / grid for setups */')
end_idx = css.find('@media (max-width: 480px) {\n  .gallery-grid {\n    grid-template-columns: 1fr;\n  }\n}') + len('@media (max-width: 480px) {\n  .gallery-grid {\n    grid-template-columns: 1fr;\n  }\n}')

if start_idx != -1 and end_idx != -1:
    css = css[:start_idx] + new_compact_css + css[end_idx:]
    with open('assets/css/styles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated assets/css/styles.css with ultra-compact media and collapsible album styles!")
else:
    print("Warning: could not locate exact CSS slice for replacement")

