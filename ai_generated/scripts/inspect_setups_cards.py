import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

setups_sec = soup.find('section', id='setups')
cards = setups_sec.find_all('div', class_='setup-card')
print(f"Total setup cards: {len(cards)}")
for i, c in enumerate(cards, 1):
    title = c.find('h3', class_='setup-title').text.strip()
    carousels = c.find_all('div', class_='mini-carousel')
    grids = c.find_all('div', class_='setup-photo-grid')
    wrappers = c.find_all('div', class_='card-img-wrapper')
    imgs = c.find_all('img')
    print(f"Setup {i}: '{title}'")
    print(f"  - Carousels: {len(carousels)} | Photo-grids: {len(grids)} | Card-img-wrappers: {len(wrappers)} | Total imgs: {len(imgs)}")

