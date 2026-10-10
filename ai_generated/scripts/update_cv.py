with open('cv.html', 'r', encoding='utf-8') as f:
    cv = f.read()

cv = cv.replace('Academic Curriculum Vitae of Arun B, Senior Research Scholar at CASEST, School of Physics, University of Hyderabad.',
                'Academic Curriculum Vitae of Arun B, Senior Research Scholar affiliated with School of Physics, University of Hyderabad (CASEST Laboratory).')

old_dept = """        <div class="cv-dept">
          Centre for Advanced Studies in Electronics Science and Technology (CASEST)<br>
          School of Physics, University of Hyderabad, Telangana, India
        </div>"""

new_dept = """        <div class="cv-dept">
          School of Physics, University of Hyderabad, Telangana, India<br>
          <em>CASEST Laboratory</em>
        </div>"""

cv = cv.replace(old_dept, new_dept)

old_email = """      <div class="cv-contact-info">
        <div><strong>Email:</strong> <a href="mailto:arunb@uohyd.ac.in">arunb@uohyd.ac.in</a></div>
        <div><strong>Alt Email:</strong> <a href="mailto:arunbhas@gmail.com">arunbhas@gmail.com</a></div>"""

new_email = """      <div class="cv-contact-info">
        <div><strong>Email:</strong> <a href="mailto:arunskalikavu@gmail.com">arunskalikavu@gmail.com</a></div>
        <div><strong>Alt Email:</strong> <a href="mailto:arunb@uohyd.ac.in">arunb@uohyd.ac.in</a></div>"""

cv = cv.replace(old_email, new_email)

cv = cv.replace('<div class="cv-entry-sub">Centre for Advanced Studies in Electronics Science and Technology (CASEST), School of Physics, University of Hyderabad</div>',
                '<div class="cv-entry-sub">School of Physics, University of Hyderabad (CASEST Laboratory)</div>')

cv = cv.replace('"Investigation of the magnetic properties of FeGaB thin films via VNA-FMR and micromagnetic modeling"',
                '"Investigation of the magnetic properties of FeGaB thin films via VNA-FMR and high-frequency characterization"')

cv = cv.replace('Arduino Embedded C++, OOMMF.', 'Arduino Embedded C++, Automated Data Acquisition.')

with open('cv.html', 'w', encoding='utf-8') as f:
    f.write(cv)

print('Updated cv.html cleanly!')

