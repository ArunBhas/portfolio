import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update In-House Setups (#setups) with carousels & compact images
new_setups_grid = '''      <div class="setups-grid">
        
        <!-- Setup 1 -->
        <div class="setup-card">
          <span class="setup-badge">High Frequency Magnetics</span>
          <h3 class="setup-title">VNA-FMR Broadband Ferromagnetic Resonance</h3>
          
          <!-- Related Photos Mini-Carousel -->
          <div class="mini-carousel" data-carousel>
            <div class="carousel-track">
              <div class="carousel-slide active" data-zoom-src="assets/images/sites/gallery/gallery_04.jpg" data-caption="VNA-FMR experimental bench setup and coplanar waveguide sample stage at University of Hyderabad">
                <img src="assets/images/sites/gallery/gallery_04.jpg" alt="VNA-FMR Setup" loading="lazy">
                <span class="carousel-slide-badge">1/2 • In-House CPW Bench</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/gallery/gallery_05.jpg" data-caption="Standardization of VNA-FMR measurements and microwave damping factor calibration on FeGaB thin films">
                <img src="assets/images/sites/gallery/gallery_05.jpg" alt="VNA-FMR Standardization" loading="lazy">
                <span class="carousel-slide-badge">2/2 • Calibration & Standardization</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
            </div>
            <button class="carousel-btn prev" aria-label="Previous image">&#10094;</button>
            <button class="carousel-btn next" aria-label="Next image">&#10095;</button>
            <div class="carousel-dots"></div>
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
          <p style="font-size: 0.8125rem; color: var(--text-muted); margin-top: auto;">
            Standardized for research papers published in <em>Journal of Physics D</em> and <em>Journal of Applied Physics</em>.
          </p>
        </div>

        <!-- Setup 2 -->
        <div class="setup-card">
          <span class="setup-badge">Multiferroics</span>
          <h3 class="setup-title">Magnetoelectric Dynamic Voltage Facility</h3>
          
          <div class="card-img-wrapper" style="height: 135px; margin-bottom: 12px;" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_01.jpg" data-caption="Magnetoelectric Voltage Measurement Facility: dynamic ME coefficient testing bench">
            <img src="assets/images/sites/experimental_setups/experimental_setups_01.jpg" alt="Magnetoelectric Voltage Facility" loading="lazy">
            <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
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
          <p style="font-size: 0.8125rem; color: var(--text-muted); margin-top: auto;">
            Automated in LabVIEW for rapid field-sweep curves and resonance peak tracking.
          </p>
        </div>

        <!-- Setup 3 -->
        <div class="setup-card">
          <span class="setup-badge">Micro-Magnetics Hardware</span>
          <h3 class="setup-title">Miniature Electromagnet for Microwave Probe Stations</h3>
          
          <div class="card-img-wrapper" style="height: 135px; margin-bottom: 12px;" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_02.jpg" data-caption="Miniature Electromagnet (800 Oe @ 1A) engineered for high frequency RF probe stations">
            <img src="assets/images/sites/experimental_setups/experimental_setups_02.jpg" alt="Miniature Electromagnet" loading="lazy">
            <button class="img-zoom-btn" aria-label="Enlarge image">🔍</button>
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
              <span class="spec-val">Ultra-compact Footprint</span>
            </div>
            <div class="spec-item">
              <span class="spec-key">Core Material</span>
              <span class="spec-val">High-permeability Soft Iron</span>
            </div>
          </div>
          <p style="font-size: 0.8125rem; color: var(--text-muted); margin-top: auto;">
            Enables high-frequency device characterization directly under controllable bias fields.
          </p>
        </div>

        <!-- Setup 4 -->
        <div class="setup-card">
          <span class="setup-badge">Open Science Hardware</span>
          <h3 class="setup-title">Low-Cost Arduino Precision Optical Chopper</h3>
          
          <!-- Related Photos Mini-Carousel -->
          <div class="mini-carousel" data-carousel>
            <div class="carousel-track">
              <div class="carousel-slide active" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_03.jpg" data-caption="Low-cost precision optical chopper assembly with 3D-printed slotted wheel and BLDC motor">
                <img src="assets/images/sites/experimental_setups/experimental_setups_03.jpg" alt="Precision Optical Chopper" loading="lazy">
                <span class="carousel-slide-badge">1/2 • Hardware Prototype</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/experimental_setups/experimental_setups_04.jpg" data-caption="Optical chopper electrical connection and microcontroller circuit wiring diagram (Arduino Uno + ESC + Motor)">
                <img src="assets/images/sites/experimental_setups/experimental_setups_04.jpg" alt="Chopper Wiring Diagram" loading="lazy">
                <span class="carousel-slide-badge">2/2 • Electronic Schematic</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
            </div>
            <button class="carousel-btn prev" aria-label="Previous image">&#10094;</button>
            <button class="carousel-btn next" aria-label="Next image">&#10095;</button>
            <div class="carousel-dots"></div>
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

# Replace setups grid
content = re.sub(r'<div class="setups-grid">[\s\S]*?<\/div>\s*<\/div>\s*<\/section>', new_setups_grid + '\n    </div>\n  </section>', content, count=1)

# 2. Update Facilities Section (#facilities) with mini-carousels
new_facilities_grid = '''      <div class="facilities-grid">
        
        <!-- Facility 1: Thin Film Synthesis -->
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

          <!-- Carousel of 4 Related Synthesis Photos -->
          <div class="mini-carousel" data-carousel>
            <div class="carousel-track">
              <div class="carousel-slide active" data-zoom-src="assets/images/sites/experience/experience_10.jpg" data-caption="DC/RF Sputtering Deposition Chamber @ CASEST, University of Hyderabad">
                <img src="assets/images/sites/experience/experience_10.jpg" alt="DC/RF Sputtering Chamber" loading="lazy">
                <span class="carousel-slide-badge">1/4 • Sputtering Chamber</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/experience/experience_11.jpg" data-caption="RF Power Supplies, Matching Networks & Mass Flow Controllers @ CASEST, UoH">
                <img src="assets/images/sites/experience/experience_11.jpg" alt="Power Rack" loading="lazy">
                <span class="carousel-slide-badge">2/4 • Power Rack & MFC</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/experience/experience_15.jpg" data-caption="RF Thin Film Deposition System @ Centre for Nanotechnology (CFN), UoH">
                <img src="assets/images/sites/experience/experience_15.jpg" alt="RF Deposition @ CFN" loading="lazy">
                <span class="carousel-slide-badge">3/4 • Deposition @ CFN</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/experience/experience_14.jpg" data-caption="Sputtering system maintenance, vacuum line repair & turbomolecular pump overhaul">
                <img src="assets/images/sites/experience/experience_14.jpg" alt="System Maintenance" loading="lazy">
                <span class="carousel-slide-badge">4/4 • Pump & Vacuum Overhaul</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
            </div>
            <button class="carousel-btn prev" aria-label="Previous image">&#10094;</button>
            <button class="carousel-btn next" aria-label="Next image">&#10095;</button>
            <div class="carousel-dots"></div>
          </div>

          <ul class="facility-items">
            <li>DC & RF Magnetron Sputtering systems</li>
            <li>System maintenance, turbo pump & RF target repair</li>
            <li>Pulsed Laser Deposition (KrF Excimer PLD)</li>
            <li>Thermal Evaporation & DC Sputter coaters</li>
          </ul>
        </div>

        <!-- Facility 2: Magnetic Dynamics -->
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

          <!-- Carousel of 3 Related Magnetometry Photos -->
          <div class="mini-carousel" data-carousel>
            <div class="carousel-track">
              <div class="carousel-slide active" data-zoom-src="assets/images/sites/experience/experience_02.jpg" data-caption="Conventional MOKE Facility @ TIFR Hyderabad for magnetic thin film optimization">
                <img src="assets/images/sites/experience/experience_02.jpg" alt="MOKE Facility" loading="lazy">
                <span class="carousel-slide-badge">1/3 • MOKE Sample Stage</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/experience/experience_01.jpg" data-caption="Conventional MOKE optical table & electromagnet poles @ TIFR Hyderabad">
                <img src="assets/images/sites/experience/experience_01.jpg" alt="MOKE Table" loading="lazy">
                <span class="carousel-slide-badge">2/3 • MOKE Optical Table</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/experience/experience_18.jpg" data-caption="Quantum Design PPMS (Physical Property Measurement System) Cryogenic Facility @ UoH">
                <img src="assets/images/sites/experience/experience_18.jpg" alt="PPMS Cryogenics" loading="lazy">
                <span class="carousel-slide-badge">3/3 • Quantum Design PPMS</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
            </div>
            <button class="carousel-btn prev" aria-label="Previous image">&#10094;</button>
            <button class="carousel-btn next" aria-label="Next image">&#10095;</button>
            <div class="carousel-dots"></div>
          </div>

          <ul class="facility-items">
            <li>Conventional MOKE (Magneto-Optical Kerr Effect) @ TIFR-H</li>
            <li>Quantum Design PPMS (Physical Property Measurement System)</li>
            <li>Broadband VNA-FMR (0.1–20 GHz)</li>
            <li>In-plane and Out-of-plane magnetic hysteresis loops</li>
          </ul>
        </div>

        <!-- Facility 3: Structural & Surface Analysis -->
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

          <!-- Carousel of 4 Related Analysis Photos -->
          <div class="mini-carousel" data-carousel>
            <div class="carousel-track">
              <div class="carousel-slide active" data-zoom-src="assets/images/sites/experience/experience_04.jpg" data-caption="Field Emission Scanning Electron Microscope (FESEM) control console @ UoH">
                <img src="assets/images/sites/experience/experience_04.jpg" alt="FESEM Console" loading="lazy">
                <span class="carousel-slide-badge">1/4 • FESEM Console & EDS</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/experience/experience_03.jpg" data-caption="FESEM high-resolution electron column @ University of Hyderabad">
                <img src="assets/images/sites/experience/experience_03.jpg" alt="FESEM Column" loading="lazy">
                <span class="carousel-slide-badge">2/4 • FESEM Electron Column</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/experience/experience_06.jpg" data-caption="Bruker D8 Advance thin film XRD diffractometer goniometer @ UoH">
                <img src="assets/images/sites/experience/experience_06.jpg" alt="XRD Gonio-Stage" loading="lazy">
                <span class="carousel-slide-badge">3/4 • Bruker D8 XRD</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/experience/experience_05.jpg" data-caption="Thin film Grazing Incidence XRD & X-ray Reflectivity (XRR) analysis setup">
                <img src="assets/images/sites/experience/experience_05.jpg" alt="GI-XRD Stage" loading="lazy">
                <span class="carousel-slide-badge">4/4 • GI-XRD / XRR Stage</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
            </div>
            <button class="carousel-btn prev" aria-label="Previous image">&#10094;</button>
            <button class="carousel-btn next" aria-label="Next image">&#10095;</button>
            <div class="carousel-dots"></div>
          </div>

          <ul class="facility-items">
            <li>FESEM (Field Emission Scanning Electron Microscopy)</li>
            <li>Powder & GI-XRD (Grazing Incidence X-ray Diffraction)</li>
            <li>X-ray Reflectivity (XRR) thin film thickness analysis</li>
            <li>Energy-Dispersive X-ray Spectroscopy (EDS)</li>
          </ul>
        </div>

        <!-- Facility 4: Cleanroom Nanofabrication -->
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

          <!-- Carousel of 3 Related Cleanroom Photos -->
          <div class="mini-carousel" data-carousel>
            <div class="carousel-track">
              <div class="carousel-slide active" data-zoom-src="assets/images/sites/gallery/gallery_01.jpg" data-caption="Receiving fabricated MEMS cantilever chips from Ms. Ashwini A (Facility Technologist, CeNSE, IISc Bangalore)">
                <img src="assets/images/sites/gallery/gallery_01.jpg" alt="CeNSE Cantilever Handover" loading="lazy">
                <span class="carousel-slide-badge">1/3 • Cantilever Device Release</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/gallery/gallery_02.jpg" data-caption="Nanofabrication process review with Mr. Venu V Bhat (Facility Technologist, CeNSE, IISc Bangalore)">
                <img src="assets/images/sites/gallery/gallery_02.jpg" alt="CeNSE Review" loading="lazy">
                <span class="carousel-slide-badge">2/3 • Process Parameter Review</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/gallery/gallery_03.jpg" data-caption="INUP-i2i Hands-on Nanofabrication Cohort at Centre for Nano Science and Engineering, IISc Bangalore">
                <img src="assets/images/sites/gallery/gallery_03.jpg" alt="CeNSE Cohort" loading="lazy">
                <span class="carousel-slide-badge">3/3 • INUP-i2i Participant Cohort</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
            </div>
            <button class="carousel-btn prev" aria-label="Previous image">&#10094;</button>
            <button class="carousel-btn next" aria-label="Next image">&#10095;</button>
            <div class="carousel-dots"></div>
          </div>

          <ul class="facility-items">
            <li>INUP-i2i Certified Cleanroom Fabrication (Class 100/1000)</li>
            <li>Optical Photolithography & Mask aligner processing</li>
            <li>Wet chemical etching & Reactive Ion Etching (RIE)</li>
            <li>MEMS micro-cantilever device fabrication & release</li>
          </ul>
        </div>

        <!-- Facility 5: Ion Beam Accelerator -->
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

          <div class="card-img-wrapper" style="height: 135px; margin-bottom: 12px;" data-zoom-src="assets/images/sites/gallery/gallery_07.jpg" data-caption="Swift Heavy Ion (SHI) Irradiation Beamline Experiment at Inter-University Accelerator Centre (IUAC), New Delhi">
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

        <!-- Facility 6: Profilometry & Spectroscopy -->
        <div class="facility-card">
          <div class="facility-header">
            <div class="facility-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg>
            </div>
            <div>
              <div class="facility-name">Metrology & Spectroscopy</div>
              <div class="facility-inst">CASEST & CFN, UoH</div>
            </div>
          </div>

          <!-- Carousel of 4 Related Metrology Photos -->
          <div class="mini-carousel" data-carousel>
            <div class="carousel-track">
              <div class="carousel-slide active" data-zoom-src="assets/images/sites/experience/experience_13.jpg" data-caption="Stylus Profilometer System stage & camera @ Centre for Nanotechnology (CFN), UoH">
                <img src="assets/images/sites/experience/experience_13.jpg" alt="Stylus Profilometer" loading="lazy">
                <span class="carousel-slide-badge">1/4 • Stylus Profilometer</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/experience/experience_16.jpg" data-caption="Atomic Force Microscopy (AFM) Head & scanner assembly @ University of Hyderabad">
                <img src="assets/images/sites/experience/experience_16.jpg" alt="AFM Facility" loading="lazy">
                <span class="carousel-slide-badge">2/4 • Atomic Force Microscope</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/experience/experience_07.jpg" data-caption="UV/VIS/NIR Spectrophotometer for optical bandgap & transmission studies @ UoH">
                <img src="assets/images/sites/experience/experience_07.jpg" alt="UV-VIS Spectrophotometer" loading="lazy">
                <span class="carousel-slide-badge">3/4 • UV/VIS/NIR Spectrometer</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
              <div class="carousel-slide" data-zoom-src="assets/images/sites/experience/experience_09.jpg" data-caption="Thermal Evaporation & Sputter Coater system for conductive contacts @ UoH">
                <img src="assets/images/sites/experience/experience_09.jpg" alt="Sputter Coater" loading="lazy">
                <span class="carousel-slide-badge">4/4 • Contact Sputter Coater</span>
                <span class="carousel-zoom-hint">🔍 Enlarge</span>
              </div>
            </div>
            <button class="carousel-btn prev" aria-label="Previous image">&#10094;</button>
            <button class="carousel-btn next" aria-label="Next image">&#10095;</button>
            <div class="carousel-dots"></div>
          </div>

          <ul class="facility-items">
            <li>Veeco/Bruker Stylus Profilometer step-height profiling</li>
            <li>Atomic Force Microscopy (AFM) surface topography</li>
            <li>UV/VIS/NIR Spectrophotometry optical absorption</li>
            <li>Vector Network Analyzer (VNA) microwave testing</li>
          </ul>
        </div>

      </div>'''

# Replace facilities grid
content = re.sub(r'<div class="facilities-grid">[\s\S]*?<\/div>\s*<\/div>\s*<\/section>', new_facilities_grid + '\n    </div>\n  </section>', content, count=1)

# 3. Update Conferences & Workshops Timeline with compact preview thumbnails
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

            <!-- Compact Media Preview -->
            <div class="timeline-thumb-box">
              <div class="timeline-thumb" data-zoom-src="assets/images/sites/conferences/conferences_01.jpg" data-caption="ICMAGMA 2025 Conference Presentation @ J.N. Tata Auditorium, IISc Bangalore">
                <img src="assets/images/sites/conferences/conferences_01.jpg" alt="ICMAGMA 2025" loading="lazy">
              </div>
              <div class="timeline-thumb-info">
                <div class="timeline-thumb-title">Conference Presentation Photo</div>
                <div class="timeline-thumb-caption">J. N. Tata Auditorium, IISc Bangalore • Click to preview</div>
              </div>
              <button class="timeline-thumb-zoom" data-zoom-src="assets/images/sites/conferences/conferences_01.jpg" data-caption="ICMAGMA 2025 Conference Presentation @ J.N. Tata Auditorium, IISc Bangalore">🔍 View Photo</button>
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

            <div class="timeline-thumb-box">
              <div class="timeline-thumb" data-zoom-src="assets/images/sites/workshops/workshops_01.jpg" data-caption="Powder and GI-XRD Advanced Instrument Training Certificate @ School of Physics, UoH">
                <img src="assets/images/sites/workshops/workshops_01.jpg" alt="GI-XRD Certificate" loading="lazy">
              </div>
              <div class="timeline-thumb-info">
                <div class="timeline-thumb-title">GI-XRD Training Certificate</div>
                <div class="timeline-thumb-caption">School of Physics, UoH • High-resolution thin film diffraction</div>
              </div>
              <button class="timeline-thumb-zoom" data-zoom-src="assets/images/sites/workshops/workshops_01.jpg" data-caption="Powder and GI-XRD Advanced Instrument Training Certificate @ School of Physics, UoH">🔍 View Certificate</button>
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

            <div class="timeline-thumb-box">
              <div class="timeline-thumb" data-zoom-src="assets/images/sites/workshops/workshops_02.jpg" data-caption="Workshop on Ion/Laser Beams in Nano-Science (WINS-2025) Certificate @ CFN, UoH">
                <img src="assets/images/sites/workshops/workshops_02.jpg" alt="WINS-2025 Workshop" loading="lazy">
              </div>
              <div class="timeline-thumb-info">
                <div class="timeline-thumb-title">WINS-2025 Symposium Certificate</div>
                <div class="timeline-thumb-caption">Centre for Nanotechnology, UoH • Beam-matter interactions</div>
              </div>
              <button class="timeline-thumb-zoom" data-zoom-src="assets/images/sites/workshops/workshops_02.jpg" data-caption="Workshop on Ion/Laser Beams in Nano-Science (WINS-2025) Certificate @ CFN, UoH">🔍 View Certificate</button>
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

            <div class="timeline-thumb-box">
              <div class="timeline-thumb" data-zoom-src="assets/images/sites/workshops/workshops_03.jpg" data-caption="ASSURE Workshop on Magnetism in collaboration with TIFR Hyderabad Certificate">
                <img src="assets/images/sites/workshops/workshops_03.jpg" alt="ASSURE Magnetism School" loading="lazy">
              </div>
              <div class="timeline-thumb-info">
                <div class="timeline-thumb-title">ASSURE Magnetism School Certificate</div>
                <div class="timeline-thumb-caption">TIFR Hyderabad & Osmania University • 10-day intensive school</div>
              </div>
              <button class="timeline-thumb-zoom" data-zoom-src="assets/images/sites/workshops/workshops_03.jpg" data-caption="ASSURE Workshop on Magnetism in collaboration with TIFR Hyderabad Certificate">🔍 View Certificate</button>
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

            <div class="timeline-thumb-box">
              <div class="timeline-thumb" data-zoom-src="assets/images/sites/conferences/conferences_02.jpg" data-caption="Frontiers in Physics (FIP 2024) Poster Presentation Certificate @ School of Physics, UoH">
                <img src="assets/images/sites/conferences/conferences_02.jpg" alt="FIP 2024" loading="lazy">
              </div>
              <div class="timeline-thumb-info">
                <div class="timeline-thumb-title">FIP 2024 Poster Certificate</div>
                <div class="timeline-thumb-caption">University of Hyderabad • VNA-FMR Landé g-factor findings</div>
              </div>
              <button class="timeline-thumb-zoom" data-zoom-src="assets/images/sites/conferences/conferences_02.jpg" data-caption="Frontiers in Physics (FIP 2024) Poster Presentation Certificate @ School of Physics, UoH">🔍 View Photo</button>
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

            <div class="timeline-thumb-box">
              <div class="timeline-thumb" data-zoom-src="assets/images/sites/conferences/conferences_05.jpg" data-caption="5th Asia Conference on Material and Manufacturing Technology (ACMMT 2023), Chiang Mai, Thailand">
                <img src="assets/images/sites/conferences/conferences_05.jpg" alt="ACMMT 2023 Thailand" loading="lazy">
              </div>
              <div class="timeline-thumb-info">
                <div class="timeline-thumb-title">ACMMT 2023 Thailand Proceedings</div>
                <div class="timeline-thumb-caption">Chiang Mai, Thailand • Room temperature static magnetic properties</div>
              </div>
              <button class="timeline-thumb-zoom" data-zoom-src="assets/images/sites/conferences/conferences_05.jpg" data-caption="5th Asia Conference on Material and Manufacturing Technology (ACMMT 2023), Chiang Mai, Thailand">🔍 View Photo</button>
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

            <div class="timeline-thumb-box">
              <div class="timeline-thumb" data-zoom-src="assets/images/sites/conferences/conferences_06.jpg" data-caption="ICACMP 2023 Oral Presentation Certificate @ GITAM Hyderabad">
                <img src="assets/images/sites/conferences/conferences_06.jpg" alt="ICACMP 2023" loading="lazy">
              </div>
              <div class="timeline-thumb-info">
                <div class="timeline-thumb-title">ICACMP 2023 Presentation Certificate</div>
                <div class="timeline-thumb-caption">GITAM University • VNA-FMR FeGaB characterization</div>
              </div>
              <button class="timeline-thumb-zoom" data-zoom-src="assets/images/sites/conferences/conferences_06.jpg" data-caption="ICACMP 2023 Oral Presentation Certificate @ GITAM Hyderabad">🔍 View Certificate</button>
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

            <div class="timeline-thumb-box">
              <div class="timeline-thumb" data-zoom-src="assets/images/sites/conferences/conferences_04.jpg" data-caption="ICMAGMA 2023 Presentation & Proceedings at Hyderabad">
                <img src="assets/images/sites/conferences/conferences_04.jpg" alt="ICMAGMA 2023" loading="lazy">
              </div>
              <div class="timeline-thumb-info">
                <div class="timeline-thumb-title">ICMAGMA 2023 Delegate Session</div>
                <div class="timeline-thumb-caption">Hyderabad, India • Magnetic Society of India meeting</div>
              </div>
              <button class="timeline-thumb-zoom" data-zoom-src="assets/images/sites/conferences/conferences_04.jpg" data-caption="ICMAGMA 2023 Presentation & Proceedings at Hyderabad">🔍 View Photo</button>
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

            <div class="timeline-thumb-box">
              <div class="timeline-thumb" data-zoom-src="assets/images/sites/workshops/workshops_07.jpg" data-caption="INUP-i2i Cleanroom Nanofabrication Certificate @ CeNSE, IISc Bangalore">
                <img src="assets/images/sites/workshops/workshops_07.jpg" alt="INUP-i2i Cleanroom Certificate" loading="lazy">
              </div>
              <div class="timeline-thumb-info">
                <div class="timeline-thumb-title">INUP-i2i Hands-on Cleanroom Certificate</div>
                <div class="timeline-thumb-caption">CeNSE, IISc Bangalore • Photolithography & MEMS cantilever etching</div>
              </div>
              <button class="timeline-thumb-zoom" data-zoom-src="assets/images/sites/workshops/workshops_07.jpg" data-caption="INUP-i2i Cleanroom Nanofabrication Certificate @ CeNSE, IISc Bangalore">🔍 View Certificate</button>
            </div>

            <p class="timeline-topic">
              Hands-on cleanroom fabrication of MEMS micro-cantilevers using photolithography, wet/dry etching, and laser vibrometer characterization under the Indian Nanoelectronics Users Programme.
            </p>
          </div>
        </div>

      </div>'''

# Replace timeline
content = re.sub(r'<div class="timeline-container">[\s\S]*?<\/div>\s*<\/div>\s*<\/section>', new_timeline + '\n    </div>\n  </section>', content, count=1)

# 4. Generate Refined 4-Column Compact Gallery with Curated Categories
manifest = [
  # In-House Setups (6)
  {'cat': 'setups', 'tag': 'In-House Bench', 'file': 'assets/images/sites/gallery/gallery_04.jpg', 'title': 'VNA-FMR Experimental Setup', 'desc': 'Vector Network Analyzer CPW fixture and calibrated electromagnet bench.'},
  {'cat': 'setups', 'tag': 'Standardization', 'file': 'assets/images/sites/gallery/gallery_05.jpg', 'title': 'VNA-FMR Thin Film Calibration', 'desc': 'Standardization of microwave S-parameters and damping factor extraction.'},
  {'cat': 'setups', 'tag': 'Multiferroic Bench', 'file': 'assets/images/sites/experimental_setups/experimental_setups_01.jpg', 'title': 'ME Voltage Facility', 'desc': 'Automated dynamic magnetoelectric voltage coefficient measurement bench.'},
  {'cat': 'setups', 'tag': 'Micro-Magnetics', 'file': 'assets/images/sites/experimental_setups/experimental_setups_02.jpg', 'title': 'Miniature Electromagnet (800 Oe)', 'desc': 'Compact 800 Oe @ 1A electromagnet custom engineered for RF probe stations.'},
  {'cat': 'setups', 'tag': 'Optoelectronic Device', 'file': 'assets/images/sites/experimental_setups/experimental_setups_03.jpg', 'title': 'Precision Optical Chopper', 'desc': 'Arduino & BLDC-driven high-speed chopper modulating light up to 2.8 kHz.'},
  {'cat': 'setups', 'tag': 'Circuit Schematic', 'file': 'assets/images/sites/experimental_setups/experimental_setups_04.jpg', 'title': 'Chopper Wiring Diagram', 'desc': 'Circuit schematic interfacing ESC, Arduino Uno, potentiometer, and motor.'},

  # Deposition & Nanofab (8)
  {'cat': 'synthesis', 'tag': 'CASEST UoH', 'file': 'assets/images/sites/experience/experience_10.jpg', 'title': 'DC/RF Sputtering Chamber', 'desc': 'Multi-target high-vacuum sputtering system for FeGaB thin films.'},
  {'cat': 'synthesis', 'tag': 'CASEST UoH', 'file': 'assets/images/sites/experience/experience_11.jpg', 'title': 'Power Rack & Gas Flow', 'desc': 'RF matching networks, DC power supplies, and Ar/O2 mass flow controllers.'},
  {'cat': 'synthesis', 'tag': 'CFN UoH', 'file': 'assets/images/sites/experience/experience_15.jpg', 'title': 'RF Deposition @ CFN', 'desc': 'Radio-frequency sputtering system for dielectric thin films.'},
  {'cat': 'synthesis', 'tag': 'Maintenance', 'file': 'assets/images/sites/experience/experience_14.jpg', 'title': 'Turbo Pump Overhaul', 'desc': 'Vacuum seal refurbishment and turbomolecular pump maintenance.'},
  {'cat': 'synthesis', 'tag': 'Cleanroom IISc', 'file': 'assets/images/sites/gallery/gallery_01.jpg', 'title': 'MEMS Cantilever Handover', 'desc': 'Receiving fabricated micro-cantilever chips from Ms. Ashwini A at CeNSE.'},
  {'cat': 'synthesis', 'tag': 'Cleanroom IISc', 'file': 'assets/images/sites/gallery/gallery_02.jpg', 'title': 'Nanofab Technical Review', 'desc': 'Reviewing device fabrication parameters with Mr. Venu V Bhat at CeNSE.'},
  {'cat': 'synthesis', 'tag': 'Cleanroom IISc', 'file': 'assets/images/sites/gallery/gallery_03.jpg', 'title': 'INUP-i2i Cohort @ IISc', 'desc': 'Nanofabrication training cohort at CeNSE, Indian Institute of Science.'},
  {'cat': 'synthesis', 'tag': 'Central Lab', 'file': 'assets/images/sites/experience/experience_09.jpg', 'title': 'Sputter Coater System', 'desc': 'High-vacuum coater for conductive contact deposition and SEM preparation.'},

  # Characterization Facilities (10)
  {'cat': 'characterization', 'tag': 'TIFR Hyderabad', 'file': 'assets/images/sites/experience/experience_01.jpg', 'title': 'Conventional MOKE Table', 'desc': 'Magneto-Optical Kerr Effect bench for magnetic domain and loop analysis.'},
  {'cat': 'characterization', 'tag': 'TIFR Hyderabad', 'file': 'assets/images/sites/experience/experience_02.jpg', 'title': 'MOKE Sample Stage', 'desc': 'Precision sample stage and optical alignment for longitudinal Kerr loops.'},
  {'cat': 'characterization', 'tag': 'Central Lab UoH', 'file': 'assets/images/sites/experience/experience_18.jpg', 'title': 'Quantum Design PPMS', 'desc': 'Cryogenic Physical Property Measurement System for magnetometry.'},
  {'cat': 'characterization', 'tag': 'FESEM UoH', 'file': 'assets/images/sites/experience/experience_03.jpg', 'title': 'FESEM Electron Column', 'desc': 'High-resolution field emission SEM for thin film morphology.'},
  {'cat': 'characterization', 'tag': 'FESEM UoH', 'file': 'assets/images/sites/experience/experience_04.jpg', 'title': 'FESEM Control Console', 'desc': 'Control console and energy-dispersive X-ray spectroscopy workstation.'},
  {'cat': 'characterization', 'tag': 'XRD UoH', 'file': 'assets/images/sites/experience/experience_05.jpg', 'title': 'Bruker D8 Thin Film XRD', 'desc': 'Diffractometer configured for grazing incidence and X-ray reflectivity.'},
  {'cat': 'characterization', 'tag': 'XRD UoH', 'file': 'assets/images/sites/experience/experience_06.jpg', 'title': 'XRD Gonio-Stage & Detector', 'desc': 'High-precision goniometer stage for crystallographic phase verification.'},
  {'cat': 'characterization', 'tag': 'Profilometry CFN', 'file': 'assets/images/sites/experience/experience_12.jpg', 'title': 'Stylus Profilometer System', 'desc': 'Veeco/Bruker stylus profilometer for thin film step-height measurement.'},
  {'cat': 'characterization', 'tag': 'Profilometry CFN', 'file': 'assets/images/sites/experience/experience_13.jpg', 'title': 'Stylus Scanning Mechanism', 'desc': 'Sub-nanometer diamond stylus and sample optical observation stage.'},
  {'cat': 'characterization', 'tag': 'AFM UoH', 'file': 'assets/images/sites/experience/experience_16.jpg', 'title': 'AFM Scanner & Head', 'desc': 'Atomic force microscope head for surface roughness analysis.'},

  # Beamline & Optics (6)
  {'cat': 'beamline', 'tag': 'IUAC New Delhi', 'file': 'assets/images/sites/gallery/gallery_07.jpg', 'title': 'Swift Heavy Ion Beamline', 'desc': 'Pelletron accelerator beamline hall at IUAC during SHI irradiation.'},
  {'cat': 'beamline', 'tag': 'Spectroscopy UoH', 'file': 'assets/images/sites/experience/experience_07.jpg', 'title': 'UV/VIS/NIR Spectrometer', 'desc': 'Dual-beam spectrophotometer for optical transmission and bandgap studies.'},
  {'cat': 'beamline', 'tag': 'Spectroscopy UoH', 'file': 'assets/images/sites/experience/experience_08.jpg', 'title': 'Spectrometer Sample Fixture', 'desc': 'Thin film optical holder in the spectrophotometer optical compartment.'},
  {'cat': 'beamline', 'tag': 'AFM UoH', 'file': 'assets/images/sites/experience/experience_17.jpg', 'title': 'AFM Isolation Platform', 'desc': 'Acoustic enclosure and active damping stage for atomic resolution.'},
  {'cat': 'beamline', 'tag': 'Lab Branding', 'file': 'assets/images/sites/home/home_01.jpg', 'title': 'Research Lab Banner Seal', 'desc': 'Official header identity from Arun B applied physics research portfolio.'},
  {'cat': 'beamline', 'tag': 'Academic Profile', 'file': 'assets/images/sites/home/home_02.jpg', 'title': 'Arun B Doctoral Scholar', 'desc': 'Centre for Advanced Studies in Electronics Science and Technology (CASEST).'},

  # Conferences (9)
  {'cat': 'conferences', 'tag': 'ICMAGMA 2025', 'file': 'assets/images/sites/conferences/conferences_01.jpg', 'title': 'ICMAGMA 2025 @ IISc', 'desc': 'Presentation on SHI irradiation effects in FeGaB films at IISc Bangalore.'},
  {'cat': 'conferences', 'tag': 'FIP 2024', 'file': 'assets/images/sites/conferences/conferences_02.jpg', 'title': 'Frontiers in Physics 2024', 'desc': 'Poster on VNA-FMR Landé g-factor determination in FeGaB thin films.'},
  {'cat': 'conferences', 'tag': 'NANOscientific', 'file': 'assets/images/sites/conferences/conferences_03.jpg', 'title': 'NANOscientific Symposium', 'desc': 'Certificate on nanoscale scanning probe characterization methodologies.'},
  {'cat': 'conferences', 'tag': 'ICMAGMA 2023', 'file': 'assets/images/sites/conferences/conferences_04.jpg', 'title': 'ICMAGMA 2023 Hyderabad', 'desc': 'Magnetic Materials and Applications conference proceedings in Hyderabad.'},
  {'cat': 'conferences', 'tag': 'ICMAGMA 2023', 'file': 'assets/images/sites/gallery/gallery_06.jpg', 'title': 'ICMAGMA 2023 Poster', 'desc': 'Poster session discussing microwave dynamic magnetic properties.'},
  {'cat': 'conferences', 'tag': 'ACMMT 2023', 'file': 'assets/images/sites/conferences/conferences_05.jpg', 'title': 'ACMMT 2023 Thailand', 'desc': 'Oral talk on room temperature magnetic properties of Pt/FeGaB/Pt trilayers.'},
  {'cat': 'conferences', 'tag': 'ICACMP 2023', 'file': 'assets/images/sites/conferences/conferences_06.jpg', 'title': 'ICACMP 2023 GITAM', 'desc': 'Oral presentation on VNA-FMR characterization of soft FeGaB thin films.'},
  {'cat': 'conferences', 'tag': 'FIP 2023', 'file': 'assets/images/sites/conferences/conferences_07.jpg', 'title': 'Frontiers in Physics 2023', 'desc': 'Poster session at School of Physics, UoH on microwave dynamics.'},
  {'cat': 'conferences', 'tag': 'ICRAMM 2019', 'file': 'assets/images/sites/conferences/conferences_08.jpg', 'title': 'ICRAMM 2019 Conference', 'desc': 'Presentation at Recent Advances in Materials and Manufacturing.'},

  # Workshops & Certifications (8)
  {'cat': 'workshops', 'tag': 'GI-XRD 2025', 'file': 'assets/images/sites/workshops/workshops_01.jpg', 'title': 'GI-XRD Certification', 'desc': 'School of Physics, UoH intensive training in thin film XRD and XRR.'},
  {'cat': 'workshops', 'tag': 'WINS-2025', 'file': 'assets/images/sites/workshops/workshops_02.jpg', 'title': 'WINS-2025 Ion/Laser Beams', 'desc': 'CFN, UoH workshop on ion/laser beam interaction in nanoscience.'},
  {'cat': 'workshops', 'tag': 'ASSURE 2024', 'file': 'assets/images/sites/workshops/workshops_03.jpg', 'title': 'ASSURE Magnetism School', 'desc': '10-day intensive school organized with TIFR Hyderabad at Osmania Univ.'},
  {'cat': 'workshops', 'tag': 'Rietveld 2024', 'file': 'assets/images/sites/workshops/workshops_04.jpg', 'title': 'Rietveld Refinement', 'desc': 'Training on crystallographic structural refinement from XRD data.'},
  {'cat': 'workshops', 'tag': 'Python 2024', 'file': 'assets/images/sites/workshops/workshops_05.jpg', 'title': 'Python Data Analytics', 'desc': 'Hands-on scientific computation and automated curve-fitting.'},
  {'cat': 'workshops', 'tag': 'Pondicherry', 'file': 'assets/images/sites/workshops/workshops_06.jpg', 'title': 'Magnetism Measurements', 'desc': 'Pondicherry University symposium on magnetic characterization.'},
  {'cat': 'workshops', 'tag': 'CeNSE IISc', 'file': 'assets/images/sites/workshops/workshops_07.jpg', 'title': 'INUP-i2i Nanofabrication', 'desc': 'Cleanroom certificate for photolithography and micro-cantilever release.'},
  {'cat': 'workshops', 'tag': 'IIT Bombay', 'file': 'assets/images/sites/workshops/workshops_08.jpg', 'title': 'INUP-i2i Familiarization', 'desc': 'Semiconductor nanofabrication technologies training certification.'}
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
              <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path></svg>
              <span>Original Archive</span>
            </div>
          </div>
        </div>'''
    gallery_cards_html.append(card)

new_gallery_section = f'''  <!-- ==========================================================================
       RESEARCH & EXPERIMENTAL GALLERY (ALL 47 MIRRORED IMAGES IN REFINED 4-COL GRID)
       ========================================================================== -->
  <section id="gallery" class="section section-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-badge">Visual Portfolio & Evidence</span>
        <h2 class="section-title">Research & Experimental Gallery</h2>
        <p class="section-subtitle">
          Curated index of all 47 original research images organized by scientific thrusts: in-house instrumentation, 
          thin film deposition, characterization facilities, conferences, and certifications.
        </p>
      </div>

      <!-- Local Mirror Callout Banner -->
      <div style="background: var(--bg-card); border: 1px solid var(--border-light); border-left: 4px solid var(--accent-cyan); padding: 14px 20px; border-radius: var(--radius-md); margin-bottom: 24px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; box-shadow: var(--shadow-sm);">
        <div>
          <div style="font-weight: 700; color: var(--text-primary); font-size: 0.9375rem; display: flex; align-items: center; gap: 8px;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent-cyan);"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
            Complete Local Offline Mirror of Published Google Site
          </div>
          <p style="color: var(--text-secondary); font-size: 0.8125rem; margin-top: 2px;">
            View the exact 7-page archive (sites.google.com/view/arunb) with original formatting and all media assets.
          </p>
        </div>
        <a href="site_mirror/home.html" target="_blank" class="btn btn-secondary" style="font-size: 0.8125rem; padding: 7px 14px; border-color: var(--accent-cyan); color: var(--accent-cyan); font-weight: 600;">
          Explore Local Mirror (7 Pages) &rarr;
        </a>
      </div>

      <!-- Gallery Filter Tabs -->
      <div class="gallery-filter-tabs">
        <button class="gallery-tab-btn active" data-category="all">All Photos (47)</button>
        <button class="gallery-tab-btn" data-category="setups">In-House Setups (6)</button>
        <button class="gallery-tab-btn" data-category="synthesis">Synthesis & Nanofab (8)</button>
        <button class="gallery-tab-btn" data-category="characterization">Characterization Labs (10)</button>
        <button class="gallery-tab-btn" data-category="conferences">Conferences & Talks (9)</button>
        <button class="gallery-tab-btn" data-category="workshops">Certifications & Schools (8)</button>
        <button class="gallery-tab-btn" data-category="beamline">Beamline & Metrology (6)</button>
      </div>

      <!-- Gallery Photo Grid (Refined 4-Column Layout) -->
      <div class="gallery-grid">
{chr(10).join(gallery_cards_html)}
      </div>

    </div>
  </section>'''

# Replace gallery section
content = re.sub(r'<\!-- ==========================================================================\s*RESEARCH & EXPERIMENTAL GALLERY[\s\S]*?<\/section>', new_gallery_section, content, count=1)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully reorganized website with mini-carousels, compact timeline media, and 4-column compact gallery!")

