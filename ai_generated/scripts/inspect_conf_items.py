import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

conf_sec = soup.find('section', id='conferences')
items = conf_sec.find_all('div', class_='timeline-item')
print(f"Total timeline items: {len(items)}")
for i, it in enumerate(items, 1):
    event = it.find('h3', class_='timeline-event').text.strip()
    thumb_box = it.find('div', class_='timeline-thumb-box')
    img = it.find('img')
    img_src = img.get('src') if img else "None"
    print(f"Event {i}: '{event}'")
    print(f"  - Has thumb_box: {bool(thumb_box)} | img: {img_src}")

