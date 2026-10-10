import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_setups = text.find('id="setups"')
print("=== SETUP CARD 1 ===")
print(text[idx_setups+400:idx_setups+1400])

idx_fac = text.find('id="facilities"')
print("\n=== FACILITY CARD 1 ===")
print(text[idx_fac+400:idx_fac+1400])

