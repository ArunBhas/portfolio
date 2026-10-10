with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="gallery"')
end_gallery = text.find('</section>', idx)
print("Gallery length:", end_gallery - idx)
print(text[idx+1200:idx+2500])

