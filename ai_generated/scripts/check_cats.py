import os
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_data/all_scraped_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Scraped categories:")
for cat, items in data.get('images_by_category', {}).items():
    print(f"- {cat}: {len(items)} images")

