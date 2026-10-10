import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="conferences"')
end_conf = text.find('</section>', idx)
conf_html = text[idx:end_conf]

thumbs = re.findall(r'<div class="timeline-thumb" data-zoom-src="(.*?)" data-caption="(.*?)">', conf_html)
print(f"Total thumbs found: {len(thumbs)}")
for i, (src, cap) in enumerate(thumbs):
    print(f"{i+1}: {src} -> {cap}")

