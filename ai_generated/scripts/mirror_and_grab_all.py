import os
import re
import json
import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup

PAGES = {
    'home': 'https://sites.google.com/view/arunb/home',
    'publications': 'https://sites.google.com/view/arunb/publications',
    'conferences': 'https://sites.google.com/view/arunb/conferences',
    'workshops': 'https://sites.google.com/view/arunb/workshops-and-trainings',
    'experimental_setups': 'https://sites.google.com/view/arunb/experimental-setups-development',
    'experience': 'https://sites.google.com/view/arunb/experience',
    'gallery': 'https://sites.google.com/view/arunb/gallery'
}

SITE_MIRROR_DIR = 'site_mirror'
ASSETS_IMG_DIR = os.path.join('assets', 'images', 'sites')

os.makedirs(SITE_MIRROR_DIR, exist_ok=True)
os.makedirs(ASSETS_IMG_DIR, exist_ok=True)

# Cookie jar opener for persistent session cookies
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'),
    ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'),
    ('Accept-Language', 'en-US,en;q=0.9'),
]

manifest = []
downloaded_urls = {}

print("=================================================================")
print("STARTING SCRAPE & MIRROR OF ALL GOOGLE SITES PAGES & IMAGES")
print("=================================================================\n")

for page_key, page_url in PAGES.items():
    print(f"\n>>> Fetching page: [{page_key}] -> {page_url}")
    try:
        req = urllib.request.Request(page_url)
        resp = opener.open(req)
        html = resp.read().decode('utf-8', errors='ignore')
        
        soup = BeautifulSoup(html, 'html.parser')
        
        # Directory for this page in assets
        page_img_dir = os.path.join(ASSETS_IMG_DIR, page_key)
        os.makedirs(page_img_dir, exist_ok=True)
        
        # Find all img tags
        img_tags = soup.find_all('img')
        print(f"    Found {len(img_tags)} img tags on {page_key}")
        
        img_idx = 0
        for img in img_tags:
            src = img.get('src', '')
            if not src or 'cleardot.gif' in src:
                continue
                
            img_idx += 1
            
            # Find context caption: previous or next headings or sibling text
            caption = img.get('alt', '').strip()
            if not caption:
                # check nearby siblings or parent's parent text
                parent = img.parent
                for _ in range(4):
                    if not parent:
                        break
                    # check for headings or paragraph nearby
                    h = parent.find_previous(['h1', 'h2', 'h3', 'h4', 'p', 'div'])
                    if h:
                        txt = h.get_text(strip=True)
                        if txt and len(txt) > 3 and txt not in ['Arun B', 'Home', 'Publications', 'Conferences', 'Workshops and Trainings', 'Experimental Setups Development', 'Experience', 'Gallery', 'More']:
                            caption = txt
                            break
                    parent = parent.parent
            
            # Determine filename
            clean_caption = re.sub(r'[^a-zA-Z0-9_\-]', '_', caption[:40]).strip('_')
            if clean_caption:
                img_filename = f"{page_key}_{img_idx:02d}_{clean_caption}.jpg"
            else:
                img_filename = f"{page_key}_{img_idx:02d}.jpg"
                
            local_save_path = os.path.join(page_img_dir, img_filename)
            rel_asset_path = f"assets/images/sites/{page_key}/{img_filename}".replace('\\', '/')
            
            # If already downloaded in this run
            if src in downloaded_urls:
                print(f"    [Reusing] {img_filename} (Already fetched)")
                actual_rel_path = downloaded_urls[src]
                img['src'] = actual_rel_path
                manifest.append({
                    'page': page_key,
                    'index': img_idx,
                    'filename': os.path.basename(actual_rel_path),
                    'path': actual_rel_path,
                    'caption': caption,
                    'original_url': src
                })
                continue
                
            # Download image
            try:
                img_req = urllib.request.Request(src)
                img_req.add_header('Referer', page_url)
                img_resp = opener.open(img_req, timeout=20)
                img_data = img_resp.read()
                
                with open(local_save_path, 'wb') as f:
                    f.write(img_data)
                    
                downloaded_urls[src] = rel_asset_path
                file_size = len(img_data)
                print(f"    [OK] Saved {img_filename} ({file_size / 1024:.1f} KB) - Caption: '{caption[:60]}'")
                
                # Rewrite img tag src for mirror
                img['src'] = f"../{rel_asset_path}"
                
                manifest.append({
                    'page': page_key,
                    'index': img_idx,
                    'filename': img_filename,
                    'path': rel_asset_path,
                    'size_bytes': file_size,
                    'caption': caption,
                    'original_url': src
                })
            except Exception as e:
                print(f"    [ERROR] Failed downloading {src[:60]}: {e}")
                
        # Also rewrite navigation links in the mirror
        for a in soup.find_all('a'):
            href = a.get('href', '')
            if href.startswith('/view/arunb/'):
                target_page = href.replace('/view/arunb/', '').split('?')[0].split('#')[0]
                if target_page == 'home' or not target_page:
                    a['href'] = 'home.html'
                else:
                    a['href'] = f"{target_page}.html"
                    
        # Save local mirror HTML
        mirror_filename = f"{page_key}.html"
        mirror_path = os.path.join(SITE_MIRROR_DIR, mirror_filename)
        with open(mirror_path, 'w', encoding='utf-8') as mf:
            mf.write(str(soup))
        print(f"    [Mirror Saved] {mirror_path}")
        
    except Exception as e:
        print(f"[ERROR] Failed fetching {page_key}: {e}")

# Save image manifest
manifest_path = os.path.join('assets', 'images', 'sites_manifest.json')
with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print("\n=================================================================")
print(f"SCRAPING COMPLETE! Total images cataloged: {len(manifest)}")
print(f"Manifest written to: {manifest_path}")
print("=================================================================")
