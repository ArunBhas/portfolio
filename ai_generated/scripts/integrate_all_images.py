import os
import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Navigation Links in Header
old_nav_links = '''        <ul class="nav-links">
          <li><a href="#about" class="nav-link">About</a></li>
          <li><a href="#research" class="nav-link">Research</a></li>
          <li><a href="#publications" class="nav-link">Publications</a></li>
          <li><a href="#setups" class="nav-link">Setups & Innovation</a></li>
          <li><a href="#facilities" class="nav-link">Facilities</a></li>
          <li><a href="#conferences" class="nav-link">Conferences</a></li>
          <li><a href="#tools" class="nav-link">Open Source</a></li>
          <li><a href="#collaborations" class="nav-link">Collaborators</a></li>
          <li><a href="#contact" class="nav-link">Contact</a></li>
        </ul>'''

new_nav_links = '''        <ul class="nav-links">
          <li><a href="#about" class="nav-link">About</a></li>
          <li><a href="#research" class="nav-link">Research</a></li>
          <li><a href="#publications" class="nav-link">Publications</a></li>
          <li><a href="#setups" class="nav-link">Setups & Innovation</a></li>
          <li><a href="#facilities" class="nav-link">Facilities</a></li>
          <li><a href="#conferences" class="nav-link">Conferences</a></li>
          <li><a href="#gallery" class="nav-link">Gallery</a></li>
          <li><a href="#tools" class="nav-link">Open Source</a></li>
          <li><a href="#collaborations" class="nav-link">Collaborators</a></li>
          <li><a href="#contact" class="nav-link">Contact</a></li>
        </ul>'''

content = content.replace(old_nav_links, new_nav_links)

# Update nav-actions to include Original Mirror button
old_nav_actions = '''      <div class="nav-actions">
        <button id="theme-toggle-btn" class="theme-toggle-btn" aria-label="Toggle dark/light theme">
          <span id="theme-toggle-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
          </span>
        </button>
        <a href="cv.html" target="_blank" class="nav-btn-cv" style="background-color: var(--accent-emerald);">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
          Curriculum Vitae
        </a>
        <button id="mobile-menu-btn" class="mobile-menu-btn" aria-label="Toggle mobile navigation">☰</button>
      </div>'''

new_nav_actions = '''      <div class="nav-actions">
        <button id="theme-toggle-btn" class="theme-toggle-btn" aria-label="Toggle dark/light theme">
          <span id="theme-toggle-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
          </span>
        </button>
        <a href="site_mirror/home.html" target="_blank" class="nav-btn-cv" style="background-color: var(--accent-cyan); margin-right: 4px;" title="Browse local offline mirror of original Google Site">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
          Original Mirror
        </a>
        <a href="cv.html" target="_blank" class="nav-btn-cv" style="background-color: var(--accent-emerald);">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
          Curriculum Vitae
        </a>
        <button id="mobile-menu-btn" class="mobile-menu-btn" aria-label="Toggle mobile navigation">☰</button>
      </div>'''

content = content.replace(old_nav_actions, new_nav_actions)

# Update Mobile Drawer
old_drawer = '''    <a href="#conferences" class="nav-link">Conferences & Trainings</a>
    <a href="#tools" class="nav-link">Open Source Tools</a>'''

new_drawer = '''    <a href="#conferences" class="nav-link">Conferences & Trainings</a>
    <a href="#gallery" class="nav-link">Research Gallery (47 Photos)</a>
    <a href="site_mirror/home.html" target="_blank" class="nav-link" style="color: var(--accent-cyan); font-weight: 700;">🌐 Original Google Site Mirror</a>
    <a href="#tools" class="nav-link">Open Source Tools</a>'''

content = content.replace(old_drawer, new_drawer)

# 2. Update Experimental Setups (#setups) with Photos
old_setups_block = '''      <div class="setups-grid">
        
        <!-- Setup 1 -->
        <div class="setup-card">
          <span class="setup-badge">High Frequency Magnetics</span>
          <h3 class="setup-title">VNA-FMR Broadband Ferromagnetic Resonance</h3>
          <p class="setup-desc">
            Developed a comprehensive frequency-domain and field-domain Ferromagnetic Resonance (FMR) measurement system. 
            Utilizes a high-frequency coplanar waveguide (CPW) connected to a Vector Network Analyzer (VNA) positioned 
            within a calibrated electromagnet to measure S-parameters (S21, S12) across microwave frequency ranges.
          </p>

          <div class="setup-specs-grid">
            <div class="spec-item">
              <span class="spec-key">Frequency Band</span>
              <span class="spec-val">0.1 GHz – 20 GHz</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Excitation</span>
              <span class="spec-val">CPW Transmission Line</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Key Extraction</span>
              <span class="spec-val">Landé g-factor, &Delta;H, &alpha;</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Application</span>
              <span class="spec-val">FeGaB, Thin Film Alloys</span>
            </div>
          </div>
          <p style="font-size: 0.8125rem; color: var(--text-muted);">
            Standardized for research papers published in <em>Journal of Physics D</em> and <em>Journal of Applied Physics</em>.
          </p>
        </div>

        <!-- Setup 2 -->
        <div class="setup-card">
          <span class="setup-badge">Multiferroics</span>
          <h3 class="setup-title">Magnetoelectric Dynamic Voltage Facility</h3>
          <p class="setup-desc">
            Designed an automated magnetoelectric voltage measurement bench to evaluate the dynamic ME voltage coefficient 
            (&alpha;<sub>ME</sub> = &delta;V / (t &middot; &delta;H<sub>ac</sub>)) in layered magnetostrictive-piezoelectric composites. 
            Features superimposed DC bias magnetic fields and high-precision Helmholtz AC excitation with lock-in detection.
          </p>

          <div class="setup-specs-grid">
            <div class="spec-item">
              <span class="spec-key">DC Bias Field</span>
              <span class="spec-val">0 to 4000 Oe</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">AC Modulation</span>
              <span class="spec-val">Helmholtz Coils (1–10 Oe)</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Signal Recovery</span>
              <span class="spec-val">Lock-in Amplifier</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Output Parameter</span>
              <span class="spec-val">&alpha;<sub>ME</sub> (mV/cm&middot;Oe)</span>
            </div>
          </div>
          <p style="font-size: 0.8125rem; color: var(--text-muted);">
            Automated in LabVIEW for rapid field-sweep curves and resonance peak tracking.
          </p>
        </div>

        <!-- Setup 3 -->
        <div class="setup-card">
          <span class="setup-badge">Micro-Magnetics Hardware</span>
          <h3 class="setup-title">Miniature Electromagnet for Microwave Probe Stations</h3>
          <p class="setup-desc">
            Engineered a compact, high-efficiency electromagnet designed specifically to fit onto the stage of microwave 
            RF probe stations where conventional bulky electromagnets cannot be accommodated. Enables simultaneous 
            in-plane magnetic biasing during micro-probe wafer-level S-parameter measurements.
          </p>

          <div class="setup-specs-grid">
            <div class="spec-item">
              <span class="spec-key">Maximum Field</span>
              <span class="spec-val">800 Oe (Continuous)</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Current Rating</span>
              <span class="spec-val">1.0 A</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Form Factor</span>
              <span class="spec-val">Ultra-compact Probe Footprint</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Core Material</span>
              <span class="spec-val">High-permeability Soft Iron</span>
            </div>
          </div>
          <p style="font-size: 0.8125rem; color: var(--text-muted);">
            Enables high-frequency device characterization directly under controllable bias fields.
          </p>
        </div>

        <!-- Setup 4 -->
        <div class="setup-card">
          <span class="setup-badge">Open Science Hardware</span>
          <h3 class="setup-title">Low-Cost Arduino Precision Optical Chopper</h3>
          <p class="setup-desc">
            Constructed a low-cost, speed-controllable optical chopper for pulsed laser and lock-in photodetector experiments. 
            Utilizes an Arduino Uno microcontroller, a high-KV drone brushless DC (BLDC) motor, electronic speed controller (ESC), 
            and precision 3D-printed slotted discs to generate clean light pulses up to 2.8 kHz.
          </p>

          <div class="code-snippet-box">
// Arduino Servo-ESC Speed Control snippet
#include &lt;Servo.h&gt;
Servo ESC;
void setup() {
  ESC.attach(9, 1000, 2000); // ESC on Pin 9
}
void loop() {
  int potValue = analogRead(A0);
  int escSignal = map(potValue, 0, 1023, 0, 180);
  ESC.write(escSignal);
}
          </div>

          <div class="setup-specs-grid">
            <div class="spec-item">
              <span class="spec-key">Max Pulse Freq</span>
              <span class="spec-val">2.8 kHz (@ 12V)</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Total BOM Cost</span>
              <span class="spec-val">&lt; ₹3,800 INR (~$45 USD)</span>
            </div>
          </div>

          <div style="display: flex; gap: 10px; margin-top: auto;">
            <a href="https://drive.google.com/file/d/1f7LT6Znlo59VlNEy-OqHPFeafTqx5kPk/view?usp=sharing" target="_blank" rel="noopener noreferrer" class="pub-btn" style="width: 100%; justify-content: center;">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
              Download 3D Print CAD Models
            </a>
          </div>
        </div>

      </div>'''

new_setups_block = '''      <div class="setups-grid">
        
        <!-- Setup 1 -->
        <div class="setup-card">
          <span class="setup-badge">High Frequency Magnetics</span>
          <h3 class="setup-title">VNA-FMR Broadband Ferromagnetic Resonance</h3>
          
          <div class="setup-photo-grid">
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/gallery/gallery_04.jpg" data-caption="VNA-FMR experimental bench setup and coplanar waveguide sample stage at University of Hyderabad">
              <img src="assets/images/sites/gallery/gallery_04.jpg" alt="VNA-FMR Experimental Setup" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/gallery/gallery_05.jpg" data-caption="Standardization of VNA-FMR measurements on ferromagnetic FeGaB thin films">
              <img src="assets/images/sites/gallery/gallery_05.jpg" alt="VNA-FMR Calibration" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
          </div>
          <div class="card-photo-caption">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            In-house CPW test fixture & calibrated electromagnet for 0.1–20 GHz spin dynamics
          </div>

          <p class="setup-desc">
            Developed a comprehensive frequency-domain and field-domain Ferromagnetic Resonance (FMR) measurement system. 
            Utilizes a high-frequency coplanar waveguide (CPW) connected to a Vector Network Analyzer (VNA) positioned 
            within a calibrated electromagnet to measure S-parameters (S21, S12) across microwave frequency ranges.
          </p>

          <div class="setup-specs-grid">
            <div class="spec-item">
              <span class="spec-key">Frequency Band</span>
              <span class="spec-val">0.1 GHz – 20 GHz</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Excitation</span>
              <span class="spec-val">CPW Transmission Line</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Key Extraction</span>
              <span class="spec-val">Landé g-factor, &Delta;H, &alpha;</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Application</span>
              <span class="spec-val">FeGaB, Thin Film Alloys</span>
            </div>
          </div>
          <p style="font-size: 0.8125rem; color: var(--text-muted);">
            Standardized for research papers published in <em>Journal of Physics D</em> and <em>Journal of Applied Physics</em>.
          </p>
        </div>

        <!-- Setup 2 -->
        <div class="setup-card">
          <span class="setup-badge">Multiferroics</span>
          <h3 class="setup-title">Magnetoelectric Dynamic Voltage Facility</h3>
          
          <div class="card-img-wrapper" style="height: 180px; margin-bottom: 10px;" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_01.jpg" data-caption="Magnetoelectric Voltage Measurement Facility: dynamic ME coefficient testing bench">
            <img src="assets/images/sites/experimental_setups/experimental_setups_01.jpg" alt="Magnetoelectric Voltage Facility" loading="lazy">
            <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
          </div>
          <div class="card-photo-caption">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            Automated ME bench: Helmholtz AC modulation, DC electromagnet, and lock-in detection
          </div>

          <p class="setup-desc">
            Designed an automated magnetoelectric voltage measurement bench to evaluate the dynamic ME voltage coefficient 
            (&alpha;<sub>ME</sub> = &delta;V / (t &middot; &delta;H<sub>ac</sub>)) in layered magnetostrictive-piezoelectric composites. 
            Features superimposed DC bias magnetic fields and high-precision Helmholtz AC excitation with lock-in detection.
          </p>

          <div class="setup-specs-grid">
            <div class="spec-item">
              <span class="spec-key">DC Bias Field</span>
              <span class="spec-val">0 to 4000 Oe</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">AC Modulation</span>
              <span class="spec-val">Helmholtz Coils (1–10 Oe)</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Signal Recovery</span>
              <span class="spec-val">Lock-in Amplifier</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Output Parameter</span>
              <span class="spec-val">&alpha;<sub>ME</sub> (mV/cm&middot;Oe)</span>
            </div>
          </div>
          <p style="font-size: 0.8125rem; color: var(--text-muted);">
            Automated in LabVIEW for rapid field-sweep curves and resonance peak tracking.
          </p>
        </div>

        <!-- Setup 3 -->
        <div class="setup-card">
          <span class="setup-badge">Micro-Magnetics Hardware</span>
          <h3 class="setup-title">Miniature Electromagnet for Microwave Probe Stations</h3>
          
          <div class="card-img-wrapper" style="height: 180px; margin-bottom: 10px;" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_02.jpg" data-caption="Miniature Electromagnet (800 Oe @ 1A) engineered for high frequency RF probe stations">
            <img src="assets/images/sites/experimental_setups/experimental_setups_02.jpg" alt="Miniature Electromagnet" loading="lazy">
            <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
          </div>
          <div class="card-photo-caption">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            800 Oe @ 1A miniature electromagnet customized for microwave probe wafer chuck
          </div>

          <p class="setup-desc">
            Engineered a compact, high-efficiency electromagnet designed specifically to fit onto the stage of microwave 
            RF probe stations where conventional bulky electromagnets cannot be accommodated. Enables simultaneous 
            in-plane magnetic biasing during micro-probe wafer-level S-parameter measurements.
          </p>

          <div class="setup-specs-grid">
            <div class="spec-item">
              <span class="spec-key">Maximum Field</span>
              <span class="spec-val">800 Oe (Continuous)</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Current Rating</span>
              <span class="spec-val">1.0 A</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Form Factor</span>
              <span class="spec-val">Ultra-compact Probe Footprint</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Core Material</span>
              <span class="spec-val">High-permeability Soft Iron</span>
            </div>
          </div>
          <p style="font-size: 0.8125rem; color: var(--text-muted);">
            Enables high-frequency device characterization directly under controllable bias fields.
          </p>
        </div>

        <!-- Setup 4 -->
        <div class="setup-card">
          <span class="setup-badge">Open Science Hardware</span>
          <h3 class="setup-title">Low-Cost Arduino Precision Optical Chopper</h3>
          
          <div class="setup-photo-grid">
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_03.jpg" data-caption="Low-cost precision optical chopper assembly with 3D-printed slotted wheel and BLDC motor">
              <img src="assets/images/sites/experimental_setups/experimental_setups_03.jpg" alt="Precision Optical Chopper" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_04.jpg" data-caption="Optical chopper electrical connection & wiring diagram (Arduino Uno + ESC + Motor)">
              <img src="assets/images/sites/experimental_setups/experimental_setups_04.jpg" alt="Chopper Wiring Diagram" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
          </div>
          <div class="card-photo-caption">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            Hardware prototype & electronic schematic for low-jitter pulsed light modulation up to 2.8 kHz
          </div>

          <p class="setup-desc">
            Constructed a low-cost, speed-controllable optical chopper for pulsed laser and lock-in photodetector experiments. 
            Utilizes an Arduino Uno microcontroller, a high-KV drone brushless DC (BLDC) motor, electronic speed controller (ESC), 
            and precision 3D-printed slotted discs to generate clean light pulses up to 2.8 kHz.
          </p>

          <div class="code-snippet-box">
// Arduino Servo-ESC Speed Control snippet
#include &lt;Servo.h&gt;
Servo ESC;
void setup() {
  ESC.attach(9, 1000, 2000); // ESC on Pin 9
}
void loop() {
  int potValue = analogRead(A0);
  int escSignal = map(potValue, 0, 1023, 0, 180);
  ESC.write(escSignal);
}
          </div>

          <div class="setup-specs-grid">
            <div class="spec-item">
              <span class="spec-key">Max Pulse Freq</span>
              <span class="spec-val">2.8 kHz (@ 12V)</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Total BOM Cost</span>
              <span class="spec-val">&lt; ₹3,800 INR (~$45 USD)</span>
            </div>
          </div>

          <div style="display: flex; gap: 10px; margin-top: auto;">
            <a href="https://drive.google.com/file/d/1f7LT6Znlo59VlNEy-OqHPFeafTqx5kPk/view?usp=sharing" target="_blank" rel="noopener noreferrer" class="pub-btn" style="width: 100%; justify-content: center;">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
              Download 3D Print CAD Models
            </a>
          </div>
        </div>

      </div>'''

content = content.replace(old_setups_block, new_setups_block)

# 3. Update Facilities Section (#facilities) with Photos
old_facilities_block = '''      <div class="facilities-grid">
        
        <div class="facility-card">
          <div class="facility-header">
            <div class="facility-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
            </div>
            <div>
              <div class="facility-name">Thin Film Synthesis</div>
              <div class="facility-inst">CASEST & CFN, UoH</div>
            </div>
          </div>
          <ul class="facility-items">
            <li>DC & RF Magnetron Sputtering systems</li>
            <li>System maintenance, turbo pump & RF target repair</li>
            <li>Pulsed Laser Deposition (KrF Excimer PLD)</li>
            <li>Thermal Evaporation & DC Sputter coaters</li>
          </ul>
        </div>

        <div class="facility-card">
          <div class="facility-header">
            <div class="facility-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line></svg>
            </div>
            <div>
              <div class="facility-name">Magnetic Dynamics</div>
              <div class="facility-inst">UoH & TIFR Hyderabad</div>
            </div>
          </div>
          <ul class="facility-items">
            <li>Conventional MOKE (Magneto-Optical Kerr Effect) @ TIFR-H</li>
            <li>Quantum Design PPMS (Physical Property Measurement System)</li>
            <li>Broadband VNA-FMR (0.1–20 GHz)</li>
            <li>In-plane and Out-of-plane magnetic hysteresis loops</li>
          </ul>
        </div>

        <div class="facility-card">
          <div class="facility-header">
            <div class="facility-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
            </div>
            <div>
              <div class="facility-name">Structural & Surface Analysis</div>
              <div class="facility-inst">Central Facilities, UoH</div>
            </div>
          </div>
          <ul class="facility-items">
            <li>FESEM (Field Emission Scanning Electron Microscopy)</li>
            <li>Powder & GI-XRD (Grazing Incidence X-ray Diffraction)</li>
            <li>X-ray Reflectivity (XRR) thin film thickness analysis</li>
            <li>Stylus Profilometer (Veeco/Bruker) & AFM</li>
            <li>UV/VIS/NIR Spectrophotometry</li>
          </ul>
        </div>

        <div class="facility-card">
          <div class="facility-header">
            <div class="facility-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="6" cy="6" r="3"></circle><circle cx="6" cy="18" r="3"></circle><line x1="20" y1="4" x2="8.12" y2="15.88"></line><line x1="14.47" y1="14.48" x2="20" y2="20"></line><line x1="8.12" y1="8.12" x2="12" y2="12"></line></svg>
            </div>
            <div>
              <div class="facility-name">Cleanroom Nanofabrication</div>
              <div class="facility-inst">CeNSE, IISc Bangalore</div>
            </div>
          </div>
          <ul class="facility-items">
            <li>INUP-i2i Certified Cleanroom Fabrication (Class 100/1000)</li>
            <li>Optical Photolithography & Mask aligner processing</li>
            <li>Wet chemical etching & Reactive Ion Etching (RIE)</li>
            <li>MEMS micro-cantilever device fabrication & release</li>
          </ul>
        </div>

        <div class="facility-card">
          <div class="facility-header">
            <div class="facility-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
            </div>
            <div>
              <div class="facility-name">Ion Beam Accelerator Facility</div>
              <div class="facility-inst">IUAC, New Delhi</div>
            </div>
          </div>
          <ul class="facility-items">
            <li>Swift Heavy Ion (SHI) Irradiation beamline experiments</li>
            <li>High-energy Pelletron accelerator operation</li>
            <li>Ion-beam induced atomic restructuring in magnetic films</li>
            <li>Defect dynamics in polymer-nanocomposite shielding materials</li>
          </ul>
        </div>

        <div class="facility-card">
          <div class="facility-header">
            <div class="facility-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg>
            </div>
            <div>
              <div class="facility-name">Microwave High-Frequency Testing</div>
              <div class="facility-inst">CASEST Microwave Lab</div>
            </div>
          </div>
          <ul class="facility-items">
            <li>Vector Network Analyzer S-parameter characterization</li>
            <li>X-band & Ku-band rectangular waveguide fixtures</li>
            <li>Cavity perturbation dielectric measurements</li>
            <li>Shielding effectiveness (SE<sub>T</sub>, SE<sub>R</sub>, SE<sub>A</sub>) calculations</li>
          </ul>
        </div>

      </div>'''

new_facilities_block = '''      <div class="facilities-grid">
        
        <!-- Facility 1 -->
        <div class="facility-card">
          <div class="facility-header">
            <div class="facility-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
            </div>
            <div>
              <div class="facility-name">Thin Film Synthesis</div>
              <div class="facility-inst">CASEST & CFN, UoH</div>
            </div>
          </div>

          <div class="setup-photo-grid">
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/experience/experience_10.jpg" data-caption="DC/RF Sputtering Deposition Facility @ CASEST, University of Hyderabad">
              <img src="assets/images/sites/experience/experience_10.jpg" alt="DC/RF Sputtering Facility" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/experience/experience_15.jpg" data-caption="RF Deposition System @ Centre for Nanotechnology (CFN), UoH">
              <img src="assets/images/sites/experience/experience_15.jpg" alt="RF Deposition System" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
          </div>

          <ul class="facility-items">
            <li>DC & RF Magnetron Sputtering systems</li>
            <li>System maintenance, turbo pump & RF target repair</li>
            <li>Pulsed Laser Deposition (KrF Excimer PLD)</li>
            <li>Thermal Evaporation & DC Sputter coaters</li>
          </ul>
        </div>

        <!-- Facility 2 -->
        <div class="facility-card">
          <div class="facility-header">
            <div class="facility-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line></svg>
            </div>
            <div>
              <div class="facility-name">Magnetic Dynamics</div>
              <div class="facility-inst">UoH & TIFR Hyderabad</div>
            </div>
          </div>

          <div class="setup-photo-grid">
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/experience/experience_02.jpg" data-caption="Conventional MOKE Facility @ TIFR Hyderabad for thin film optimization">
              <img src="assets/images/sites/experience/experience_02.jpg" alt="MOKE Facility @ TIFR Hyderabad" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/experience/experience_18.jpg" data-caption="Quantum Design PPMS (Physical Property Measurement System) Cryogenic Facility">
              <img src="assets/images/sites/experience/experience_18.jpg" alt="Quantum Design PPMS" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
          </div>

          <ul class="facility-items">
            <li>Conventional MOKE (Magneto-Optical Kerr Effect) @ TIFR-H</li>
            <li>Quantum Design PPMS (Physical Property Measurement System)</li>
            <li>Broadband VNA-FMR (0.1–20 GHz)</li>
            <li>In-plane and Out-of-plane magnetic hysteresis loops</li>
          </ul>
        </div>

        <!-- Facility 3 -->
        <div class="facility-card">
          <div class="facility-header">
            <div class="facility-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
            </div>
            <div>
              <div class="facility-name">Structural & Surface Analysis</div>
              <div class="facility-inst">Central Facilities, UoH</div>
            </div>
          </div>

          <div class="setup-photo-grid">
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/experience/experience_04.jpg" data-caption="Field Emission Scanning Electron Microscope (FESEM) Facility @ UoH">
              <img src="assets/images/sites/experience/experience_04.jpg" alt="FESEM Facility" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/experience/experience_06.jpg" data-caption="Thin Film XRD & XRR (Bruker D8) Diffractometer Facility @ UoH">
              <img src="assets/images/sites/experience/experience_06.jpg" alt="XRD Facility" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
          </div>

          <ul class="facility-items">
            <li>FESEM (Field Emission Scanning Electron Microscopy)</li>
            <li>Powder & GI-XRD (Grazing Incidence X-ray Diffraction)</li>
            <li>X-ray Reflectivity (XRR) thin film thickness analysis</li>
            <li>Stylus Profilometer (Veeco/Bruker) & AFM</li>
            <li>UV/VIS/NIR Spectrophotometry</li>
          </ul>
        </div>

        <!-- Facility 4 -->
        <div class="facility-card">
          <div class="facility-header">
            <div class="facility-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="6" cy="6" r="3"></circle><circle cx="6" cy="18" r="3"></circle><line x1="20" y1="4" x2="8.12" y2="15.88"></line><line x1="14.47" y1="14.48" x2="20" y2="20"></line><line x1="8.12" y1="8.12" x2="12" y2="12"></line></svg>
            </div>
            <div>
              <div class="facility-name">Cleanroom Nanofabrication</div>
              <div class="facility-inst">CeNSE, IISc Bangalore</div>
            </div>
          </div>

          <div class="setup-photo-grid">
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/gallery/gallery_01.jpg" data-caption="Receiving fabricated MEMS cantilever chips from Ms. Ashwini A (Facility Technologist, CeNSE, IISc Bangalore)">
              <img src="assets/images/sites/gallery/gallery_01.jpg" alt="CeNSE Nanofabrication Handover" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/gallery/gallery_02.jpg" data-caption="Cleanroom device fabrication interaction with Mr. Venu V Bhat (Facility Technologist, CeNSE, IISc Bangalore)">
              <img src="assets/images/sites/gallery/gallery_02.jpg" alt="CeNSE Cleanroom Discussion" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
          </div>

          <ul class="facility-items">
            <li>INUP-i2i Certified Cleanroom Fabrication (Class 100/1000)</li>
            <li>Optical Photolithography & Mask aligner processing</li>
            <li>Wet chemical etching & Reactive Ion Etching (RIE)</li>
            <li>MEMS micro-cantilever device fabrication & release</li>
          </ul>
        </div>

        <!-- Facility 5 -->
        <div class="facility-card">
          <div class="facility-header">
            <div class="facility-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
            </div>
            <div>
              <div class="facility-name">Ion Beam Accelerator Facility</div>
              <div class="facility-inst">IUAC, New Delhi</div>
            </div>
          </div>

          <div class="card-img-wrapper" style="height: 140px; margin-bottom: 14px;" data-zoom-src="assets/images/sites/gallery/gallery_07.jpg" data-caption="Swift Heavy Ion (SHI) Irradiation Beamline Experiment at Inter-University Accelerator Centre (IUAC), New Delhi">
            <img src="assets/images/sites/gallery/gallery_07.jpg" alt="SHI Beamline at IUAC" loading="lazy">
            <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
          </div>

          <ul class="facility-items">
            <li>Swift Heavy Ion (SHI) Irradiation beamline experiments</li>
            <li>High-energy Pelletron accelerator operation</li>
            <li>Ion-beam induced atomic restructuring in magnetic films</li>
            <li>Defect dynamics in polymer-nanocomposite shielding materials</li>
          </ul>
        </div>

        <!-- Facility 6 -->
        <div class="facility-card">
          <div class="facility-header">
            <div class="facility-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg>
            </div>
            <div>
              <div class="facility-name">Profilometry & Surface Metrology</div>
              <div class="facility-inst">CASEST & CFN, UoH</div>
            </div>
          </div>

          <div class="setup-photo-grid">
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/experience/experience_13.jpg" data-caption="Stylus Profilometer System @ Centre for Nanotechnology (CFN), UoH">
              <img src="assets/images/sites/experience/experience_13.jpg" alt="Stylus Profilometer" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
            <div class="card-img-wrapper" data-zoom-src="assets/images/sites/experience/experience_16.jpg" data-caption="Atomic Force Microscopy (AFM) Facility @ University of Hyderabad">
              <img src="assets/images/sites/experience/experience_16.jpg" alt="AFM Facility" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
            </div>
          </div>

          <ul class="facility-items">
            <li>Veeco/Bruker Stylus Profilometer step-height measurement</li>
            <li>Atomic Force Microscopy (AFM) surface topography</li>
            <li>UV/VIS/NIR Spectrophotometry optical bandgap analysis</li>
            <li>Vector Network Analyzer (VNA) microwave S-parameter testing</li>
          </ul>
        </div>

      </div>'''

content = content.replace(old_facilities_block, new_facilities_block)

# 4. Update Conferences & Workshops Timeline with Photos & Complete Records
old_timeline = '''      <div class="timeline-container">
        
        <!-- Conference 1 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge poster">Poster Presentation</span>
              <span class="timeline-date">12–14 February 2025</span>
            </div>
            <h3 class="timeline-event">International Conference on Magnetic Materials and Applications (ICMAGMA 2025)</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              J. N. Tata Auditorium, Indian Institute of Science (IISc), Bangalore, India
            </div>
            <p class="timeline-topic">
              <strong>Paper:</strong> <em>"Effect of Swift Heavy Ion (SHI) Irradiation on Magnetic Properties of FeGaB Thin Film"</em> — B. Arun, Jisna Rahman, K. C. James Raju.
            </p>
          </div>
        </div>

        <!-- Training 1 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge training">Hands-On Certification</span>
              <span class="timeline-date">21–25 March 2025</span>
            </div>
            <h3 class="timeline-event">Powder and GI-XRD Advanced Instrument Training</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              School of Physics, University of Hyderabad, India
            </div>
            <p class="timeline-topic">
              Intensive operational and analysis training on high-resolution X-ray diffractometer in powder and Grazing Incidence (GI-XRD) geometries for thin film thinness and phase determination.
            </p>
          </div>
        </div>

        <!-- Training 2 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge training">Symposium Workshop</span>
              <span class="timeline-date">19–20 February 2025</span>
            </div>
            <h3 class="timeline-event">Workshop on Ion/Laser Beams in Nano-Science (WINS-2025)</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              Centre for Nanotechnology (CFN), University of Hyderabad, India
            </div>
            <p class="timeline-topic">
              Advanced discussions on ion and laser beam interactions for nanomaterial patterning, defect engineering, and spintronic materials modification.
            </p>
          </div>
        </div>

        <!-- Training 3 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge training">Research School</span>
              <span class="timeline-date">11–21 December 2024</span>
            </div>
            <h3 class="timeline-event">ASSURE Workshop on Magnetism (TIFR Hyderabad Collaboration)</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              Dept of Physics, Osmania University & TIFR Hyderabad, Telangana, India
            </div>
            <p class="timeline-topic">
              Comprehensive 10-day intensive school covering theoretical and experimental fundamentals of magnetism, exchange bias, spin pumping, and MOKE/PPMS characterization.
            </p>
          </div>
        </div>

        <!-- Conference 2 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge poster">Poster Presentation</span>
              <span class="timeline-date">27–28 September 2024</span>
            </div>
            <h3 class="timeline-event">Frontiers in Physics Conference (FIP 2024)</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              School of Physics, University of Hyderabad, India
            </div>
            <p class="timeline-topic">
              <strong>Paper:</strong> <em>"Development of VNA FMR and Precise Determination of Landé g-factor of Gallium Iron Boride Thin Films"</em> — B. Arun, K. C. James Raju.
            </p>
          </div>
        </div>

        <!-- Conference 3 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge oral">Oral Presentation</span>
              <span class="timeline-date">22–24 November 2023</span>
            </div>
            <h3 class="timeline-event">5th Asia Conference on Material and Manufacturing Technology (ACMMT 2023)</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              Chiang Mai, Thailand
            </div>
            <p class="timeline-topic">
              <strong>Paper:</strong> <em>"Room Temperature Static Magnetic Properties of Pt/FeGaB/Pt Tri-Layer"</em> — B. Arun, Andrews Joseph, K. C. James Raju.
            </p>
          </div>
        </div>

        <!-- Conference 4 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge oral">Oral Presentation</span>
              <span class="timeline-date">11–13 October 2023</span>
            </div>
            <h3 class="timeline-event">Intl. Conference on Advances in Condensed Matter Physics (ICACMP 2023)</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              GITAM School of Science, Hyderabad, India
            </div>
            <p class="timeline-topic">
              <strong>Paper:</strong> <em>"Ferromagnetic Resonance Characterization of FeGaB Thin Films Using Vector Network Analyzer"</em> — B. Arun, K. C. James Raju.
            </p>
          </div>
        </div>

        <!-- Training 4 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge training">Cleanroom Hands-On Training</span>
              <span class="timeline-date">14–24 February 2023</span>
            </div>
            <h3 class="timeline-event">INUP-i2i Hands-On Nanofabrication & Characterization</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              Centre for Nano Science and Engineering (CeNSE), IISc Bangalore, India
            </div>
            <p class="timeline-topic">
              Hands-on cleanroom fabrication of MEMS micro-cantilevers using photolithography, wet/dry etching, and laser vibrometer characterization under the Indian Nanoelectronics Users Programme.
            </p>
          </div>
        </div>

      </div>'''

new_timeline = '''      <div class="timeline-container">
        
        <!-- Conference 1 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge poster">Poster Presentation</span>
              <span class="timeline-date">12–14 February 2025</span>
            </div>
            <h3 class="timeline-event">International Conference on Magnetic Materials and Applications (ICMAGMA 2025)</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              J. N. Tata Auditorium, Indian Institute of Science (IISc), Bangalore, India
            </div>
            <div class="card-img-wrapper" style="height: 180px; margin: 12px 0;" data-zoom-src="assets/images/sites/conferences/conferences_01.jpg" data-caption="ICMAGMA 2025 Conference Presentation @ J.N. Tata Auditorium, IISc Bangalore">
              <img src="assets/images/sites/conferences/conferences_01.jpg" alt="ICMAGMA 2025" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge photo">🔍</button>
            </div>
            <p class="timeline-topic">
              <strong>Paper:</strong> <em>"Effect of Swift Heavy Ion (SHI) Irradiation on Magnetic Properties of FeGaB Thin Film"</em> — B. Arun, Jisna Rahman, K. C. James Raju.
            </p>
          </div>
        </div>

        <!-- Training 1 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge training">Hands-On Certification</span>
              <span class="timeline-date">21–25 March 2025</span>
            </div>
            <h3 class="timeline-event">Powder and GI-XRD Advanced Instrument Training</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              School of Physics, University of Hyderabad, India
            </div>
            <div class="card-img-wrapper" style="height: 180px; margin: 12px 0;" data-zoom-src="assets/images/sites/workshops/workshops_01.jpg" data-caption="Powder and GI-XRD Advanced Training Certificate @ School of Physics, UoH">
              <img src="assets/images/sites/workshops/workshops_01.jpg" alt="GI-XRD Certificate" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge photo">🔍</button>
            </div>
            <p class="timeline-topic">
              Intensive operational and analysis training on high-resolution X-ray diffractometer in powder and Grazing Incidence (GI-XRD) geometries for thin film thickness and phase determination.
            </p>
          </div>
        </div>

        <!-- Training 2 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge training">Symposium Workshop</span>
              <span class="timeline-date">19–20 February 2025</span>
            </div>
            <h3 class="timeline-event">Workshop on Ion/Laser Beams in Nano-Science (WINS-2025)</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              Centre for Nanotechnology (CFN), University of Hyderabad, India
            </div>
            <div class="card-img-wrapper" style="height: 180px; margin: 12px 0;" data-zoom-src="assets/images/sites/workshops/workshops_02.jpg" data-caption="Workshop on Ion/Laser Beams in Nano-Science (WINS-2025) @ CFN, UoH">
              <img src="assets/images/sites/workshops/workshops_02.jpg" alt="WINS-2025 Workshop" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge photo">🔍</button>
            </div>
            <p class="timeline-topic">
              Advanced discussions on ion and laser beam interactions for nanomaterial patterning, defect engineering, and spintronic materials modification.
            </p>
          </div>
        </div>

        <!-- Training 3 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge training">Research School</span>
              <span class="timeline-date">11–21 December 2024</span>
            </div>
            <h3 class="timeline-event">ASSURE Workshop on Magnetism (TIFR Hyderabad Collaboration)</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              Dept of Physics, Osmania University & TIFR Hyderabad, Telangana, India
            </div>
            <div class="card-img-wrapper" style="height: 180px; margin: 12px 0;" data-zoom-src="assets/images/sites/workshops/workshops_03.jpg" data-caption="ASSURE Workshop on Magnetism in collaboration with TIFR Hyderabad">
              <img src="assets/images/sites/workshops/workshops_03.jpg" alt="ASSURE Magnetism School" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge photo">🔍</button>
            </div>
            <p class="timeline-topic">
              Comprehensive 10-day intensive school covering theoretical and experimental fundamentals of magnetism, exchange bias, spin pumping, and MOKE/PPMS characterization.
            </p>
          </div>
        </div>

        <!-- Conference 2 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge poster">Poster Presentation</span>
              <span class="timeline-date">27–28 September 2024</span>
            </div>
            <h3 class="timeline-event">Frontiers in Physics Conference (FIP 2024)</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              School of Physics, University of Hyderabad, India
            </div>
            <div class="card-img-wrapper" style="height: 180px; margin: 12px 0;" data-zoom-src="assets/images/sites/conferences/conferences_02.jpg" data-caption="Frontiers in Physics (FIP 2024) Poster Presentation @ School of Physics, UoH">
              <img src="assets/images/sites/conferences/conferences_02.jpg" alt="FIP 2024" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge photo">🔍</button>
            </div>
            <p class="timeline-topic">
              <strong>Paper:</strong> <em>"Development of VNA FMR and Precise Determination of Landé g-factor of Gallium Iron Boride Thin Films"</em> — B. Arun, K. C. James Raju.
            </p>
          </div>
        </div>

        <!-- Conference 3 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge oral">Oral Presentation</span>
              <span class="timeline-date">22–24 November 2023</span>
            </div>
            <h3 class="timeline-event">5th Asia Conference on Material and Manufacturing Technology (ACMMT 2023)</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              Chiang Mai, Thailand
            </div>
            <div class="card-img-wrapper" style="height: 180px; margin: 12px 0;" data-zoom-src="assets/images/sites/conferences/conferences_05.jpg" data-caption="5th Asia Conference on Material and Manufacturing Technology (ACMMT 2023), Chiang Mai, Thailand">
              <img src="assets/images/sites/conferences/conferences_05.jpg" alt="ACMMT 2023 Thailand" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge photo">🔍</button>
            </div>
            <p class="timeline-topic">
              <strong>Paper:</strong> <em>"Room Temperature Static Magnetic Properties of Pt/FeGaB/Pt Tri-Layer"</em> — B. Arun, Andrews Joseph, K. C. James Raju.
            </p>
          </div>
        </div>

        <!-- Conference 4 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge oral">Oral Presentation</span>
              <span class="timeline-date">11–13 October 2023</span>
            </div>
            <h3 class="timeline-event">Intl. Conference on Advances in Condensed Matter Physics (ICACMP 2023)</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              GITAM School of Science, Hyderabad, India
            </div>
            <div class="card-img-wrapper" style="height: 180px; margin: 12px 0;" data-zoom-src="assets/images/sites/conferences/conferences_06.jpg" data-caption="ICACMP 2023 Presentation @ GITAM Hyderabad">
              <img src="assets/images/sites/conferences/conferences_06.jpg" alt="ICACMP 2023" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge photo">🔍</button>
            </div>
            <p class="timeline-topic">
              <strong>Paper:</strong> <em>"Ferromagnetic Resonance Characterization of FeGaB Thin Films Using Vector Network Analyzer"</em> — B. Arun, K. C. James Raju.
            </p>
          </div>
        </div>

        <!-- Conference 5 (ICMAGMA 2023) -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge poster">Poster Presentation</span>
              <span class="timeline-date">4–6 December 2023</span>
            </div>
            <h3 class="timeline-event">International Conference on Magnetic Materials and Applications (ICMAGMA 2023)</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              Hyderabad, Telangana, India
            </div>
            <div class="card-img-wrapper" style="height: 180px; margin: 12px 0;" data-zoom-src="assets/images/sites/conferences/conferences_04.jpg" data-caption="ICMAGMA 2023 Presentation & Proceedings at Hyderabad">
              <img src="assets/images/sites/conferences/conferences_04.jpg" alt="ICMAGMA 2023" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge photo">🔍</button>
            </div>
            <p class="timeline-topic">
              High-frequency dynamic magnetic analysis and microwave Gilbert damping in engineered magnetostrictive thin film alloys.
            </p>
          </div>
        </div>

        <!-- Training 4 -->
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-content">
            <div class="timeline-header">
              <span class="timeline-badge training">Cleanroom Hands-On Training</span>
              <span class="timeline-date">14–24 February 2023</span>
            </div>
            <h3 class="timeline-event">INUP-i2i Hands-On Nanofabrication & Characterization</h3>
            <div class="timeline-location">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              Centre for Nano Science and Engineering (CeNSE), IISc Bangalore, India
            </div>
            <div class="card-img-wrapper" style="height: 180px; margin: 12px 0;" data-zoom-src="assets/images/sites/workshops/workshops_07.jpg" data-caption="INUP-i2i Cleanroom Nanofabrication Certificate @ CeNSE, IISc Bangalore">
              <img src="assets/images/sites/workshops/workshops_07.jpg" alt="INUP-i2i Cleanroom Certificate" loading="lazy">
              <button class="img-zoom-btn" aria-label="Enlarge photo">🔍</button>
            </div>
            <p class="timeline-topic">
              Hands-on cleanroom fabrication of MEMS micro-cantilevers using photolithography, wet/dry etching, and laser vibrometer characterization under the Indian Nanoelectronics Users Programme.
            </p>
          </div>
        </div>

      </div>'''

content = content.replace(old_timeline, new_timeline)

# 5. Build Dedicated Gallery Section (#gallery)
manifest = [
  # Setups
  {'cat': 'setups', 'tag': 'In-House Hardware', 'file': 'assets/images/sites/experimental_setups/experimental_setups_01.jpg', 'title': 'Magnetoelectric Voltage Facility', 'desc': 'Dynamic magnetoelectric voltage coefficient measurement bench with lock-in detection and AC/DC bias.'},
  {'cat': 'setups', 'tag': 'Probe Stage Hardware', 'file': 'assets/images/sites/experimental_setups/experimental_setups_02.jpg', 'title': 'Miniature Electromagnet (800 Oe)', 'desc': 'Compact 800 Oe @ 1A electromagnet custom engineered for RF microwave wafer probe stations.'},
  {'cat': 'setups', 'tag': 'Optoelectronic Hardware', 'file': 'assets/images/sites/experimental_setups/experimental_setups_03.jpg', 'title': 'Precision Optical Chopper', 'desc': 'Arduino Uno & BLDC-driven high-speed optical chopper generating light modulation pulses up to 2.8 kHz.'},
  {'cat': 'setups', 'tag': 'Schematics & Wiring', 'file': 'assets/images/sites/experimental_setups/experimental_setups_04.jpg', 'title': 'Optical Chopper Wiring Diagram', 'desc': 'Detailed electrical circuit schematic interfacing potentiometer, ESC, Arduino Uno, and brushless motor.'},
  {'cat': 'setups', 'tag': 'Spin Dynamics', 'file': 'assets/images/sites/gallery/gallery_04.jpg', 'title': 'VNA-FMR Experimental Bench', 'desc': 'Broadband Vector Network Analyzer Ferromagnetic Resonance system with coplanar waveguide and electromagnet.'},
  {'cat': 'setups', 'tag': 'Standardization', 'file': 'assets/images/sites/gallery/gallery_05.jpg', 'title': 'VNA-FMR Standardization on Thin Films', 'desc': 'Rigorous microwave S-parameter calibration and Gilbert damping factor extraction on FeGaB alloy films.'},

  # Facilities - Experience
  {'cat': 'facilities', 'tag': 'MOKE @ TIFR-H', 'file': 'assets/images/sites/experience/experience_01.jpg', 'title': 'Conventional MOKE System @ TIFR-H', 'desc': 'Magneto-Optical Kerr Effect optical table and magnet poles used for FeGaB magnetic domain and hysteresis studies.'},
  {'cat': 'facilities', 'tag': 'MOKE @ TIFR-H', 'file': 'assets/images/sites/experience/experience_02.jpg', 'title': 'MOKE Sample Stage Alignment', 'desc': 'Precision goniometer sample holder and laser alignment setup for in-plane longitudinal MOKE loops.'},
  {'cat': 'facilities', 'tag': 'FESEM @ UoH', 'file': 'assets/images/sites/experience/experience_03.jpg', 'title': 'Field Emission SEM Facility', 'desc': 'High-resolution field emission scanning electron microscope at UoH for microstructural surface imaging.'},
  {'cat': 'facilities', 'tag': 'FESEM @ UoH', 'file': 'assets/images/sites/experience/experience_04.jpg', 'title': 'FESEM Control & Acquisition Console', 'desc': 'Electron beam column control console and energy-dispersive X-ray spectroscopy (EDS) terminal.'},
  {'cat': 'facilities', 'tag': 'XRD @ UoH', 'file': 'assets/images/sites/experience/experience_05.jpg', 'title': 'Thin Film XRD & XRR (Bruker D8)', 'desc': 'Bruker D8 Advance diffractometer goniometer configured for thin film phase and reflectivity analysis.'},
  {'cat': 'facilities', 'tag': 'XRD @ UoH', 'file': 'assets/images/sites/experience/experience_06.jpg', 'title': 'High-Resolution XRD Gonio-Stage', 'desc': 'Grazing incidence XRD stage with scintillation detector for structural characterization of nano-coatings.'},
  {'cat': 'facilities', 'tag': 'Spectroscopy @ UoH', 'file': 'assets/images/sites/experience/experience_07.jpg', 'title': 'UV/VIS/NIR Spectrophotometer', 'desc': 'Optical transmission and absorption spectroscopy system for thin films and dielectric composites.'},
  {'cat': 'facilities', 'tag': 'Spectroscopy @ UoH', 'file': 'assets/images/sites/experience/experience_08.jpg', 'title': 'UV/VIS Spectrometer Sample Chamber', 'desc': 'Cuvette and solid-state thin film sample fixture inside the dual-beam spectrophotometer optical compartment.'},
  {'cat': 'facilities', 'tag': 'Deposition @ UoH', 'file': 'assets/images/sites/experience/experience_09.jpg', 'title': 'Thermal & Sputter Coater Facility', 'desc': 'High-vacuum deposition system for conductive contact layer deposition and SEM conductive pre-coating.'},
  {'cat': 'facilities', 'tag': 'Sputtering @ CASEST', 'file': 'assets/images/sites/experience/experience_10.jpg', 'title': 'DC/RF Magnetron Sputtering System', 'desc': 'Multi-target high-vacuum sputtering system at CASEST for ferromagnetic FeGaB and multiferroic thin films.'},
  {'cat': 'facilities', 'tag': 'Sputtering @ CASEST', 'file': 'assets/images/sites/experience/experience_11.jpg', 'title': 'Sputtering Power Rack & Gas Mass Flow', 'desc': 'RF matching networks, DC power supplies, and Ar/O2 mass flow controller (MFC) console at CASEST.'},
  {'cat': 'facilities', 'tag': 'Profilometry @ CFN', 'file': 'assets/images/sites/experience/experience_12.jpg', 'title': 'Stylus Profilometer System @ CFN', 'desc': 'Veeco/Bruker high-resolution stylus profilometer at Centre for Nanotechnology for step-height profiling.'},
  {'cat': 'facilities', 'tag': 'Profilometry @ CFN', 'file': 'assets/images/sites/experience/experience_13.jpg', 'title': 'Stylus Profilometer Stage & Camera', 'desc': 'Sub-nanometer diamond stylus scanning mechanism and sample observation microscope stage.'},
  {'cat': 'facilities', 'tag': 'System Maintenance', 'file': 'assets/images/sites/experience/experience_14.jpg', 'title': 'Sputtering Turbo Pump & Line Repair', 'desc': 'Hands-on troubleshooting, vacuum flange seal overhaul, and turbomolecular pump maintenance.'},
  {'cat': 'facilities', 'tag': 'Deposition @ CFN', 'file': 'assets/images/sites/experience/experience_15.jpg', 'title': 'RF Deposition Facility @ CFN', 'desc': 'Dedicated radio-frequency sputtering deposition chamber for dielectric and functional thin film coatings.'},
  {'cat': 'facilities', 'tag': 'AFM @ UoH', 'file': 'assets/images/sites/experience/experience_16.jpg', 'title': 'Atomic Force Microscope (AFM) Head', 'desc': 'Cantilever optical lever detection head and scanner module for surface nanoscale topography.'},
  {'cat': 'facilities', 'tag': 'AFM @ UoH', 'file': 'assets/images/sites/experience/experience_17.jpg', 'title': 'AFM Vibration Isolation Platform', 'desc': 'Acoustic isolation enclosure and active vibration damping system ensuring atomic-scale resolution.'},
  {'cat': 'facilities', 'tag': 'Cryogenics @ UoH', 'file': 'assets/images/sites/experience/experience_18.jpg', 'title': 'Quantum Design PPMS Facility', 'desc': 'Physical Property Measurement System with EverCool cryostat for temperature-dependent magnetometry.'},

  # Cleanroom & Accelerator
  {'cat': 'fieldwork', 'tag': 'CeNSE Cleanroom', 'file': 'assets/images/sites/gallery/gallery_01.jpg', 'title': 'MEMS Cantilever Handover at CeNSE', 'desc': 'Receiving fabricated micro-cantilever chips from Ms. Ashwini A (Facility Technologist, CeNSE, IISc Bangalore).'},
  {'cat': 'fieldwork', 'tag': 'CeNSE Cleanroom', 'file': 'assets/images/sites/gallery/gallery_02.jpg', 'title': 'Nanofabrication Technical Review', 'desc': 'Technical interaction and process parameter review with Mr. Venu V Bhat (Facility Technologist, CeNSE).'},
  {'cat': 'fieldwork', 'tag': 'CeNSE Cleanroom', 'file': 'assets/images/sites/gallery/gallery_03.jpg', 'title': 'INUP-i2i Participant Cohort @ IISc', 'desc': 'Hands-on cleanroom training batch at the Centre for Nano Science and Engineering, IISc Bangalore.'},
  {'cat': 'fieldwork', 'tag': 'IUAC Delhi', 'file': 'assets/images/sites/gallery/gallery_07.jpg', 'title': 'Swift Heavy Ion Beamline @ IUAC', 'desc': 'Pelletron accelerator beamline hall at Inter-University Accelerator Centre, New Delhi during FeGaB SHI irradiation.'},

  # Conferences
  {'cat': 'conferences', 'tag': 'ICMAGMA 2025', 'file': 'assets/images/sites/conferences/conferences_01.jpg', 'title': 'ICMAGMA 2025 @ IISc Bangalore', 'desc': 'Presentation on Swift Heavy Ion (SHI) irradiation effects on FeGaB films at J.N. Tata Auditorium, IISc.'},
  {'cat': 'conferences', 'tag': 'FIP 2024', 'file': 'assets/images/sites/conferences/conferences_02.jpg', 'title': 'Frontiers in Physics (FIP 2024)', 'desc': 'Poster presentation on VNA-FMR Landé g-factor determination in FeGaB thin films at University of Hyderabad.'},
  {'cat': 'conferences', 'tag': 'NANOscientific 2023', 'file': 'assets/images/sites/conferences/conferences_03.jpg', 'title': '2023 NANOscientific Symposium Asia', 'desc': 'Certificate and technical presentation on nanoscale scanning probe characterization methodologies.'},
  {'cat': 'conferences', 'tag': 'ICMAGMA 2023', 'file': 'assets/images/sites/conferences/conferences_04.jpg', 'title': 'ICMAGMA 2023 @ Hyderabad', 'desc': 'International Conference on Magnetic Materials and Applications delegate sessions in Hyderabad.'},
  {'cat': 'conferences', 'tag': 'ICMAGMA 2023', 'file': 'assets/images/sites/gallery/gallery_06.jpg', 'title': 'ICMAGMA 2023 Poster Presentation', 'desc': 'Disseminating thin film ferromagnetic resonance and anisotropy findings to magnetic materials peers.'},
  {'cat': 'conferences', 'tag': 'ACMMT 2023', 'file': 'assets/images/sites/conferences/conferences_05.jpg', 'title': 'ACMMT 2023 @ Chiang Mai, Thailand', 'desc': 'Oral talk on room temperature static magnetic properties of Pt/FeGaB/Pt trilayers at ACMMT 2023.'},
  {'cat': 'conferences', 'tag': 'ICACMP 2023', 'file': 'assets/images/sites/conferences/conferences_06.jpg', 'title': 'ICACMP 2023 @ GITAM Hyderabad', 'desc': 'Oral presentation on Vector Network Analyzer FMR characterization of soft FeGaB thin films.'},
  {'cat': 'conferences', 'tag': 'FIP 2023', 'file': 'assets/images/sites/conferences/conferences_07.jpg', 'title': 'Frontiers in Physics (FIP 2023)', 'desc': 'Poster session at School of Physics, University of Hyderabad on microwave magnetic materials.'},
  {'cat': 'conferences', 'tag': 'ICRAMM 2019', 'file': 'assets/images/sites/conferences/conferences_08.jpg', 'title': 'ICRAMM 2019 Conference', 'desc': 'Presentation at International Conference on Recent Advances in Materials and Manufacturing.'},

  # Workshops
  {'cat': 'workshops', 'tag': 'GI-XRD 2025', 'file': 'assets/images/sites/workshops/workshops_01.jpg', 'title': 'Powder & GI-XRD Advanced Certification', 'desc': 'School of Physics, UoH intensive certification in grazing incidence X-ray diffraction analysis.'},
  {'cat': 'workshops', 'tag': 'WINS-2025', 'file': 'assets/images/sites/workshops/workshops_02.jpg', 'title': 'Ion/Laser Beams in Nano-Science', 'desc': 'CFN, UoH workshop on ion and laser beam nanostructuring and materials modification.'},
  {'cat': 'workshops', 'tag': 'ASSURE 2024', 'file': 'assets/images/sites/workshops/workshops_03.jpg', 'title': 'ASSURE Workshop on Magnetism', 'desc': '10-day intensive school organized with TIFR Hyderabad at Osmania University on advanced magnetism.'},
  {'cat': 'workshops', 'tag': 'Rietveld 2024', 'file': 'assets/images/sites/workshops/workshops_04.jpg', 'title': 'Rietveld Refinement Workshop', 'desc': 'Advanced training on crystallographic structural refinement from powder XRD data.'},
  {'cat': 'workshops', 'tag': 'Python 2024', 'file': 'assets/images/sites/workshops/workshops_05.jpg', 'title': 'Python for Data Analysis Workshop', 'desc': 'Hands-on scientific computation, automated curve-fitting, and data analytics certification.'},
  {'cat': 'workshops', 'tag': 'Pondicherry 2023', 'file': 'assets/images/sites/workshops/workshops_06.jpg', 'title': 'Magnetism & Measurements Workshop', 'desc': 'Pondicherry University symposium on magnetic characterization instrumentation and techniques.'},
  {'cat': 'workshops', 'tag': 'CeNSE IISc 2023', 'file': 'assets/images/sites/workshops/workshops_07.jpg', 'title': 'INUP-i2i Hands-On Nanofabrication', 'desc': 'CeNSE, IISc Bangalore cleanroom certificate for micro-cantilever photolithography and dry etching.'},
  {'cat': 'workshops', 'tag': 'IIT Bombay 2023', 'file': 'assets/images/sites/workshops/workshops_08.jpg', 'title': 'INUP-i2i Nanofabrication Technologies', 'desc': 'Familiarization workshop certification covering state-of-the-art semiconductor device fabrication.'},

  # Home
  {'cat': 'fieldwork', 'tag': 'Academic Profile', 'file': 'assets/images/sites/home/home_02.jpg', 'title': 'Senior Research Scholar Arun B', 'desc': 'Centre for Advanced Studies in Electronics Science and Technology (CASEST), University of Hyderabad.'},
  {'cat': 'fieldwork', 'tag': 'Lab Branding', 'file': 'assets/images/sites/home/home_01.jpg', 'title': 'Research Lab Banner & Seal', 'desc': 'Official header identity from Arun B applied physics research portfolio.'}
]

gallery_cards_html = []
for item in manifest:
    card = f'''        <div class="gallery-card" data-category="{item['cat']}">
          <div class="gallery-card-img-box">
            <img src="{item['file']}" alt="{item['title']}" loading="lazy" data-zoom-src="{item['file']}" data-caption="{item['title']} • {item['desc']}">
            <span class="gallery-badge-overlay">{item['tag']}</span>
            <button class="img-zoom-btn" aria-label="Enlarge image" data-zoom-src="{item['file']}" data-caption="{item['title']} • {item['desc']}">🔍</button>
          </div>
          <div class="gallery-card-body">
            <h3 class="gallery-card-title">{item['title']}</h3>
            <p class="gallery-card-desc">{item['desc']}</p>
            <div class="gallery-card-meta">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="10" r="3"></circle><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path></svg>
              <span>Original Google Site Mirror Asset</span>
            </div>
          </div>
        </div>'''
    gallery_cards_html.append(card)

gallery_section_html = f'''  <!-- ==========================================================================
       RESEARCH & EXPERIMENTAL GALLERY (ALL 47 MIRRORED IMAGES)
       ========================================================================== -->
  <section id="gallery" class="section section-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-badge">Visual Portfolio & Evidence</span>
        <h2 class="section-title">Research & Experimental Gallery</h2>
        <p class="section-subtitle">
          Complete high-resolution photo chronicle of in-house scientific instrumentation, premier laboratory facilities, 
          international conference presentations, and certified nanofabrication workshops.
        </p>
      </div>

      <!-- Local Mirror Callout Banner -->
      <div style="background: var(--bg-card); border: 1px solid var(--border-light); border-left: 4px solid var(--accent-cyan); padding: 18px 24px; border-radius: var(--radius-md); margin-bottom: 32px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; box-shadow: var(--shadow-sm);">
        <div>
          <div style="font-weight: 700; color: var(--text-primary); font-size: 1rem; display: flex; align-items: center; gap: 8px;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent-cyan);"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
            Complete Local Offline Mirror of Published Google Site
          </div>
          <p style="color: var(--text-secondary); font-size: 0.875rem; margin-top: 4px;">
            Browse the exact offline replica of the published website (sites.google.com/view/arunb) including Home, Publications, Conferences, Workshops, Experimental Setups, Experience, and Gallery.
          </p>
        </div>
        <a href="site_mirror/home.html" target="_blank" class="btn btn-secondary" style="font-size: 0.8125rem; padding: 10px 18px; border-color: var(--accent-cyan); color: var(--accent-cyan); font-weight: 700;">
          Explore Local Mirror (7 Pages) &rarr;
        </a>
      </div>

      <!-- Gallery Filter Tabs -->
      <div class="gallery-filter-tabs">
        <button class="gallery-tab-btn active" data-category="all">All Photos (47)</button>
        <button class="gallery-tab-btn" data-category="setups">In-House Setups (6)</button>
        <button class="gallery-tab-btn" data-category="facilities">Laboratory Facilities (18)</button>
        <button class="gallery-tab-btn" data-category="conferences">Conferences (9)</button>
        <button class="gallery-tab-btn" data-category="workshops">Workshops & Certifications (8)</button>
        <button class="gallery-tab-btn" data-category="fieldwork">Cleanroom & Accelerator (6)</button>
      </div>

      <!-- Gallery Photo Grid -->
      <div class="gallery-grid">
{chr(10).join(gallery_cards_html)}
      </div>

    </div>
  </section>
'''

# Insert Gallery right after </section> of conferences
target_after_conf = '</section>\n\n  <!-- ==========================================================================\n       OPEN SOURCE SCIENTIFIC SOFTWARE & GITHUB'
if target_after_conf in content:
    content = content.replace(target_after_conf, f'</section>\n\n{gallery_section_html}\n  <!-- ==========================================================================\n       OPEN SOURCE SCIENTIFIC SOFTWARE & GITHUB')
else:
    # fallback
    conf_end = '<!-- OPEN SOURCE SCIENTIFIC SOFTWARE & GITHUB -->'
    print("Warning: exact string not matched, checking alternate split")

# 6. Add Lightbox Modal markup before </body>
lightbox_modal_html = '''  <!-- ==========================================================================
       IMAGE LIGHTBOX MODAL
       ========================================================================== -->
  <div id="lightbox-modal" class="lightbox-modal" role="dialog" aria-modal="true">
    <button id="lightbox-close-btn" class="lightbox-close-btn" aria-label="Close image">&times;</button>
    <div class="lightbox-img-wrapper">
      <img id="lightbox-img" class="lightbox-img" src="" alt="Enlarged research image">
    </div>
    <div id="lightbox-caption" class="lightbox-caption"></div>
  </div>
'''

if 'id="lightbox-modal"' not in content:
    content = content.replace('</body>', f'{lightbox_modal_html}\n</body>')

# 7. Update Footer with Gallery and Mirror Links
old_footer_links = '''            <li><a href="#about">About & Background</a></li>
            <li><a href="#research">Research Thrusts</a></li>
            <li><a href="#publications">Publications (22 Articles)</a></li>
            <li><a href="#setups">In-house Setups</a></li>
            <li><a href="#facilities">Laboratory Facilities</a></li>
            <li><a href="#conferences">Conferences & Trainings</a></li>
            <li><a href="#tools">Open Source Code</a></li>'''

new_footer_links = '''            <li><a href="#about">About & Background</a></li>
            <li><a href="#research">Research Thrusts</a></li>
            <li><a href="#publications">Publications (22 Articles)</a></li>
            <li><a href="#setups">In-house Setups</a></li>
            <li><a href="#facilities">Laboratory Facilities</a></li>
            <li><a href="#conferences">Conferences & Trainings</a></li>
            <li><a href="#gallery">Research Gallery (47 Photos)</a></li>
            <li><a href="site_mirror/home.html" target="_blank" style="color: var(--accent-cyan); font-weight: 600;">🌐 Original Google Site Mirror</a></li>
            <li><a href="#tools">Open Source Code</a></li>'''

content = content.replace(old_footer_links, new_footer_links)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated index.html with all 47 images, gallery, and local mirror integration!")

