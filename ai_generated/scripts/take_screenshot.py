import subprocess
import os
import time

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"c:\Users\arun\Downloads\portfolio\index.html"
file_url = "file:///" + html_path.replace("\\", "/")

os.makedirs("_data/screenshots", exist_ok=True)

# 1. Take a screenshot of top/hero
out_top = os.path.abspath("_data/screenshots/top.png")
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--window-size=1280,900",
    f"--screenshot={out_top}",
    file_url
]
subprocess.run(cmd, capture_output=True)
print(f"Top screenshot captured: {os.path.exists(out_top)} ({out_top})")

# 2. Check playwright or selenium to take full page or scroll screenshots
try:
    import selenium
    print("Selenium available!")
except ImportError:
    print("Selenium not installed.")

