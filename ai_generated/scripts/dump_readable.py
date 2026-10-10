import json

with open('all_scraped_data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open('all_content_readable.md', 'w', encoding='utf-8') as out:
    for page, val in d.items():
        out.write(f'# PAGE: {page}\n\n')
        out.write(f'Title: {val.get("title", "")}\n\n')
        out.write('## Text Strings:\n\n')
        for s in val.get('strings', []):
            if s not in ['Skip to main content', 'Skip to navigation', 'Search this site', 'Embedded Files', 'Google Sites', 'Report abuse', 'Page details', 'Page updated']:
                out.write(f'{s}\n\n')
        out.write('\n## Links:\n\n')
        for l in val.get('links', []):
            out.write(f'- [{l.get("text", "")}]({l.get("href", "")})\n')
        out.write('\n## Images:\n\n')
        for im in val.get('images', []):
            out.write(f'- src: {im.get("src", "")} | alt: {im.get("alt", "")}\n')
        out.write('\n' + '='*80 + '\n\n')

print('Wrote all_content_readable.md successfully')
