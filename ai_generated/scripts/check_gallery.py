with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="gallery"')
print("Gallery index:", idx)
if idx != -1:
    print(text[idx:idx+1200])

