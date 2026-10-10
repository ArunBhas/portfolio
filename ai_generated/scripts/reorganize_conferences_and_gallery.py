import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Conferences Timeline Items to use .timeline-photo-pill
# We replace each timeline-thumb-box with the sleek timeline-photo-pill
timeline_replacements = [
    (
        'assets/images/sites/conferences/conferences_01.jpg',
        'ICMAGMA 2025 Conference Presentation @ J.N. Tata Auditorium, IISc Bangalore',
        'ICMAGMA 2025 Photo'
    ),
    (
        'assets/images/sites/workshops/workshops_01.jpg',
        'Powder and GI-XRD Advanced Instrument Training Certificate @ School of Physics, UoH',
        'GI-XRD Certificate'
    ),
    (
        'assets/images/sites/workshops/workshops_02.jpg',
        'Workshop on Ion/Laser Beams in Nano-Science (WINS-2025) Certificate @ CFN, UoH',
        'WINS-2025 Certificate'
    ),
    (
        'assets/images/sites/workshops/workshops_03.jpg',
        'ASSURE Workshop on Magnetism in collaboration with TIFR Hyderabad Certificate',
        'ASSURE Certificate'
    ),
    (
        'assets/images/sites/conferences/conferences_02.jpg',
        'Frontiers in Physics (FIP 2024) Poster Presentation Certificate @ School of Physics, UoH',
        'FIP 2024 Certificate'
    ),
    (
        'assets/images/sites/conferences/conferences_05.jpg',
        '5th Asia Conference on Material and Manufacturing Technology (ACMMT 2023), Chiang Mai, Thailand',
        'ACMMT 2023 Photo'
    ),
    (
        'assets/images/sites/conferences/conferences_06.jpg',
        'ICACMP 2023 Oral Presentation Certificate @ GITAM Hyderabad',
        'ICACMP 2023 Certificate'
    ),
    (
        'assets/images/sites/conferences/conferences_04.jpg',
        'ICMAGMA 2023 Presentation & Proceedings at Hyderabad',
        'ICMAGMA 2023 Photo'
    ),
    (
        'assets/images/sites/workshops/workshops_07.jpg',
        'INUP-i2i Cleanroom Nanofabrication Certificate @ CeNSE, IISc Bangalore',
        'INUP Cleanroom Certificate'
    ),
]

# We use regex to replace each block in #conferences
# Pattern for thumb box in conference timeline:
conf_start = html.find('id="conferences"')
conf_end = html.find('</section>', conf_start)
conf_section = html[conf_start:conf_end]

for img_src, caption, label in timeline_replacements:
    # Match the timeline thumb block containing img_src
    pattern = rf'(?:<!-- Compact Media Preview -->\s*)?<div class="timeline-thumb-box">\s*<div class="timeline-thumb"[^>]*{re.escape(img_src)}[^>]*>.*?</div>\s*<div class="timeline-thumb-info">.*?</div>\s*<button class="timeline-thumb-zoom"[^>]*>.*?</button>\s*</div>'
    pill_html = f'''<button class="timeline-photo-pill" data-zoom-src="{img_src}" data-caption="{caption}" aria-label="View {label}">
              <img src="{img_src}" alt="{label}" loading="lazy">
              <span>View {label}</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            </button>'''
    
    # Also check if it was a simpler card-img-wrapper in conference
    pattern_wrapper = rf'<div class="card-img-wrapper"[^>]*{re.escape(img_src)}[^>]*>.*?</div>'
    
    if re.search(pattern, conf_section):
        conf_section = re.sub(pattern, pill_html, conf_section, count=1)
    elif re.search(pattern_wrapper, conf_section):
        conf_section = re.sub(pattern_wrapper, pill_html, conf_section, count=1)

html = html[:conf_start] + conf_section + html[conf_end:]
print("Updated conferences section with sleek inline pills!")

# 2. Build the Collapsible Thematic Albums for #gallery
albums_data = [
    {
        'id': 'album-setups',
        'icon': '⚙️',
        'title': 'In-House Instrumentation & Experimental Setups',
        'desc': 'Custom diagnostic benches, electromagnet probe stages, and automated optical choppers engineered at University of Hyderabad.',
        'photos': [
            ('assets/images/sites/experimental_setups/experimental_setups_01.jpg', 'Magnetoelectric Voltage Facility', 'Dynamic ME voltage coefficient measurement bench with lock-in detection and AC/DC bias'),
            ('assets/images/sites/experimental_setups/experimental_setups_02.jpg', 'Miniature Probe Electromagnet', 'Compact 800 Oe @ 1A electromagnet custom engineered for RF microwave wafer probe stations'),
            ('assets/images/sites/experimental_setups/experimental_setups_03.jpg', 'Precision Optical Chopper', 'Arduino Uno & BLDC-driven high-speed optical chopper generating light modulation pulses up to 2.8 kHz'),
            ('assets/images/sites/experimental_setups/experimental_setups_04.jpg', 'Optical Chopper Schematic', 'Detailed electrical circuit schematic interfacing potentiometer, ESC, Arduino Uno, and motor'),
            ('assets/images/sites/gallery/gallery_04.jpg', 'VNA-FMR Experimental Bench', 'Broadband Vector Network Analyzer Ferromagnetic Resonance system with coplanar waveguide'),
            ('assets/images/sites/gallery/gallery_05.jpg', 'VNA-FMR Standardization on FeGaB', 'Microwave S-parameter calibration and Gilbert damping factor extraction on FeGaB alloy films'),
        ]
    },
    {
        'id': 'album-synthesis',
        'icon': '🔬',
        'title': 'Thin Film Synthesis & Nanofabrication',
        'desc': 'Multi-target high-vacuum sputtering systems, vacuum maintenance, and cleanroom MEMS micro-cantilever fabrication at CeNSE IISc.',
        'photos': [
            ('assets/images/sites/experience/experience_10.jpg', 'DC/RF Sputtering System', 'Multi-target high-vacuum sputtering system at CASEST for ferromagnetic FeGaB thin films'),
            ('assets/images/sites/experience/experience_11.jpg', 'Sputtering RF/DC Power Rack', 'RF matching networks, DC power supplies, and Ar/O2 mass flow controller (MFC) console'),
            ('assets/images/sites/experience/experience_15.jpg', 'RF Deposition Chamber @ CFN', 'Radio-frequency sputtering deposition chamber at Centre for Nanotechnology'),
            ('assets/images/sites/experience/experience_09.jpg', 'Thermal & Sputter Coater', 'High-vacuum deposition system for conductive contact layer deposition and SEM pre-coating'),
            ('assets/images/sites/experience/experience_14.jpg', 'Turbo Pump Overhaul', 'Hands-on vacuum flange seal overhaul and turbomolecular pump maintenance at CASEST'),
            ('assets/images/sites/gallery/gallery_01.jpg', 'MEMS Cantilever Handover @ CeNSE', 'Receiving fabricated micro-cantilever chips from Ms. Ashwini A (CeNSE, IISc Bangalore)'),
            ('assets/images/sites/gallery/gallery_02.jpg', 'Nanofabrication Technical Review', 'Process parameter review with Mr. Venu V Bhat (Facility Technologist, CeNSE)'),
            ('assets/images/sites/gallery/gallery_03.jpg', 'INUP-i2i Cleanroom Cohort @ IISc', 'Hands-on cleanroom training batch at Centre for Nano Science and Engineering, IISc'),
        ]
    },
    {
        'id': 'album-characterization',
        'icon': '📊',
        'title': 'Advanced Characterization & Metrology Facilities',
        'desc': 'Field emission scanning electron microscopy (FESEM), grazing incidence XRD/XRR, MOKE magnetometry, stylus profilometry, and AFM.',
        'photos': [
            ('assets/images/sites/experience/experience_01.jpg', 'Conventional MOKE @ TIFR-H', 'Magneto-Optical Kerr Effect optical table and magnet poles for FeGaB hysteresis loops'),
            ('assets/images/sites/experience/experience_02.jpg', 'MOKE Precision Sample Stage', 'Precision goniometer sample holder and laser alignment setup for in-plane MOKE'),
            ('assets/images/sites/experience/experience_03.jpg', 'Field Emission SEM (FESEM)', 'High-resolution field emission scanning electron microscope at UoH for microstructures'),
            ('assets/images/sites/experience/experience_04.jpg', 'FESEM Console & EDS', 'Electron beam column control console and energy-dispersive X-ray spectroscopy terminal'),
            ('assets/images/sites/experience/experience_05.jpg', 'Bruker D8 Advance XRD/XRR', 'Bruker D8 Advance diffractometer goniometer configured for thin film phase and thickness'),
            ('assets/images/sites/experience/experience_06.jpg', 'High-Res XRD Goniometer', 'Grazing incidence XRD stage with scintillation detector for structural characterization'),
            ('assets/images/sites/experience/experience_12.jpg', 'Stylus Profilometer System @ CFN', 'Veeco/Bruker high-resolution stylus profilometer for thin film step-height profiling'),
            ('assets/images/sites/experience/experience_13.jpg', 'Stylus Profiler Stage & Optics', 'Sub-nanometer diamond stylus scanning mechanism and sample observation microscope'),
            ('assets/images/sites/experience/experience_16.jpg', 'AFM Scanning Head', 'Cantilever optical lever detection head and scanner module for surface topography'),
            ('assets/images/sites/experience/experience_17.jpg', 'AFM Vibration Isolation Table', 'Acoustic isolation enclosure and active vibration damping system ensuring atomic resolution'),
        ]
    },
    {
        'id': 'album-conferences',
        'icon': '🏛️',
        'title': 'Scientific Conferences & Symposia',
        'desc': 'Oral and poster presentations across premier national and international physics conferences.',
        'photos': [
            ('assets/images/sites/conferences/conferences_01.jpg', 'ICMAGMA 2025 @ IISc Bangalore', 'Presentation at J.N. Tata Auditorium, Indian Institute of Science (IISc), Bangalore'),
            ('assets/images/sites/conferences/conferences_02.jpg', 'Frontiers in Physics (FIP 2024)', 'Poster presentation certificate at School of Physics, University of Hyderabad'),
            ('assets/images/sites/conferences/conferences_03.jpg', 'NANOscientific Symposium Asia 2023', 'Certificate and technical presentation on nanoscale scanning probe characterization'),
            ('assets/images/sites/conferences/conferences_04.jpg', 'ICMAGMA 2023 @ Hyderabad', 'International Conference on Magnetic Materials and Applications delegate proceedings'),
            ('assets/images/sites/gallery/gallery_06.jpg', 'ICMAGMA 2023 Poster Session', 'Disseminating thin film ferromagnetic resonance and anisotropy findings'),
            ('assets/images/sites/conferences/conferences_05.jpg', 'ACMMT 2023 @ Chiang Mai, Thailand', 'Oral presentation on Pt/FeGaB/Pt trilayers at Chiang Mai, Thailand'),
            ('assets/images/sites/conferences/conferences_06.jpg', 'ICACMP 2023 @ GITAM Hyderabad', 'Oral presentation on Vector Network Analyzer FMR characterization of FeGaB films'),
            ('assets/images/sites/conferences/conferences_07.jpg', 'Frontiers in Physics (FIP 2023)', 'Poster presentation session at School of Physics, University of Hyderabad'),
            ('assets/images/sites/conferences/conferences_08.jpg', 'ICRAMM 2019 Conference', 'Presentation at International Conference on Recent Advances in Materials and Manufacturing'),
        ]
    },
    {
        'id': 'album-workshops',
        'icon': '🎓',
        'title': 'National Workshops & Specialized Hands-On Trainings',
        'desc': 'Formal training certifications in grazing incidence XRD, ion and laser beam nanostructuring, and semiconductor cleanrooms.',
        'photos': [
            ('assets/images/sites/workshops/workshops_01.jpg', 'Powder & GI-XRD Certification', 'School of Physics, UoH intensive certification in grazing incidence XRD analysis'),
            ('assets/images/sites/workshops/workshops_02.jpg', 'Ion/Laser Beams (WINS-2025)', 'CFN, UoH workshop on ion and laser beam nanostructuring and materials modification'),
            ('assets/images/sites/workshops/workshops_03.jpg', 'ASSURE Magnetism (TIFR-H)', '10-day intensive school organized with TIFR Hyderabad at Osmania University'),
            ('assets/images/sites/workshops/workshops_04.jpg', 'Rietveld Refinement Workshop', 'Advanced training on crystallographic structural refinement from powder XRD data'),
            ('assets/images/sites/workshops/workshops_05.jpg', 'Python for Scientific Computing', 'Hands-on scientific computation, automated curve-fitting, and data analytics certification'),
            ('assets/images/sites/workshops/workshops_06.jpg', 'Magnetism & Measurements', 'Pondicherry University symposium on magnetic characterization instrumentation'),
            ('assets/images/sites/workshops/workshops_07.jpg', 'INUP-i2i Cleanroom Nanofabrication', 'CeNSE, IISc Bangalore cleanroom certificate for micro-cantilever photolithography'),
            ('assets/images/sites/workshops/workshops_08.jpg', 'INUP-i2i Nanofab Technologies', 'IIT Bombay familiarization workshop certification covering semiconductor fabrication'),
        ]
    },
    {
        'id': 'album-facilities-academic',
        'icon': '📜',
        'title': 'National Accelerator Facilities & Academic Portfolio',
        'desc': 'Swift Heavy Ion (SHI) irradiation beamline at IUAC New Delhi, cryogenic PPMS, optical spectroscopy, and scholar profile.',
        'photos': [
            ('assets/images/sites/gallery/gallery_07.jpg', 'Swift Heavy Ion Beamline @ IUAC', 'Pelletron accelerator beamline hall at Inter-University Accelerator Centre, New Delhi'),
            ('assets/images/sites/experience/experience_18.jpg', 'Quantum Design PPMS Facility', 'Physical Property Measurement System with EverCool cryostat for temperature magnetometry'),
            ('assets/images/sites/experience/experience_07.jpg', 'UV/VIS/NIR Spectrophotometer', 'Optical transmission and absorption spectroscopy system for thin films'),
            ('assets/images/sites/experience/experience_08.jpg', 'UV/VIS Sample Compartment', 'Solid-state thin film sample fixture inside the dual-beam spectrophotometer'),
            ('assets/images/sites/home/home_02.jpg', 'Senior Research Scholar Arun B', 'School of Physics, University of Hyderabad (CASEST Laboratory)'),
            ('assets/images/sites/home/home_01.jpg', 'Applied Physics Research Lab Identity', 'Professional identity banner from Arun B applied physics research portfolio'),
        ]
    }
]

albums_html_parts = []
for album in albums_data:
    thumbs_html = []
    for src, title, desc in album['photos']:
        thumb_item = f'''          <div class="album-thumb-item" data-zoom-src="{src}" data-caption="{title} • {desc}">
            <div class="album-thumb-img-wrapper">
              <img src="{src}" alt="{title}" loading="lazy">
              <span class="album-thumb-overlay-btn">🔍 Enlarge</span>
            </div>
            <div class="album-thumb-label" title="{title}">{title}</div>
          </div>'''
        thumbs_html.append(thumb_item)
    
    thumbs_joined = '\n'.join(thumbs_html)
    
    card_html = f'''      <!-- Album: {album['title']} -->
      <div class="gallery-album-card" id="{album['id']}">
        <div class="album-header" role="button" tabindex="0" aria-expanded="false" aria-controls="{album['id']}-body">
          <div class="album-header-left">
            <span class="album-icon">{album['icon']}</span>
            <div>
              <div class="album-title">{album['title']}</div>
            </div>
            <span class="album-count-badge">{len(album['photos'])} Photos</span>
          </div>
          <div class="album-header-right">
            <span class="album-state-hint">View Photos ▼</span>
            <span class="album-chevron">▾</span>
          </div>
        </div>
        <div class="album-body" id="{album['id']}-body">
          <p class="album-desc">{album['desc']}</p>
          <div class="album-thumbs-grid">
{thumbs_joined}
          </div>
        </div>
      </div>'''
    albums_html_parts.append(card_html)

all_albums_html = '\n\n'.join(albums_html_parts)

new_gallery_section = f'''  <!-- ==========================================================================
       RESEARCH & EXPERIMENTAL GALLERY (ORGANIZED COLLAPSIBLE ALBUMS)
       ========================================================================== -->
  <section id="gallery" class="section section-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-badge">Visual Portfolio & Evidence</span>
        <h2 class="section-title">Research & Experimental Gallery</h2>
        <p class="section-subtitle">
          Compact thematic visual archives documenting in-house instrumentation, premier laboratory facilities, 
          academic conferences, and certified nanofabrication workshops. Click any album to browse thumbnails.
        </p>
      </div>

      <!-- Compact Album Controls Bar -->
      <div class="gallery-controls-bar">
        <div class="gallery-stats-label">
          📁 6 Curated Thematic Albums &bull; 47 High-Resolution Images
        </div>
        <button id="album-toggle-all-btn" class="album-toggle-all-btn" type="button">
          Expand All Albums
        </button>
      </div>

      <!-- Collapsible Albums List -->
      <div class="gallery-albums-list">
{all_albums_html}
      </div>

    </div>
  </section>'''

# Replace gallery section in html
gal_start = html.find('id="gallery"')
# find opening <section before gal_start
section_gal_start = html.rfind('<section', 0, gal_start)
section_gal_end = html.find('</section>', gal_start) + len('</section>')

if section_gal_start != -1 and section_gal_end != -1:
    html = html[:section_gal_start] + new_gallery_section + html[section_gal_end:]
    print("Replaced gallery section with compact collapsible album drawers!")
else:
    print("Error finding gallery section!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully!")

