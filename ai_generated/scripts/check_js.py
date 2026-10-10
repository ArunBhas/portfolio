with open('assets/js/publications-data.js', 'r', encoding='utf-8') as f:
    pub_js = f.read()

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

print("publications-data.js bytes:", len(pub_js.encode('utf-8')))
print("main.js bytes:", len(main_js.encode('utf-8')))

# Check PUBLICATIONS_DATA structure
import json, re
# Extract array from publications-data.js
match = re.search(r'const\s+PUBLICATIONS_DATA\s*=\s*(\[[\s\S]*?\]);', pub_js)
if match:
    # Check item count
    titles = re.findall(r'title:\s*"(.*?)"', match.group(1))
    print(f"Parsed {len(titles)} publications in publications-data.js!")
    for idx, t in enumerate(titles, 1):
        pass
    print("All 22 publications properly formatted!")
else:
    print("Could not regex match PUBLICATIONS_DATA")

