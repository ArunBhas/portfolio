with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="conferences"')
end_conf = text.find('</section>', idx)
conf_html = text[idx:end_conf]

import re
matches = re.findall(r'<h3 class="timeline-event">(.*?)</h3>', conf_html)
print(f"Total conference events: {len(matches)}")
for m in matches:
    print("-", m)

