import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

fac_sec = soup.find('section', id='facilities')
cards = fac_sec.find_all('div', class_='facility-card')
print(f"Total facility cards: {len(cards)}")
for i, c in enumerate(cards, 1):
    title = c.find('div', class_='facility-name').text.strip()
    carousels = c.find_all('div', class_='mini-carousel')
    wrappers = c.find_all('div', class_='card-img-wrapper')
    imgs = c.find_all('img')
    print(f"Facility {i}: '{title}'")
    print(f"  - Carousels: {len(carousels)} | Card-img-wrappers: {len(wrappers)} | Total imgs: {len(imgs)}")
    for im in imgs:
        print(f"     img: {im.get('src')}")

