import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Correction 1 & 2: Email, Affiliation, Meta
html = html.replace('arunbhas@gmail.com', 'arunskalikavu@gmail.com')
html = html.replace(
    '<title>Arun B | Senior Research Scholar - Applied Physics & Materials Science | University of Hyderabad</title>',
    '<title>Arun B | Senior Research Scholar - School of Physics, University of Hyderabad</title>'
)
html = html.replace(
    'Academic and research portfolio of Arun B (B. Arun), Senior Research Scholar at CASEST, School of Physics, University of Hyderabad. Specializing in thin film synthesis, VNA-FMR, microwave characterization, magnetoelectric devices, and instrumentation.',
    'Academic and research portfolio of Arun B (B. Arun), Senior Research Scholar affiliated with the School of Physics, University of Hyderabad (working in CASEST laboratory). Specializing in thin film synthesis, VNA-FMR, microwave characterization, magnetoelectric devices, and instrumentation.'
)

# Schema.org worksFor department
html = html.replace(
    '"department": "Centre for Advanced Studies in Electronics Science and Technology (CASEST), School of Physics"',
    '"department": "School of Physics (CASEST Laboratory)"'
)

# Correction 4: Remove darkmode toggle button from nav-actions
old_nav_actions = '''      <div class="nav-actions">
        <button id="theme-toggle-btn" class="theme-toggle-btn" aria-label="Toggle dark/light theme">
          <span id="theme-toggle-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
          </span>
        </button>
        <a href="site_mirror/home.html" target="_blank" class="nav-btn-cv" style="background-color: var(--accent-cyan); margin-right: 4px;" title="Browse local offline mirror of original Google Site">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1 4-10z"></path></svg>
          Original Mirror
        </a>
        <a href="cv.html" target="_blank" class="nav-btn-cv" style="background-color: var(--accent-emerald);">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
          Curriculum Vitae
        </a>
        <button id="mobile-menu-btn" class="mobile-menu-btn" aria-label="Toggle mobile navigation">☰</button>
      </div>'''

new_nav_actions = '''      <div class="nav-actions">
        <a href="cv.html" target="_blank" class="nav-btn-cv" style="background-color: var(--accent-primary);">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
          Curriculum Vitae
        </a>
        <button id="mobile-menu-btn" class="mobile-menu-btn" aria-label="Toggle mobile navigation">☰</button>
      </div>'''

html = html.replace(old_nav_actions, new_nav_actions)

# Remove mirror link from mobile drawer
html = html.replace(
    '    <a href="site_mirror/home.html" target="_blank" class="nav-link" style="color: var(--accent-cyan); font-weight: 700;">🌐 Original Google Site Mirror</a>\n',
    ''
)

# Correction 2 & 3: Hero section role, institution, bio
old_hero_info = '''        <h1 class="hero-title">Arun B</h1>
        <div class="hero-role">Senior Research Scholar in Applied Physics</div>
        <div class="hero-institution">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
          CASEST, School of Physics • University of Hyderabad, India
        </div>

        <p class="hero-bio">
          Pioneering investigations into <strong>thin film synthesis</strong>, <strong>high-frequency microwave dynamics</strong>, 
          and <strong>broadband ferromagnetic resonance (VNA-FMR)</strong>. Actively bridging material physics and functional engineering 
          through custom laboratory instrumentation, micromagnetic simulations, and multiferroic magnetoelectric devices.
        </p>'''

new_hero_info = '''        <h1 class="hero-title">Arun B</h1>
        <div class="hero-role">Senior Research Scholar</div>
        <div class="hero-institution">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
          School of Physics, University of Hyderabad, India • CASEST Laboratory
        </div>

        <p class="hero-bio">
          Doctoral research in <strong>thin film synthesis</strong>, <strong>high-frequency microwave dynamics</strong>, 
          and <strong>broadband ferromagnetic resonance (VNA-FMR)</strong>. Bridging fundamental physics and device engineering 
          through custom laboratory instrumentation, functional materials synthesis, and multiferroic magnetoelectric composites.
        </p>'''

html = html.replace(old_hero_info, new_hero_info)

# Profile Card Dept & Uni
old_profile_card = '''          <h2 class="profile-card-name">B. Arun</h2>
          <div class="profile-card-dept">CASEST, School of Physics</div>
          <div class="profile-card-uni">University of Hyderabad, India</div>'''

new_profile_card = '''          <h2 class="profile-card-name">B. Arun</h2>
          <div class="profile-card-dept">School of Physics</div>
          <div class="profile-card-uni">University of Hyderabad, India</div>
          <div style="font-size: 0.8125rem; color: var(--text-muted); margin-top: 2px;">CASEST Laboratory</div>'''

html = html.replace(old_profile_card, new_profile_card)

# Profile Card Email
html = html.replace(
    '<span>arunb@uohyd.ac.in</span>',
    '<span>arunskalikavu@gmail.com</span>'
)

# Correction 2 & 3 in About Section
old_about_text = '''        <p class="section-subtitle">
          Doctoral researcher at the Centre for Advanced Studies in Electronics Science and Technology (CASEST), 
          School of Physics, University of Hyderabad, working under the guidance of Prof. K. C. James Raju.
        </p>'''

new_about_text = '''        <p class="section-subtitle">
          Doctoral researcher affiliated with the School of Physics, University of Hyderabad, 
          conducting advanced experimental investigations in the CASEST laboratory under the guidance of Prof. K. C. James Raju.
        </p>'''

html = html.replace(old_about_text, new_about_text)

# Remove micromagnetic skill tag
html = html.replace(
    '<span class="skill-tag">Micromagnetic Simulation (OOMMF)</span>',
    '<span class="skill-tag">Microwave VNA-FMR Dynamics</span>'
)

# Student thesis title correction
html = html.replace(
    '"Investigation of the magnetic properties of FeGaB thin films via VNA-FMR and micromagnetic modeling"',
    '"Investigation of the magnetic properties of FeGaB thin films via VNA-FMR and high-frequency characterization"'
)

# Contact section email and lab affiliation
old_contact_lab = '''              <div>
                <div class="contact-entry-label">Laboratory Affiliation</div>
                <div class="contact-entry-value">Centre for Advanced Studies in Electronics Science and Technology (CASEST)</div>
                <div style="font-size: 0.875rem; color: var(--text-muted); margin-top: 2px;">
                  School of Physics, University of Hyderabad, Prof. C. R. Rao Road, Gachibowli, Hyderabad 500046, Telangana, India
                </div>
              </div>'''

new_contact_lab = '''              <div>
                <div class="contact-entry-label">Academic Affiliation & Lab</div>
                <div class="contact-entry-value">School of Physics, University of Hyderabad</div>
                <div style="font-size: 0.875rem; color: var(--text-muted); margin-top: 2px;">
                  Working in CASEST Laboratory, Prof. C. R. Rao Road, Gachibowli, Hyderabad 500046, Telangana, India
                </div>
              </div>'''

html = html.replace(old_contact_lab, new_contact_lab)

# Contact section email list
old_contact_emails = '''              <div>
                <div class="contact-entry-label">Email Addresses</div>
                <div class="contact-entry-value"><a href="mailto:arunb@uohyd.ac.in">arunb@uohyd.ac.in</a></div>
                <div style="font-size: 0.875rem; color: var(--text-muted);"><a href="mailto:arunskalikavu@gmail.com">arunskalikavu@gmail.com</a></div>
              </div>'''

new_contact_emails = '''              <div>
                <div class="contact-entry-label">Email Addresses</div>
                <div class="contact-entry-value"><a href="mailto:arunskalikavu@gmail.com">arunskalikavu@gmail.com</a></div>
                <div style="font-size: 0.875rem; color: var(--text-muted); margin-top: 2px;"><a href="mailto:arunb@uohyd.ac.in">arunb@uohyd.ac.in</a></div>
              </div>'''

html = html.replace(old_contact_emails, new_contact_emails)

# Footer bio
old_footer_desc = '''          <p class="footer-brand-desc">
            Senior Research Scholar at the School of Physics & CASEST, University of Hyderabad. 
            Investigating thin film magnetism, microwave VNA-FMR, magnetoelectric coupling, and instrumentation.
          </p>'''

new_footer_desc = '''          <p class="footer-brand-desc">
            Senior Research Scholar affiliated with the School of Physics, University of Hyderabad (working in CASEST Laboratory). 
            Investigating thin film synthesis, microwave VNA-FMR dynamics, magnetoelectric coupling, and instrumentation.
          </p>'''

html = html.replace(old_footer_desc, new_footer_desc)

# Remove mirror link from footer
html = html.replace(
    '            <li><a href="site_mirror/home.html" target="_blank" style="color: var(--accent-cyan); font-weight: 600;">🌐 Original Google Site Mirror</a></li>\n',
    ''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html: Email, Affiliation, micromagnetics removed, mirror button removed!")

# 2. Update cv.html
with open('cv.html', 'r', encoding='utf-8') as f:
    cv = f.read()

cv = cv.replace('arunbhas@gmail.com', 'arunskalikavu@gmail.com')
cv = cv.replace(
    'CASEST, School of Physics, University of Hyderabad',
    'School of Physics, University of Hyderabad (CASEST Laboratory)'
)
cv = cv.replace(
    '<div class="cv-dept">CASEST, School of Physics</div>',
    '<div class="cv-dept">School of Physics (CASEST Laboratory)</div>'
)
# Remove mirror button from CV action-bar
cv = cv.replace(
    '    <a href="site_mirror/home.html" target="_blank" class="btn-action">\n      🌐 Original Site Mirror\n    </a>\n',
    ''
)

with open('cv.html', 'w', encoding='utf-8') as f:
    f.write(cv)

print("Updated cv.html successfully!")
