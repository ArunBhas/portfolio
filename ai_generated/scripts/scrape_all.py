import urllib.request
import json
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

pages = {
    'home': 'https://sites.google.com/view/arunb/home',
    'publications': 'https://sites.google.com/view/arunb/publications',
    'conferences': 'https://sites.google.com/view/arunb/conferences',
    'workshops': 'https://sites.google.com/view/arunb/workshops-and-trainings',
    'experimental_setups': 'https://sites.google.com/view/arunb/experimental-setups-development',
    'experience': 'https://sites.google.com/view/arunb/experience',
    'gallery': 'https://sites.google.com/view/arunb/gallery',
    'scholar': 'https://scholar.google.com/citations?user=Su9nLc4AAAAJ&hl=en',
    'github': 'https://github.com/ArunBhas'
}

results = {}

for name, url in pages.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            
            # extract images
            imgs = []
            for img in soup.find_all('img'):
                src = img.get('src', '')
                alt = img.get('alt', '')
                if src and not 'cleardot' in src:
                    imgs.append({'src': src, 'alt': alt})

            # extract links
            links = []
            for a in soup.find_all('a'):
                h = a.get('href', '')
                t = a.get_text(strip=True)
                if h and not h.startswith('#'):
                    links.append({'text': t, 'href': h})

            # remove scripts and styles
            for s in soup(['script', 'style']):
                s.decompose()
                
            strings = [s for s in soup.stripped_strings if s]
            
            results[name] = {
                'title': soup.title.string if soup.title else '',
                'strings': strings,
                'links': links,
                'images': imgs
            }
            print(f"Scraped {name}: {len(strings)} strings, {len(links)} links, {len(imgs)} imgs")
    except Exception as e:
        print(f"Error scraping {name}: {e}")

with open('all_scraped_data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("Saved all_scraped_data.json successfully")
