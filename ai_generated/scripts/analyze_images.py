import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

imgs = soup.find_all('img')
print(f'Total images in index.html: {len(imgs)}')

for i, img in enumerate(imgs, 1):
    src = img.get('src', '')
    parent = img.parent
    p_tag = parent.name
    p_class = " ".join(parent.get('class', []))
    grandparent = parent.parent
    gp_tag = grandparent.name if grandparent else ""
    gp_class = " ".join(grandparent.get('class', [])) if grandparent else ""
    print(f"[{i:02d}] src: {src[:45]:<45} | Parent: {p_tag}.{p_class:<30} | Grandparent: {gp_tag}.{gp_class}")

