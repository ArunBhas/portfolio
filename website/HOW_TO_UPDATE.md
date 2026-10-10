# 📖 Website Content Maintenance & Update Guide

This guide explains how to easily update and maintain your academic research portfolio website, add new equipment, add new photos to existing setups, and update conferences and gallery archives.

---

## 📁 Website Folder Organization

All files related to the live website reside inside the `website/` directory:

```
website/
├── index.html                   # Main academic portfolio homepage
├── cv.html                      # Formal Curriculum Vitae (Print / PDF ready)
├── resources.txt                # External scholarly profile links
├── HOW_TO_UPDATE.md             # This maintenance guide
├── scripts/
│   └── update_scholar.py        # 15-day automated Google Scholar sync script
├── assets/
│   ├── css/
│   │   └── styles.css           # Pure white professional stylesheet
│   ├── js/
│   │   ├── main.js              # Interactive engine (carousels, zoom, modals)
│   │   └── publications-data.js # Bibliographic dataset for all publications
│   └── images/                  # Organized by section and equipment
│       ├── profile/             # Profile avatars and portraits
│       ├── setups/              # In-House Experimental Setups
│       │   ├── vna-fmr/
│       │   ├── magnetoelectric/
│       │   ├── miniature-electromagnet/
│       │   ├── four-probe/
│       │   └── optical-chopper/
│       ├── facilities/          # Characterization & Laboratory Facilities
│       │   ├── thin-film/
│       │   ├── magnetic-dynamics/
│       │   ├── structural-surface/
│       │   ├── cleanroom/
│       │   ├── accelerator-beamline/
│       │   └── metrology-spectroscopy/
│       ├── conferences/         # Conference & workshop presentation certificates
│       └── gallery/             # Supplementary fieldwork & lab documentary archive
```

---

## 1. 🔬 How to Add Images to an Existing Equipment Setup

Suppose you want to add a 4th photo to the **Miniature Electromagnet**:

1. **Save your new image** in:
   ```
   website/assets/images/setups/miniature-electromagnet/miniature-electromagnet-04.jpg
   ```
2. **Open `website/index.html`**, search for `Miniature Electromagnet`, and find the `<div class="carousel-track">`.
3. **Add a new slide**:
   ```html
   <div class="carousel-slide" data-caption="New angle of miniature electromagnet coil" data-zoom-src="assets/images/setups/miniature-electromagnet/miniature-electromagnet-04.jpg">
     <img src="assets/images/setups/miniature-electromagnet/miniature-electromagnet-04.jpg" alt="Miniature electromagnet coil" loading="lazy">
   </div>
   ```
4. Update the badge counter if desired (e.g. change `1/3` to `1/4`).

---

## 2. ⚡ How to Add a Brand-New Equipment Setup

1. **Create a folder for the equipment**:
   ```
   website/assets/images/setups/my-new-equipment/
   ```
2. **Drop your photos** inside (e.g. `equipment-01.jpg`, `equipment-02.jpg`).
3. **Open `website/index.html`**, locate `<div class="setups-grid">`, and paste this ready-to-use card template:

```html
<!-- Setup: My New Equipment -->
<div class="setup-card">
  <span class="setup-badge">Domain / Field Badge</span>
  <h3 class="setup-title">Name of the New Experimental Setup</h3>

  <!-- Mini-Carousel (supports 1 or more images) -->
  <div class="mini-carousel" data-carousel>
    <div class="carousel-track">
      <div class="carousel-slide active" data-caption="Primary view of the diagnostic bench" data-zoom-src="assets/images/setups/my-new-equipment/equipment-01.jpg">
        <img src="assets/images/setups/my-new-equipment/equipment-01.jpg" alt="Setup Primary View" loading="lazy">
      </div>
      <div class="carousel-slide" data-caption="Close-up detail of the sensor stage" data-zoom-src="assets/images/setups/my-new-equipment/equipment-02.jpg">
        <img src="assets/images/setups/my-new-equipment/equipment-02.jpg" alt="Setup Stage Detail" loading="lazy">
      </div>
    </div>
    <div class="carousel-nav">
      <button class="carousel-prev" aria-label="Previous image">&lsaquo;</button>
      <button class="carousel-next" aria-label="Next image">&rsaquo;</button>
    </div>
    <div class="carousel-badge">1/2 &bull; View Description</div>
  </div>

  <p class="setup-desc">
    Concise description of the system engineering, operational parameters, and research applications.
  </p>

  <div class="setup-specs">
    <div class="spec-item">
      <span class="spec-label">Operating Band</span>
      <span class="spec-value">0.1 &ndash; 20 GHz</span>
    </div>
    <div class="spec-item">
      <span class="spec-label">Automation</span>
      <span class="spec-value">LabVIEW / Python</span>
    </div>
  </div>
</div>
```

---

## 3. 🏭 How to Add or Update a Characterization Facility

1. Save facility photos in `website/assets/images/facilities/<category>/`.
2. Open `website/index.html` under `<section id="facilities">` &rarr; `<div class="facilities-grid">`.
3. Add slides to the existing facility's carousel or add a new facility card using the clean facility layout.

---

## 4. 🎓 How to Add a New Conference / Presentation Record

1. Save the certificate/presentation photo in:
   ```
   website/assets/images/conferences/my-new-conference.jpg
   ```
2. Open `website/index.html` under `<div class="timeline-container">`.
3. Add a new timeline entry:

```html
<div class="timeline-item">
  <div class="timeline-dot"></div>
  <div class="timeline-content">
    <div class="timeline-header">
      <span class="timeline-badge poster">Oral / Poster Presentation</span>
      <span class="timeline-date">DD–DD Month 2026</span>
    </div>
    <h3 class="timeline-event">Conference Name (ACRONYM 2026)</h3>
    <div class="timeline-location">Host Institution, City, Country</div>
    
    <div class="timeline-proof-badge" data-caption="Title of the paper or poster" data-zoom-src="assets/images/conferences/my-new-conference.jpg">
      <img src="assets/images/conferences/my-new-conference.jpg" alt="Conference Certificate" loading="lazy">
      <span>📜 Presentation Certificate</span>
      <span class="proof-hint">🔍 Hover to Zoom</span>
    </div>

    <p class="timeline-desc">
      Brief summary of findings presented.
    </p>
  </div>
</div>
```

---

## 5. 🖼️ How to Add a Photo to the Filmstrip Gallery

1. Save the photo in `website/assets/images/gallery/my-new-photo.jpg`.
2. Open `website/index.html` under `<section id="gallery">` &rarr; `<div class="gallery-grid">`.
3. Add a gallery card:

```html
<div class="gallery-card" data-caption="Detailed caption describing the photo" data-zoom-src="assets/images/gallery/my-new-photo.jpg">
  <div class="gallery-card-img-box">
    <img src="assets/images/gallery/my-new-photo.jpg" alt="Short description" loading="lazy">
  </div>
  <div class="gallery-card-body">
    <div class="gallery-card-title">Short Title</div>
    <div class="gallery-card-sub">Event / Context</div>
  </div>
</div>
```

---

## 🔄 Automated Dynamic Synchronization (Google Scholar & GitHub)

- **Daily Automation (Every 24 Hours)**:
  When hosted on GitHub, `.github/workflows/update_scholar.yml` runs automatically every day at 00:00 UTC (05:30 AM IST).
  1. **Google Scholar**: Fetches latest citation metrics (total citations, h-index, i10-index, and per-paper counts) and updates `publications-data.js` and `index.html`.
  2. **GitHub Repositories**: Queries your GitHub account (`@ArunBhas`), filters out the `portfolio` repo, preserves rich descriptions for your core tools, and automatically adds any new public repositories to the "Open-Source Scientific Software & Repositories" section.
- **Manual Runs**:
  - In GitHub: Go to **Actions** &rarr; **Dynamic Academic Sync (Scholar & GitHub)** &rarr; **Run workflow**.
  - Locally:
    ```powershell
    python scripts/update_scholar.py
    python scripts/update_github_repos.py
    ```

---

## 🚀 How to Preview & Run

### Direct Browser Opening:
Double-click `website/index.html` (or the root `index.html` which redirects automatically).

### Local Server:
```powershell
# From the portfolio directory:
python -m http.server 8080
```
Open [http://localhost:8080](http://localhost:8080) in your browser.

