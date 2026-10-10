import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

setups_sec = soup.find('section', id='setups')
for c in setups_sec.find_all('div', class_='setup-card'):
    title = c.find('h3', class_='setup-title').text.strip()
    print(f"\n--- {title} ---")
    print(str(c)[:500])

