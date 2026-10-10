import os
import glob
from bs4 import BeautifulSoup

def audit_html(file_path):
    print(f"\n--- Auditing {file_path} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Check images
    imgs = soup.find_all('img')
    broken_imgs = []
    base_dir = os.path.dirname(file_path)
    
    for img in imgs:
        src = img.get('src')
        if not src or src.startswith('data:'):
            continue
        # resolve relative to base_dir
        resolved = os.path.normpath(os.path.join(base_dir, src))
        if not os.path.exists(resolved):
            broken_imgs.append((src, resolved))
    
    print(f"Total images checked: {len(imgs)}")
    if broken_imgs:
        print(f"[FAIL] Broken images ({len(broken_imgs)}):")
        for orig, res in broken_imgs[:10]:
            print(f"   {orig} -> {res}")
    else:
        print("[PASS] All images exist and resolved cleanly!")

# Audit modern website
audit_html('index.html')
audit_html('cv.html')

# Audit mirror files
for mirror in sorted(glob.glob('site_mirror/*.html')):
    audit_html(mirror)
