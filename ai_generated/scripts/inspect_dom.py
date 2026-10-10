from bs4 import BeautifulSoup
import os

pages = ['conferences', 'workshops', 'experimental_setups', 'experience', 'gallery', 'home']

for page in pages:
    path = os.path.join('site_mirror', f'{page}.html')
    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    print(f'\n======================================================')
    print(f'=== DOM INSPECT: {page} ===')
    print(f'======================================================')
    for i, img in enumerate(soup.find_all('img')):
        src = img.get('src', '')
        base = os.path.basename(src)
        
        # Look for section or surrounding grid item
        sec = img.find_parent('section')
        if sec:
            strings = [s for s in sec.stripped_strings if s not in ['Skip to main content', 'Skip to navigation', 'Search this site', 'Embedded Files', 'Google Sites', 'Report abuse', 'Page details', 'Page updated']]
            txt = ' | '.join(strings[:5])
            print(f'  IMG #{i+1} [{base}]: {txt[:120]}')
        else:
            p = img.parent
            txt = ''
            for _ in range(5):
                if not p:
                    break
                s = [x for x in p.stripped_strings if x]
                if s:
                    txt = ' | '.join(s[:4])
                    break
                p = p.parent
            print(f'  IMG #{i+1} [{base}]: (parent) {txt[:120]}')
