import subprocess

with open('marin_logo_header.svg', 'r', encoding='utf-8') as f:
    c = f.read()

c_with_bg = c.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 560" width="1024" height="560">',
                      '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 560" width="1024" height="560"><rect width="100%" height="100%" fill="#0b0b0d"/>')

with open('preview_with_bg.svg', 'w', encoding='utf-8') as f:
    f.write(c_with_bg)

subprocess.run(['magick', 'preview_with_bg.svg', 'preview_logo_perfect.png'])
print('Rendered preview_logo_perfect.png')
