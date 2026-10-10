import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="conferences"')
end_conf = text.find('</section>', idx)
conf_html = text[idx:end_conf]

# Find where timeline-thumb-box is defined
m = re.search(r'(<div class="timeline-thumb-box">.*?</div>\s*</div>\s*</div>)', conf_html, re.DOTALL)
if m:
    print(m.group(1)[:500])

