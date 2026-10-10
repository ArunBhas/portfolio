with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_setups = text.find('id="setups"')
idx_fac = text.find('id="facilities"')
end_fac = text.find('</section>', idx_fac)

print("Setups section preview:")
print(text[idx_setups:idx_setups+800])

print("\nFacilities section preview:")
print(text[idx_fac:idx_fac+800])

