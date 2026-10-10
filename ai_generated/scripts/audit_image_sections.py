import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("=== AUDIT OF ALL IMAGE PARENTS IN INDEX.HTML ===")
for sec in soup.find_all('section'):
    sec_id = sec.get('id', 'no-id')
    imgs = sec.find_all('img')
    if imgs:
        print(f"\nSection #{sec_id}: {len(imgs)} images")
        for i, img in enumerate(imgs, 1):
            src = img.get('src', '')
            parent_classes = ".".join(img.parent.get('class', ['no-class']))
            inline_style = img.get('style', '') or img.parent.get('style', '')
            print(f"  {i}. {src[:40]:<40} in <{img.parent.name}.{parent_classes}> [inline: {inline_style[:30]}]")

