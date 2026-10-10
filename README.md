# Arun B – Academic Research Portfolio Repository

Welcome to the official source repository for the academic research portfolio of **Arun B (B. Arun)**, Senior Research Scholar affiliated with the **School of Physics, University of Hyderabad** (conducting research in the **CASEST laboratory** under **Prof. K. C. James Raju**).

---

## 📁 Repository Structure Overview

The repository has been cleanly separated into dedicated folders for maintainability and automated synchronization:

```
portfolio/
├── website/                     # 🌐 Complete production portfolio website
│   ├── index.html               # Main academic research portfolio homepage
│   ├── cv.html                  # Formal printable Curriculum Vitae (PDF ready)
│   ├── resources.txt            # Scholarly profile reference links
│   ├── HOW_TO_UPDATE.md         # Step-by-step content & image maintenance guide
│   ├── scripts/
│   │   └── update_scholar.py    # Dynamic Google Scholar sync engine
│   └── assets/
│       ├── css/
│       │   └── styles.css       # Clean academic styles & responsive layouts
│       ├── js/
│       │   ├── main.js          # Interactive features (carousels, hover-zoom, modals)
│       │   └── publications-data.js # Bibliographic dataset for all 22+ publications
│       └── images/              # Organized by section and equipment
│           ├── profile/         # Profile avatars and portraits
│           ├── setups/          # In-house experimental setups (VNA-FMR, magnetoelectric, etc.)
│           ├── facilities/      # Laboratory facilities (sputtering, MOKE, cleanroom, etc.)
│           ├── conferences/     # Conference presentation proofs & certificates
│           └── gallery/         # Supplementary fieldwork & lab documentary archive
│
├── .github/
│   └── workflows/
│       └── update_scholar.yml   # 15-day automated Google Scholar sync workflow
├── scripts/
│   └── update_scholar.py        # Root wrapper for local Scholar sync
├── index.html                   # Root entry point (auto-redirects to website/index.html)
├── cv.html                      # Root CV entry point (auto-redirects to website/cv.html)
└── README.md                    # This repository guide
```

---

## 🚀 How to Run & Preview Locally

### Option 1: Direct Browser Opening
- Double-click `website/index.html` (or root `index.html` which automatically opens `website/index.html`).
- Zero dependencies required; runs 100% offline.

### Option 2: Python Local Server
Run in PowerShell or terminal:
```powershell
python -m http.server 8080
```
Then visit: [http://localhost:8080](http://localhost:8080) (or [http://localhost:8080/website/](http://localhost:8080/website/)).

---

## 📝 How to Update Website Content & Add Images

To add photos of new equipment, more photos to existing setups, new conference presentations, or new facilities, consult the comprehensive guide:
👉 [**website/HOW_TO_UPDATE.md**](website/HOW_TO_UPDATE.md)

### Quick Examples:
- **Adding photos to an existing setup**: Drop photos into `website/assets/images/setups/<setup-name>/` and add a slide in `website/index.html`.
- **Adding a new equipment setup**: Create `website/assets/images/setups/<new-setup>/`, add your photos, and paste the ready-to-use card template in `website/index.html`.
- **Adding a conference presentation**: Save the certificate in `website/assets/images/conferences/` and add a timeline item in `website/index.html`.

---

## 🔄 Dynamic Google Scholar Auto-Sync

- **Automatic (Every 15 Days)**:
  GitHub Actions runs `.github/workflows/update_scholar.yml` on the 1st and 15th of every month. It scrapes Google Scholar (`user=Su9nLc4AAAAJ`), updates citation statistics (185+ citations, h-index 7, i10-index 7) and publications in `website/assets/js/publications-data.js` and `website/index.html`, and auto-commits the changes.
- **Manual Local Run**:
  Run anytime from the terminal:
  ```powershell
  python scripts/update_scholar.py
  ```

---

## 🌐 How to Deploy to GitHub Pages

1. Initialize git and commit:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit of clean research portfolio structure"
   ```
2. Link your GitHub repository:
   ```powershell
   git remote add origin https://github.com/ArunBhas/ArunBhas.github.io.git
   git branch -M main
   git push -u origin main
   ```
3. In GitHub:
   - Go to **Settings** &rarr; **Pages** &rarr; Source: **Deploy from a branch** &rarr; Select `main` / `/root` &rarr; Click **Save**.
   - Visitors will automatically load the website at `https://arunbhas.github.io/`.
