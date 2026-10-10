import os
#!/usr/bin/env python3
"""
Dynamic Google Scholar Synchronization Script for Arun B Academic Portfolio
Author: Arun B (School of Physics, University of Hyderabad)
Google Scholar ID: Su9nLc4AAAAJ

Fetches latest citation metrics and publication data from Google Scholar,
updates assets/js/publications-data.js and index.html statistics,
and prepares changes for automated commit & deployment.
"""

import sys
import re
import json
from datetime import datetime

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: 'requests' and 'beautifulsoup4' are required. Install with: pip install requests beautifulsoup4")
    sys.exit(1)

SCHOLAR_ID = "Su9nLc4AAAAJ"
SCHOLAR_URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en&pagesize=100"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

def fetch_scholar_data():
    print(f"Fetching Google Scholar data for user: {SCHOLAR_ID}...")
    try:
        resp = requests.get(SCHOLAR_URL, headers=HEADERS, timeout=20)
        resp.raise_for_status()
    except Exception as e:
        print(f"Network error while fetching Google Scholar: {e}")
        return None

    soup = BeautifulSoup(resp.text, 'html.parser')

    # Extract citation metrics table
    metrics_cells = soup.select('td.gsc_rsb_std')
    if len(metrics_cells) >= 6:
        total_citations = int(metrics_cells[0].text.strip() or 0)
        citations_since_2019 = int(metrics_cells[1].text.strip() or 0)
        h_index = int(metrics_cells[2].text.strip() or 0)
        h_index_since_2019 = int(metrics_cells[3].text.strip() or 0)
        i10_index = int(metrics_cells[4].text.strip() or 0)
        i10_since_2019 = int(metrics_cells[5].text.strip() or 0)
    else:
        print("Warning: Could not parse metrics table from Scholar page.")
        return None

    # Extract publication rows
    pubs = []
    rows = soup.select('tr.gsc_a_tr')
    for row in rows:
        title_el = row.select_one('a.gsc_a_at')
        authors_el = row.select_one('div.gs_gray')
        venue_el = row.select('div.gs_gray')
        cites_el = row.select_one('a.gsc_a_ac')
        year_el = row.select_one('span.gsc_a_h')

        title = title_el.text.strip() if title_el else ""
        link = ("https://scholar.google.com" + title_el['href']) if (title_el and 'href' in title_el.attrs) else ""
        authors = authors_el.text.strip() if authors_el else ""
        venue = venue_el[1].text.strip() if len(venue_el) > 1 else ""
        cites_str = cites_el.text.strip() if cites_el else "0"
        cites = int(cites_str) if cites_str.isdigit() else 0
        year = year_el.text.strip() if year_el else ""

        if title:
            pubs.append({
                'title': title,
                'link': link,
                'authors': authors,
                'venue': venue,
                'citations': cites,
                'year': year
            })

    print(f"Successfully scraped Scholar metrics:")
    print(f"  - Total Citations: {total_citations}")
    print(f"  - h-index: {h_index}")
    print(f"  - i10-index: {i10_index}")
    print(f"  - Indexed Publications: {len(pubs)}")

    return {
        'total_citations': total_citations,
        'citations_since_2019': citations_since_2019,
        'h_index': h_index,
        'i10_index': i10_index,
        'publications': pubs,
        'sync_date': datetime.now().strftime("%Y-%m-%d")
    }

def update_publications_data_js(scholar_data):
    candidates = ['website/assets/js/publications-data.js', 'assets/js/publications-data.js']
    target_paths = [p for p in candidates if os.path.exists(p)]
    if not target_paths:
        print("Warning: Neither website/assets/js/publications-data.js nor assets/js/publications-data.js found.")
        return False

    for js_path in target_paths:
        _do_update_js(js_path, scholar_data)
    return True

def _do_update_js(js_path, scholar_data):
    try:
        with open(js_path, 'r', encoding='utf-8') as f:
            js_content = f.read()
    except FileNotFoundError:
        print(f"File {js_path} not found.")
        return False

    # Normalize titles for matching
    def norm(t):
        return re.sub(r'[^a-zA-Z0-9]', '', t).lower()

    scholar_map = {norm(p['title']): p for p in scholar_data['publications']}

    # Update citation counts in existing entries
    updated_count = 0
    for sch_norm, sch_item in scholar_map.items():
        # Match title in JS file
        for m in re.finditer(r'title:\s*"([^"]+)",[\s\S]*?citations:\s*(\d+)', js_content):
            file_title = m.group(1)
            old_cites = int(m.group(2))
            if norm(file_title) == sch_norm or sch_norm.startswith(norm(file_title)[:25]):
                new_cites = sch_item['citations']
                if old_cites != new_cites:
                    old_sub = m.group(0)
                    new_sub = old_sub.replace(f"citations: {old_cites}", f"citations: {new_cites}")
                    js_content = js_content.replace(old_sub, new_sub)
                    updated_count += 1
                break

    # Update metadata header in publications-data.js
    meta_comment = f"""/**
 * CURATED PUBLICATION DATASET - ARUN B (B. Arun)
 * Senior Research Scholar, School of Physics, University of Hyderabad
 * 
 * Auto-synced with Google Scholar: {scholar_data['sync_date']}
 * Total Citations: {scholar_data['total_citations']} | h-index: {scholar_data['h_index']} | i10-index: {scholar_data['i10_index']}
 */"""

    # Replace top comment if exists
    js_content = re.sub(r'/\*\*[\s\S]*?\*/', meta_comment, js_content, count=1)

    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"Updated {js_path}: {updated_count} publication citation counts refreshed.")
    return True

def update_html_metrics(scholar_data):
    candidates = ['website/index.html', 'index.html']
    target_paths = [p for p in candidates if os.path.exists(p)]
    for html_path in target_paths:
        _do_update_html(html_path, scholar_data)
    return True

def _do_update_html(html_path, scholar_data):
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        print(f"File {html_path} not found.")
        return False

    cites = scholar_data['total_citations']
    h_idx = scholar_data['h_index']
    i10_idx = scholar_data['i10_index']

    # Update impact section stat numbers if present
    # Citation counter data-target
    html = re.sub(
        r'(<div class="impact-stat-number" data-target=")\d+(".*?>)\d+\+?(</div>\s*<div class="impact-stat-label">Citations)',
        rf'\g<1>{cites}\g<2>{cites}+\g<3>',
        html
    )

    # h-index data-target
    html = re.sub(
        r'(<div class="impact-stat-number" data-target=")\d+(".*?>)\d+(</div>\s*<div class="impact-stat-label">h-Index)',
        rf'\g<1>{h_idx}\g<2>{h_idx}\g<3>',
        html
    )

    # i10-index data-target
    html = re.sub(
        r'(<div class="impact-stat-number" data-target=")\d+(".*?>)\d+(</div>\s*<div class="impact-stat-label">i10-Index)',
        rf'\g<1>{i10_idx}\g<2>{i10_idx}\g<3>',
        html
    )

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Updated {html_path} impact metrics to: {cites}+ Citations, h-index {h_idx}, i10-index {i10_idx}.")
    return True

def main():
    print("=" * 60)
    print("Arun B - Dynamic Google Scholar Sync Engine")
    print("=" * 60)
    data = fetch_scholar_data()
    if not data:
        print("Failed to sync from Google Scholar.")
        sys.exit(1)

    update_publications_data_js(data)
    update_html_metrics(data)
    print("=" * 60)
    print(f"Synchronization completed successfully on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}!")
    print("=" * 60)

if __name__ == '__main__':
    main()

