import glob

banner_html = '''<div id="portfolio-mirror-top-banner" style="background: #0f172a; color: #f8fafc; padding: 10px 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 13px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; border-bottom: 2px solid #0284c7; position: sticky; top: 0; z-index: 999999; box-shadow: 0 4px 12px rgba(0,0,0,0.35);">
  <div style="display: flex; align-items: center; gap: 10px;">
    <span style="background: #0284c7; color: #ffffff; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Local Archive</span>
    <span style="color: #e2e8f0; font-weight: 500;">Offline Mirror of Original Google Site (sites.google.com/view/arunb) • All 47 Images Preserved Locally</span>
  </div>
  <div style="display: flex; align-items: center; gap: 10px;">
    <a href="../index.html" style="background: #2563eb; color: #ffffff; text-decoration: none; padding: 6px 14px; border-radius: 6px; font-weight: 600; font-size: 12px; display: inline-flex; align-items: center; gap: 6px; transition: background 0.2s;">
      &larr; Switch to Modern Portfolio
    </a>
    <a href="../cv.html" target="_blank" style="background: #10b981; color: #ffffff; text-decoration: none; padding: 6px 14px; border-radius: 6px; font-weight: 600; font-size: 12px;">
      📄 Curriculum Vitae
    </a>
  </div>
</div>'''

for filepath in glob.glob('site_mirror/*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if 'id="portfolio-mirror-top-banner"' in html:
        print(f"Banner already present in {filepath}")
        continue
    
    # insert right after <body ...>
    if '<body' in html:
        parts = html.split('<body', 1)
        # find the end of the body tag
        rest = parts[1]
        closing_angle = rest.find('>')
        before_body = parts[0] + '<body' + rest[:closing_angle+1]
        after_body = rest[closing_angle+1:]
        new_html = before_body + '\n' + banner_html + '\n' + after_body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Added mirror banner to {filepath}")
    else:
        print(f"Could not find <body> in {filepath}")

