with open('assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
# Remove .theme-toggle-btn rules
css = re.sub(r'\.theme-toggle-btn\s*\{[^}]*\}', '', css)
css = re.sub(r'\.theme-toggle-btn:hover\s*\{[^}]*\}', '', css)
css = css.replace(', .theme-toggle-btn', '')

with open('assets/css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Cleaned unused theme-toggle-btn rules from styles.css!")

