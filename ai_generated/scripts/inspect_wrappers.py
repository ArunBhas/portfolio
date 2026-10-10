import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

setups_sec = soup.find('section', id='setups')
for c in setups_sec.find_all('div', class_='setup-card'):
    t = c.find('h3', class_='setup-title').text.strip()
    img_wrap = c.find('div', class_='card-img-wrapper')
    if img_wrap:
        print(f"Setup with card-img-wrapper: {t}")
        print(str(img_wrap)[:300])

fac_sec = soup.find('section', id='facilities')
for c in fac_sec.find_all('div', class_='facility-card'):
    t = c.find('div', class_='facility-name').text.strip()
    img_wrap = c.find('div', class_='card-img-wrapper')
    if img_wrap:
        print(f"\nFacility with card-img-wrapper: {t}")
        print(str(img_wrap)[:300])

