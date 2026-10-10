with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="conferences"')
end_conf = text.find('</section>', idx)
print("Conferences length:", end_conf - idx)
print(text[idx:idx+1500])

