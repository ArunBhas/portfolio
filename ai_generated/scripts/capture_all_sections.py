import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"c:\Users\arun\Downloads\portfolio\index.html"
file_url = "file:///" + html_path.replace("\\", "/")

os.makedirs("_data/screenshots", exist_ok=True)

# Helper to create a wrapper HTML that scrolls to a specific element and takes screenshot
sections = ['setups', 'facilities', 'conferences', 'gallery']

with open('index.html', 'r', encoding='utf-8') as f:
    orig_html = f.read()

for sec in sections:
    # Inject an onload script to scroll to section
    scroll_script = f'''<script>
    window.addEventListener('DOMContentLoaded', () => {{
      const el = document.getElementById('{sec}');
      if (el) {{
        el.scrollIntoView();
      }}
    }});
    </script>'''
    temp_html_content = orig_html.replace('</body>', scroll_script + '</body>')
    temp_path = os.path.abspath(f'_data/screenshots/temp_{sec}.html')
    with open(temp_path, 'w', encoding='utf-8') as tf:
        tf.write(temp_html_content)

    out_png = os.path.abspath(f'_data/screenshots/{sec}.png')
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--window-size=1280,1000",
        f"--screenshot={out_png}",
        f"file:///{temp_path.replace('\\', '/')}"
    ]
    subprocess.run(cmd, capture_output=True)
    print(f"Captured {sec}.png: {os.path.exists(out_png)}")

print("All section screenshots captured successfully!")

