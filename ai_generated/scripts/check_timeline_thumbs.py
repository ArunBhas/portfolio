with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<div class="timeline-thumb-box">.*?</div>\s*</div>', text, re.DOTALL)
print(f"Total timeline-thumb-box: {len(matches)}")
if matches:
    print(matches[0][:400])

