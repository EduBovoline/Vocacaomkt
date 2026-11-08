import xml.etree.ElementTree as ET
import subprocess

tree = ET.parse('marin_logo_simbolo.svg')
root = tree.getroot()
paths = root.findall('{http://www.w3.org/2000/svg}path')

# Path 0 is hat: #F5A602
# Paths 1, 2, 3, 4 are letters: #FFFFFF
svg_out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 560" width="1024" height="560">']
for i, p in enumerate(paths):
    d = p.attrib.get('d', '')
    tf = p.attrib.get('transform', '')
    col = '#F5A602' if i == 0 else '#FFFFFF'
    svg_out.append(f'  <path d="{d}" fill="{col}" transform="{tf}"/>')
svg_out.append('</svg>')

with open('marin_logo_header.svg', 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg_out))

subprocess.run(['magick', 'marin_logo_header.svg', '-background', '#0b0b0d', '-flatten', 'preview_logo_header.png'])
print('Logo header SVG created successfully')
