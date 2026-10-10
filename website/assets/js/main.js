/**
 * Main Interactive Logic for Arun B Academic Portfolio
 * Theme Toggle, Real-time Publication Search/Filtering, BibTeX Modal, Animations
 */

document.addEventListener('DOMContentLoaded', () => {
  initReadingProgress();
  initNavigation();
  initPublications();
  initImpactCounters();
  initBibTeXModal();
  initCarousels();
  initLightbox();
  initHoverZoom();
  initAlbumDrawers();
  initContactForm();
  initBackToTop();
});


/* --------------------------------------------------------------------------
   READING PROGRESS BAR
   -------------------------------------------------------------------------- */
function initReadingProgress() {
  const progressBar = document.getElementById('reading-progress');
  if (!progressBar) return;

  window.addEventListener('scroll', () => {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = (window.scrollY / totalHeight) * 100;
    progressBar.style.width = `${progress}%`;
  }, { passive: true });
}

/* --------------------------------------------------------------------------
   NAVIGATION & ACTIVE LINK TRACKING
   -------------------------------------------------------------------------- */
function initNavigation() {
  const navbar = document.querySelector('.navbar');
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const mobileDrawer = document.getElementById('mobile-nav-drawer');
  const navLinks = document.querySelectorAll('.nav-link');

  // Sticky shadow effect
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar?.classList.add('scrolled');
    } else {
      navbar?.classList.remove('scrolled');
    }
  }, { passive: true });

  // Mobile menu drawer
  mobileBtn?.addEventListener('click', () => {
    mobileDrawer?.classList.toggle('open');
    const isOpen = mobileDrawer?.classList.contains('open');
    mobileBtn.setAttribute('aria-expanded', isOpen);
  });

  // Close mobile drawer on link click
  mobileDrawer?.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
      mobileDrawer.classList.remove('open');
    });
  });

  // Active section tracking with IntersectionObserver
  const sections = document.querySelectorAll('section[id]');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, { threshold: 0.25 });

  sections.forEach(sec => observer.observe(sec));
}

/* --------------------------------------------------------------------------
   PUBLICATIONS RENDERING, SEARCH & CATEGORY FILTERING
   -------------------------------------------------------------------------- */
let activeCategory = 'all';
let searchQuery = '';

function initPublications() {
  const container = document.getElementById('publications-container');
  const searchInput = document.getElementById('pub-search-input');
  const filterTabs = document.querySelectorAll('.pub-tab-btn');
  const countBadge = document.getElementById('pub-results-count');

  if (!container || typeof PUBLICATIONS_DATA === 'undefined') return;

  renderPublications();

  // Category filter tabs
  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      filterTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      activeCategory = tab.getAttribute('data-category');
      renderPublications();
    });
  });

  // Real-time search
  searchInput?.addEventListener('input', (e) => {
    searchQuery = e.target.value.toLowerCase().trim();
    renderPublications();
  });
}

function renderPublications() {
  const container = document.getElementById('publications-container');
  const countBadge = document.getElementById('pub-results-count');
  if (!container) return;

  const filtered = PUBLICATIONS_DATA.filter(pub => {
    const matchesCategory = activeCategory === 'all' || pub.category === activeCategory;
    const matchesSearch = !searchQuery || 
      pub.title.toLowerCase().includes(searchQuery) ||
      pub.authors.toLowerCase().includes(searchQuery) ||
      pub.journal.toLowerCase().includes(searchQuery) ||
      pub.year.toString().includes(searchQuery) ||
      (pub.tags && pub.tags.some(t => t.toLowerCase().includes(searchQuery)));

    return matchesCategory && matchesSearch;
  });

  if (countBadge) {
    countBadge.textContent = `Showing ${filtered.length} of ${PUBLICATIONS_DATA.length} publications`;
  }

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="text-align: center; padding: 48px; background: var(--bg-card); border-radius: var(--radius-lg); border: 1px dashed var(--border-subtle);">
        <p style="font-size: 1.125rem; font-weight: 600; color: var(--text-muted); margin-bottom: 8px;">No matching publications found</p>
        <p style="font-size: 0.875rem; color: var(--text-muted);">Try adjusting your search terms or selecting a different category tab.</p>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(pub => {
    // Bold Arun's name in authors list
    const highlightedAuthors = pub.authors
      .replace(/B\.\s*Arun/g, '<strong>B. Arun</strong>')
      .replace(/Arun,\s*B/g, '<strong>Arun, B</strong>')
      .replace(/Arun\s*B/g, '<strong>Arun B</strong>');

    return `
      <article class="pub-card" data-pub-id="${pub.id}">
        <div class="pub-card-top">
          <div style="display: flex; align-items: center; gap: 10px;">
            <span class="pub-index-badge">#${pub.id}</span>
            <span class="pub-category-pill">${pub.categoryLabel}</span>
          </div>
          ${pub.citations > 0 ? `
            <span class="pub-citation-badge">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
              ${pub.citations} Citations
            </span>
          ` : ''}
        </div>

        <h3 class="pub-title">
          <a href="${pub.url}" target="_blank" rel="noopener noreferrer">${pub.title}</a>
        </h3>

        <p class="pub-authors">${highlightedAuthors}</p>

        <p class="pub-meta-line">
          <span class="pub-journal">${pub.journal}</span>
          ${pub.volume ? `<strong>${pub.volume}</strong>` : ''}
          ${pub.issue ? `(${pub.issue})` : ''}
          ${pub.pages ? `, ${pub.pages}` : ''}
          <span class="pub-year">(${pub.year})</span>
          ${pub.doi ? `• <span style="font-family: var(--font-mono); font-size: 0.8125rem;">DOI: ${pub.doi}</span>` : ''}
        </p>

        ${pub.abstract ? `<p class="pub-abstract">${pub.abstract}</p>` : ''}

        <div class="pub-footer">
          <div class="pub-tags">
            ${pub.tags ? pub.tags.map(tag => `<span class="pub-tag">#${tag}</span>`).join('') : ''}
          </div>
          <div class="pub-actions">
            <button class="pub-btn btn-cite" data-pub-id="${pub.id}">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>
              BibTeX
            </button>
            <a href="${pub.url}" target="_blank" rel="noopener noreferrer" class="pub-btn">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
              View Article
            </a>
          </div>
        </div>
      </article>
    `;
  }).join('');

  // Attach Cite click handlers
  container.querySelectorAll('.btn-cite').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const pubId = parseInt(btn.getAttribute('data-pub-id'), 10);
      const pub = PUBLICATIONS_DATA.find(p => p.id === pubId);
      if (pub) {
        openBibTeXModal(pub);
      }
    });
  });
}

/* --------------------------------------------------------------------------
   BIBTEX MODAL & COPY TO CLIPBOARD
   -------------------------------------------------------------------------- */
function initBibTeXModal() {
  const modal = document.getElementById('bibtex-modal');
  const closeBtn = document.getElementById('modal-close-btn');
  const copyBtn = document.getElementById('modal-copy-btn');
  const bibtexTextarea = document.getElementById('bibtex-textarea');

  closeBtn?.addEventListener('click', closeBibTeXModal);
  modal?.addEventListener('click', (e) => {
    if (e.target === modal) closeBibTeXModal();
  });

  copyBtn?.addEventListener('click', () => {
    if (!bibtexTextarea) return;
    navigator.clipboard.writeText(bibtexTextarea.value).then(() => {
      const originalText = copyBtn.innerHTML;
      copyBtn.innerHTML = `
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
        Copied to Clipboard!
      `;
      setTimeout(() => {
        copyBtn.innerHTML = originalText;
      }, 2000);
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal?.classList.contains('active')) {
      closeBibTeXModal();
    }
  });
}

function openBibTeXModal(pub) {
  const modal = document.getElementById('bibtex-modal');
  const textarea = document.getElementById('bibtex-textarea');
  const title = document.getElementById('modal-pub-title');

  if (textarea) textarea.value = getBibTeX(pub);
  if (title) title.textContent = `BibTeX Citation: ${pub.title}`;
  modal?.classList.add('active');
}

function closeBibTeXModal() {
  document.getElementById('bibtex-modal')?.classList.remove('active');
}

/* --------------------------------------------------------------------------
   ANIMATED IMPACT METRICS COUNTER
   -------------------------------------------------------------------------- */
function initImpactCounters() {
  const counters = document.querySelectorAll('.impact-num[data-target]');
  if (counters.length === 0) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counter = entry.target;
        const target = parseInt(counter.getAttribute('data-target'), 10);
        const suffix = counter.getAttribute('data-suffix') || '';
        let count = 0;
        const speed = Math.max(1, Math.floor(target / 40));

        const updateCount = () => {
          count += speed;
          if (count >= target) {
            counter.textContent = `${target}${suffix}`;
          } else {
            counter.textContent = `${count}${suffix}`;
            requestAnimationFrame(updateCount);
          }
        };

        updateCount();
        obs.unobserve(counter);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(c => observer.observe(c));
}

/* --------------------------------------------------------------------------
   CONTACT FORM SUBMISSION WITH FALLBACK
   -------------------------------------------------------------------------- */
function initContactForm() {
  const form = document.getElementById('contact-form');
  const feedback = document.getElementById('form-feedback');

  form?.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('contact-name')?.value.trim();
    const email = document.getElementById('contact-email')?.value.trim();
    const subject = document.getElementById('contact-subject')?.value.trim();
    const message = document.getElementById('contact-message')?.value.trim();

    if (!name || !email || !message) {
      if (feedback) {
        feedback.textContent = 'Please fill out all required fields.';
        feedback.style.color = '#ef4444';
      }
      return;
    }

    // Compose mailto fallback
    const mailtoLink = `mailto:arunskalikavu@gmail.com?subject=${encodeURIComponent('[Academic Inquiry] ' + subject)}&body=${encodeURIComponent(`Dear Arun,\n\nName: ${name}\nEmail: ${email}\n\nMessage:\n${message}`)}`;

    if (feedback) {
      feedback.innerHTML = `
        <span style="color: var(--accent-emerald); font-weight: 600;">
          Thank you, ${name}! Opening your email client to send your inquiry...
        </span>
      `;
    }

    setTimeout(() => {
      window.location.href = mailtoLink;
    }, 600);
  });
}

/* --------------------------------------------------------------------------
   BACK TO TOP BUTTON
   -------------------------------------------------------------------------- */
function initBackToTop() {
  const btn = document.getElementById('back-to-top');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* --------------------------------------------------------------------------
   MINI-CAROUSEL CONTROLLER
   -------------------------------------------------------------------------- */
function initCarousels() {
  document.querySelectorAll('[data-carousel]').forEach(carousel => {
    const slides = carousel.querySelectorAll('.carousel-slide');
    const dotsContainer = carousel.querySelector('.carousel-dots');
    const prevBtn = carousel.querySelector('.carousel-btn.prev');
    const nextBtn = carousel.querySelector('.carousel-btn.next');
    let currentIndex = 0;

    if (slides.length <= 1) {
      if (prevBtn) prevBtn.style.display = 'none';
      if (nextBtn) nextBtn.style.display = 'none';
      if (dotsContainer) dotsContainer.style.display = 'none';
      return;
    }

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    let autoplayTimer;
    let isHovered = false;
    let hasFocus = false;

    // Build dots
    if (dotsContainer) {
      dotsContainer.innerHTML = '';
      slides.forEach((_, i) => {
        const dot = document.createElement('span');
        dot.className = `carousel-dot ${i === 0 ? 'active' : ''}`;
        dot.addEventListener('click', (e) => {
          e.stopPropagation();
          goToSlide(i);
          startAutoplay();
        });
        dotsContainer.appendChild(dot);
      });
    }

    function goToSlide(index) {
      slides[currentIndex].classList.remove('active');
      const dots = dotsContainer?.querySelectorAll('.carousel-dot');
      if (dots && dots[currentIndex]) dots[currentIndex].classList.remove('active');

      currentIndex = (index + slides.length) % slides.length;

      slides[currentIndex].classList.add('active');
      if (dots && dots[currentIndex]) dots[currentIndex].classList.add('active');
    }

    prevBtn?.addEventListener('click', (e) => {
      e.stopPropagation();
      goToSlide(currentIndex - 1);
      startAutoplay();
    });

    nextBtn?.addEventListener('click', (e) => {
      e.stopPropagation();
      goToSlide(currentIndex + 1);
      startAutoplay();
    });

    function stopAutoplay() {
      window.clearInterval(autoplayTimer);
      autoplayTimer = undefined;
    }

    function startAutoplay() {
      stopAutoplay();
      if (prefersReducedMotion || isHovered || hasFocus || document.hidden) return;
      autoplayTimer = window.setInterval(() => goToSlide(currentIndex + 1), 6000);
    }

    carousel.addEventListener('mouseenter', () => {
      isHovered = true;
      stopAutoplay();
    });
    carousel.addEventListener('mouseleave', () => {
      isHovered = false;
      startAutoplay();
    });
    carousel.addEventListener('focusin', () => {
      hasFocus = true;
      stopAutoplay();
    });
    carousel.addEventListener('focusout', (event) => {
      if (!carousel.contains(event.relatedTarget)) {
        hasFocus = false;
        startAutoplay();
      }
    });
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) stopAutoplay();
      else startAutoplay();
    });
    startAutoplay();
  });
}

/* --------------------------------------------------------------------------
   IMAGE LIGHTBOX MODAL
   -------------------------------------------------------------------------- */
function initLightbox() {
  const modal = document.getElementById('lightbox-modal');
  const modalImg = document.getElementById('lightbox-img');
  const modalCaption = document.getElementById('lightbox-caption');
  const closeBtn = document.getElementById('lightbox-close-btn');

  document.addEventListener('click', (e) => {
    // Ignore carousel navigation clicks
    if (e.target.closest('.carousel-btn, .carousel-dots, .carousel-dot')) return;

    const trigger = e.target.closest('[data-zoom-src], .timeline-proof-badge, .proof-badge-thumb, .carousel-slide.active, .album-thumb-item, .card-img-wrapper');
    if (trigger && !trigger.closest('#lightbox-modal')) {
      const src = trigger.getAttribute('data-zoom-src') || 
                  trigger.querySelector('img')?.getAttribute('data-zoom-src') || 
                  trigger.querySelector('img')?.getAttribute('src') || 
                  trigger.getAttribute('src');
      const caption = trigger.getAttribute('data-caption') || 
                      trigger.querySelector('img')?.getAttribute('data-caption') || 
                      trigger.querySelector('img')?.getAttribute('alt') || 
                      trigger.getAttribute('alt') || '';
      if (src && modalImg) {
        modalImg.src = src;
        if (modalCaption) modalCaption.textContent = caption;
        modal?.classList.add('active');
      }
    }
  });

  closeBtn?.addEventListener('click', () => modal?.classList.remove('active'));
  modal?.addEventListener('click', (e) => {
    if (e.target === modal || e.target === closeBtn) modal?.classList.remove('active');
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal?.classList.contains('active')) {
      modal?.classList.remove('active');
    }
  });
}

/* --------------------------------------------------------------------------
   COLLAPSIBLE ALBUM DRAWERS
   -------------------------------------------------------------------------- */
function initAlbumDrawers() {
  const albumCards = document.querySelectorAll('.gallery-album-card');
  const toggleAllBtn = document.getElementById('album-toggle-all-btn');

  function toggleAlbum(card) {
    card.classList.toggle('open');
    const isOpen = card.classList.contains('open');
    const header = card.querySelector('.album-header');
    const hint = card.querySelector('.album-state-hint');
    if (header) header.setAttribute('aria-expanded', isOpen);
    if (hint) hint.textContent = isOpen ? 'Collapse ▲' : 'View Photos ▼';
  }

  albumCards.forEach(card => {
    const header = card.querySelector('.album-header');
    header?.addEventListener('click', () => toggleAlbum(card));
    header?.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleAlbum(card);
      }
    });
  });

  let allOpen = false;
  toggleAllBtn?.addEventListener('click', () => {
    allOpen = !allOpen;
    albumCards.forEach(card => {
      if (allOpen) {
        card.classList.add('open');
      } else {
        card.classList.remove('open');
      }
      const header = card.querySelector('.album-header');
      const hint = card.querySelector('.album-state-hint');
      if (header) header.setAttribute('aria-expanded', allOpen);
      if (hint) hint.textContent = allOpen ? 'Collapse ▲' : 'View Photos ▼';
    });
    toggleAllBtn.textContent = allOpen ? 'Collapse All Albums' : 'Expand All Albums';
  });
}




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
        const cardWidth = 320;
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
    preview.style.top = `${Math.round(y)}px`;
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
