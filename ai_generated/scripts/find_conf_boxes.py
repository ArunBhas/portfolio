with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="conferences"')
end_conf = text.find('</section>', idx)
conf_html = text[idx:end_conf]

# Find timeline-thumb-box occurrences
import re
boxes = list(re.finditer(r'<div class="timeline-thumb-box">', conf_html))
print(f"Total timeline-thumb-box: {len(boxes)}")
for i, m in enumerate(boxes):
    start = m.start()
    snippet = conf_html[start:start+400]
    print(f"--- BOX {i+1} ---")
    print(snippet[:snippet.find('</div>\n            </div>') + 25])

