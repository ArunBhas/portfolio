import os
import sys
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(text, 'html.parser')

print("Image file dimensions on disk:")
for img in soup.find_all('img'):
    src = img.get('src')
    if src and not src.startswith('data:') and os.path.exists(src):
        with Image.open(src) as im:
            w, h = im.size
            ratio = w / h
            print(f"{src[:45]:<45} : {w}x{h} (aspect: {ratio:.2f})")

