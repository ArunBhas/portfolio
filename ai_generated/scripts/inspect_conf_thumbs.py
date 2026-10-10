import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="conferences"')
end_conf = text.find('</section>', idx)
conf_html = text[idx:end_conf]

# Find all timeline items
items = re.findall(r'<div class="timeline-item">.*?</div>\s*</div>\s*</div>', conf_html, re.DOTALL)
print(f"Found {len(items)} items")
for i, item in enumerate(items):
    # extract title
    title_m = re.search(r'<h3 class="timeline-event">(.*?)</h3>', item)
    title = title_m.group(1) if title_m else "N/A"
    # extract thumb box
    thumb_m = re.search(r'<div class="timeline-thumb-box">.*?</div>\s*</div>', item, re.DOTALL)
    print(f"Item {i+1}: {title} | Has thumb: {bool(thumb_m)}")

