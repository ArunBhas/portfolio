import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

conf_sec = soup.find('section', id='conferences')
items = conf_sec.find_all('div', class_='timeline-item')
for i, it in enumerate(items, 1):
    event = it.find('h3', class_='timeline-event').text.strip()
    thumb_box = it.find('div', class_='timeline-thumb-box')
    img = thumb_box.find('img') if thumb_box else None
    src = img.get('src') if img else ""
    caption = thumb_box.find('div', class_='timeline-thumb').get('data-caption', '') if thumb_box else ""
    title = thumb_box.find('div', class_='timeline-thumb-title').text.strip() if thumb_box and thumb_box.find('div', class_='timeline-thumb-title') else event
    print(f"Item {i}:")
    print(f"  Event: {event}")
    print(f"  Src: {src}")
    print(f"  Title: {title}")
    print(f"  Caption: {caption}\n")

