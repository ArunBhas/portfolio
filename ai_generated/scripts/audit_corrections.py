import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

files_to_check = ['index.html', 'cv.html', 'assets/js/main.js', 'assets/css/styles.css']

terms_to_flag = [
    ('Old Email (arunbhas)', r'arunbhas@gmail\.com'),
    ('Site mirror button/link', r'site_mirror'),
    ('Micromagnetic mentions', r'micromagnetic'),
    ('Theme toggle button', r'theme-toggle-btn'),
    ('Dark mode toggle icon', r'theme-toggle-icon'),
]

print("=== THOROUGH AUDIT OF USER CORRECTIONS ===")
for file_name in files_to_check:
    print(f"\nScanning: {file_name}")
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  Error reading {file_name}: {e}")
        continue

    for label, pattern in terms_to_flag:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            print(f"  ⚠️ FOUND {len(matches)} instance(s) of '{label}'!")
            # Show snippet
            for m in re.finditer(pattern, content, re.IGNORECASE):
                snippet = content[max(0, m.start()-40):min(len(content), m.end()+40)]
                print(f"     Context: {repr(snippet.strip())}")
        else:
            print(f"  ✅ '{label}': None found.")

print("\nAudit complete!")

