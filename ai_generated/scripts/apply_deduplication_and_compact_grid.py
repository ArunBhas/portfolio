import re
import sys
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 1. UPDATE index.html: REMOVE REPEATED IMAGES
# ==============================================================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# A. In #setups:
# Setup 2: Remove repeated gallery_05.jpg slide (keep experimental_setups_01.jpg)
for sc in soup.find_all('div', class_='setup-card'):
    title = sc.find('h3', class_='setup-title')
    if title and 'Magnetoelectric' in title.text:
        car = sc.find('div', class_='mini-carousel')
        if car:
            # Replace carousel with a clean, ultra-compact single photo frame (height: 52px)
            new_box_html = '''<div class="card-img-wrapper" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_01.jpg" data-caption="Magnetoelectric Voltage Measurement Facility: dynamic ME coefficient testing bench with lock-in detection and AC/DC bias">
            <img src="assets/images/sites/experimental_setups/experimental_setups_01.jpg" alt="Magnetoelectric Voltage Facility" loading="lazy">
            <span class="carousel-slide-badge">Dynamic ME Bench</span>
            <span class="carousel-zoom-hint">🔍 Enlarge</span>
          </div>'''
            car.replace_with(BeautifulSoup(new_box_html, 'html.parser').find('div'))
            print("Setup 2: Removed duplicate slide, converted to single compact frame.")

# Setup 3: Remove repeated gallery_04.jpg slide (keep experimental_setups_02.jpg)
for sc in soup.find_all('div', class_='setup-card'):
    title = sc.find('h3', class_='setup-title')
    if title and 'Electromagnet' in title.text:
        car = sc.find('div', class_='mini-carousel')
        if car:
            # Replace carousel with a clean, ultra-compact single photo frame (height: 52px)
            new_box_html = '''<div class="card-img-wrapper" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_02.jpg" data-caption="Miniature Electromagnet (800 Oe @ 1A) custom engineered for high-frequency microwave wafer probe stations">
            <img src="assets/images/sites/experimental_setups/experimental_setups_02.jpg" alt="Miniature Electromagnet" loading="lazy">
            <span class="carousel-slide-badge">800 Oe Probe Magnet</span>
            <span class="carousel-zoom-hint">🔍 Enlarge</span>
          </div>'''
            car.replace_with(BeautifulSoup(new_box_html, 'html.parser').find('div'))
            print("Setup 3: Removed duplicate slide, converted to single compact frame.")

# B. In #facilities:
# Facility 5 (Ion Beam Accelerator): Remove repeated experience_18.jpg slide (keep gallery_07.jpg)
for fc in soup.find_all('div', class_='facility-card'):
    name = fc.find('div', class_='facility-name')
    if name and 'Accelerator' in name.text:
        car = fc.find('div', class_='mini-carousel')
        if car:
            new_box_html = '''<div class="card-img-wrapper" data-zoom-src="assets/images/sites/gallery/gallery_07.jpg" data-caption="Swift Heavy Ion (SHI) Irradiation Beamline Experiment at Inter-University Accelerator Centre (IUAC), New Delhi">
            <img src="assets/images/sites/gallery/gallery_07.jpg" alt="SHI Beamline at IUAC" loading="lazy">
            <span class="carousel-slide-badge">Pelletron Beamline</span>
            <span class="carousel-zoom-hint">🔍 Enlarge</span>
          </div>'''
            car.replace_with(BeautifulSoup(new_box_html, 'html.parser').find('div'))
            print("Facility 5: Removed duplicate slide, converted to single compact frame.")

# C. In #gallery:
# Reorganize into a clean Curated Visual Evidence Gallery with 4-6 images displayed in a single screen row!
# Containing the 13 unique images that do NOT appear anywhere else on the website.
unique_gallery_manifest = [
    {
        'src': 'assets/images/sites/gallery/gallery_06.jpg',
        'title': 'ICMAGMA 2023 Poster Session',
        'tag': 'Symposium Proceeding',
        'desc': 'High-frequency damping and magnetic anisotropy findings at Hyderabad'
    },
    {
        'src': 'assets/images/sites/conferences/conferences_03.jpg',
        'title': 'NANOscientific Symposium 2023',
        'tag': 'International Presentation',
        'desc': 'Nanoscale scanning probe characterization methodologies'
    },
    {
        'src': 'assets/images/sites/conferences/conferences_07.jpg',
        'title': 'Frontiers in Physics (FIP 2023)',
        'tag': 'Poster Presentation',
        'desc': 'School of Physics, UoH session on microwave magnetic materials'
    },
    {
        'src': 'assets/images/sites/conferences/conferences_08.jpg',
        'title': 'ICRAMM 2019 Conference',
        'tag': 'Oral Presentation',
        'desc': 'International Conference on Recent Advances in Materials'
    },
    {
        'src': 'assets/images/sites/workshops/workshops_04.jpg',
        'title': 'Rietveld Refinement Training',
        'tag': 'Specialized Workshop',
        'desc': 'Crystallographic structural refinement from powder XRD data'
    },
    {
        'src': 'assets/images/sites/workshops/workshops_05.jpg',
        'title': 'Python Scientific Computing',
        'tag': 'Data Modeling Workshop',
        'desc': 'Hands-on scientific computation, curve fitting, and analytics certification'
    },
    {
        'src': 'assets/images/sites/workshops/workshops_06.jpg',
        'title': 'Magnetism & Measurements',
        'tag': 'National Symposium',
        'desc': 'Pondicherry University symposium on magnetic instrumentation'
    },
    {
        'src': 'assets/images/sites/workshops/workshops_08.jpg',
        'title': 'INUP-i2i Nanofab Technologies',
        'tag': 'Cleanroom Training',
        'desc': 'IIT Bombay certification covering semiconductor fabrication'
    },
    {
        'src': 'assets/images/sites/experience/experience_08.jpg',
        'title': 'UV/VIS/NIR Sample Chamber',
        'tag': 'Optical Metrology',
        'desc': 'Thin film optical absorbance and transmission fixture'
    },
    {
        'src': 'assets/images/sites/experience/experience_12.jpg',
        'title': 'Stylus Profilometer Facility',
        'tag': 'Surface Metrology',
        'desc': 'Veeco/Bruker step-height measurement at Centre for Nanotechnology'
    },
    {
        'src': 'assets/images/sites/experience/experience_17.jpg',
        'title': 'AFM Vibration Isolation Table',
        'tag': 'Nanoscale Imaging',
        'desc': 'Acoustic isolation enclosure and active vibration damping system'
    },
    {
        'src': 'assets/images/sites/home/home_01.jpg',
        'title': 'Applied Physics Research Lab',
        'tag': 'Laboratory Identity',
        'desc': 'Official branding and group insignia from Arun B research portfolio'
    },
    {
        'src': 'assets/images/sites/home/home_02.jpg',
        'title': 'Arun B Doctoral Profile',
        'tag': 'Academic Scholar',
        'desc': 'School of Physics, University of Hyderabad (CASEST Laboratory)'
    }
]

gallery_cards_html = []
for item in unique_gallery_manifest:
    card = f'''        <div class="gallery-card" data-zoom-src="{item['src']}" data-caption="{item['title']} • {item['desc']}">
          <div class="gallery-card-img-box">
            <img src="{item['src']}" alt="{item['title']}" loading="lazy">
            <span class="gallery-card-zoom-btn">🔍</span>
          </div>
          <div class="gallery-card-body">
            <div class="gallery-card-title">{item['title']}</div>
            <div class="gallery-card-tag">{item['tag']}</div>
          </div>
        </div>'''
    gallery_cards_html.append(card)

joined_cards = '\n'.join(gallery_cards_html)

new_gallery_section = f'''  <!-- ==========================================================================
       CURATED VISUAL EVIDENCE GALLERY (4-6 IMAGES PER SCREEN ROW • ZERO REPEATS)
       ========================================================================== -->
  <section id="gallery" class="section section-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-badge">Documentary Archives</span>
        <h2 class="section-title">Curated Visual Evidence & Fieldwork Gallery</h2>
        <p class="section-subtitle">
          Supplementary photographic records of specialized national workshops, symposium presentations, 
          and analytical instrumentation. Hover over any thumbnail to inspect high-resolution details.
        </p>
      </div>

      <!-- Single Screen 4-6 Images Layout Grid -->
      <div class="gallery-grid">
{joined_cards}
      </div>

    </div>
  </section>'''

# Replace gallery section in soup
old_gallery = soup.find('section', id='gallery')
if old_gallery:
    old_gallery.replace_with(BeautifulSoup(new_gallery_section, 'html.parser').find('section'))
    print("Replaced #gallery with compact 5-column grid (4-6 per row, 13 unique images)!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("index.html successfully updated!")

