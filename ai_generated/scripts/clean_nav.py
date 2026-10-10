import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_block = re.search(r'<div class="nav-actions">.*?</div>\s*</div>\s*</header>', text, re.DOTALL)
if old_block:
    new_actions = """<div class="nav-actions">
        <a href="cv.html" target="_blank" class="nav-btn-cv" style="background-color: var(--accent-primary);">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
          Curriculum Vitae
        </a>
        <button id="mobile-menu-btn" class="mobile-menu-btn" aria-label="Toggle mobile navigation">☰</button>
      </div>
    </div>
  </header>"""
    text = text[:old_block.start()] + new_actions + text[old_block.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Cleaned nav-actions successfully!")
else:
    print("Could not find nav-actions block!")

