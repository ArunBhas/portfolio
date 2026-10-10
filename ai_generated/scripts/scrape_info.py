import urllib.request
import json
import re
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

urls = {
    'home': 'https://sites.google.com/view/arunb/home',
    'publications': 'https://sites.google.com/view/arunb/publications',
    'conferences': 'https://sites.google.com/view/arunb/conferences',
    'workshops': 'https://sites.google.com/view/arunb/workshops-and-trainings',
    'experimental_setups': 'https://sites.google.com/view/arunb/experimental-setups-development',
    'experience': 'https://sites.google.com/view/arunb/experience',
    'gallery': 'https://sites.google.com/view/arunb/gallery'
}

data = {}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            
            # Google sites structure often has class "TYR3kc" or role "main"
            main = soup.find('div', role='main') or soup.find('body')
            
            text_lines = []
            for tag in main.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'span']):
                t = tag.get_text(separator=' ', strip=True)
                if t and t not in text_lines and len(t) > 2:
                    # filter out menu repetition if possible
                    if t not in ['Home', 'Publications', 'Conferences', 'Workshops and Trainings', 
                                 'Experimental Setups Development', 'Experience', 'Gallery', 'More']:
                        text_lines.append(t)
            
            links = []
            for a in main.find_all('a'):
                h = a.get('href', '')
                t = a.get_text(strip=True)
                if h and not h.startswith('#'):
                    links.append({'text': t, 'href': h})
                    
            images = []
            for img in main.find_all('img'):
                src = img.get('src', '')
                alt = img.get('alt', '')
                if src and not 'cleardot.gif' in src:
                    images.append({'src': src, 'alt': alt})
                    
            data[name] = {
                'url': url,
                'title': soup.title.string if soup.title else '',
                'texts': text_lines,
                'links': links,
                'images': images
            }
            print(f'Done {name}: {len(text_lines)} text items, {len(links)} links, {len(images)} images')
    except Exception as e:
        print(f'Error fetching {name}: {e}')

with open('google_sites_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('Finished saving google_sites_extracted.json')
