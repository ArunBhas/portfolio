with open('assets/css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('STRICT COMPACT MEDIA')
print(css[idx:idx+2500])

