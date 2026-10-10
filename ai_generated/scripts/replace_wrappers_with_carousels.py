import sys
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Setup 2
setup_2 = None
for c in soup.find_all('div', class_='setup-card'):
    title_el = c.find('h3', class_='setup-title')
    if title_el and 'Magnetoelectric' in title_el.text:
        setup_2 = c
        break

if setup_2:
    img_wrap = setup_2.find('div', class_='card-img-wrapper')
    if img_wrap:
        carousel_html = '''<div class="mini-carousel" data-carousel>
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
        new_tag = BeautifulSoup(carousel_html, 'html.parser').find('div')
        img_wrap.replace_with(new_tag)
        print("Replaced Setup 2 image wrapper with mini-carousel!")

# 2. Setup 3
setup_3 = None
for c in soup.find_all('div', class_='setup-card'):
    title_el = c.find('h3', class_='setup-title')
    if title_el and 'Electromagnet' in title_el.text:
        setup_3 = c
        break

if setup_3:
    img_wrap = setup_3.find('div', class_='card-img-wrapper')
    if img_wrap:
        carousel_html = '''<div class="mini-carousel" data-carousel>
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
        new_tag = BeautifulSoup(carousel_html, 'html.parser').find('div')
        img_wrap.replace_with(new_tag)
        print("Replaced Setup 3 image wrapper with mini-carousel!")

# 3. Facility 5
fac_5 = None
for c in soup.find_all('div', class_='facility-card'):
    name_el = c.find('div', class_='facility-name')
    if name_el and 'Accelerator' in name_el.text:
        fac_5 = c
        break

if fac_5:
    img_wrap = fac_5.find('div', class_='card-img-wrapper')
    if img_wrap:
        carousel_html = '''<div class="mini-carousel" data-carousel>
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
        new_tag = BeautifulSoup(carousel_html, 'html.parser').find('div')
        img_wrap.replace_with(new_tag)
        print("Replaced Facility 5 image wrapper with mini-carousel!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("All card-img-wrappers replaced with standardized mini-carousels!")

