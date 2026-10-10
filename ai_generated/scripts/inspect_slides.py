import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("1. Setups slides:")
for c in soup.find_all('div', class_='setup-card'):
    t = c.find('h3', class_='setup-title').text.strip()
    slides = [s.get('data-zoom-src') for s in c.find_all('div', class_='carousel-slide')]
    print(f"  {t}: {slides}")

print("\n2. Facility 5 slides:")
for c in soup.find_all('div', class_='facility-card'):
    t = c.find('div', class_='facility-name').text.strip()
    if 'Accelerator' in t:
        slides = [s.get('data-zoom-src') for s in c.find_all('div', class_='carousel-slide')]
        print(f"  {t}: {slides}")

