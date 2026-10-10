import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="conferences"')
end_conf = text.find('</section>', idx)
conf_html = text[idx:end_conf]

# Match timeline-thumb-box and its content
pattern = r'(<!-- Compact Media Preview -->\s*<div class="timeline-thumb-box">.*?</div>\s*</div>)'
boxes = re.findall(pattern, conf_html, re.DOTALL)
print(f"Matched {len(boxes)} boxes")
for i, b in enumerate(boxes):
    print(f"\n--- BOX {i+1} ---")
    print(b)

