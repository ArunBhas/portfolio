with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m2 = re.search(r'<div class="setup-card">\s*<span class="setup-badge">Multiferroics</span>.*?</div>\s*</div>\s*</div>', text, re.DOTALL)
if m2:
    print("Found Setup 2!")
    print(m2.group(0)[:400])

m3 = re.search(r'<div class="setup-card">\s*<span class="setup-badge">Micro-Magnetics Hardware</span>.*?</div>\s*</div>\s*</div>', text, re.DOTALL)
if m3:
    print("\nFound Setup 3!")
    print(m3.group(0)[:400])

m5 = re.search(r'<div class="facility-card">.*?<div class="facility-name">Ion Beam Accelerator Facility</div>.*?</div>\s*</div>\s*</div>', text, re.DOTALL)
if m5:
    print("\nFound Facility 5!")
    print(m5.group(0)[:400])

