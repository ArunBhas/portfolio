with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('class="timeline-thumb-box"')
print(text[idx-50:idx+450])

