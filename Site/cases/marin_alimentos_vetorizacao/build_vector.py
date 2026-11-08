import xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

def text_to_paths(text, font_path, font_size, letter_spacing=0.0):
    font = TTFont(font_path)
    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()
    hmtx = font['hmtx']
    units_per_em = font['head'].unitsPerEm
    scale = font_size / units_per_em

    cur_x = 0.0
    paths = []
    
    for char in text:
        if char == ' ':
            cur_x += font_size * 0.35 + letter_spacing
            continue
        code = ord(char)
        if code not in cmap:
            continue
        glyph_name = cmap[code]
        adv, lsb = hmtx[glyph_name]
        
        pen = SVGPathPen(glyph_set)
        tpen = TransformPen(pen, (scale, 0, 0, -scale, cur_x, 0))
        glyph = glyph_set[glyph_name]
        glyph.draw(tpen)
        
        d = pen.getCommands()
        if d:
            paths.append(d)
        cur_x += adv * scale + letter_spacing
        
    return paths, cur_x

def extract_paths_from_svg(svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()
    return root.findall('{http://www.w3.org/2000/svg}path')

# Get text paths
font_bd = r'C:\Windows\Fonts\arialbd.ttf'

del_paths, del_w = text_to_paths('DELIVERY', font_bd, 13.5, 2.5)
del_x = 358.5 - del_w / 2
del_y = 138

ret_paths, ret_w = text_to_paths('RETIRADA', font_bd, 13.5, 2.5)
ret_x = 498.5 - ret_w / 2
ret_y = 138

ali_paths, ali_w = text_to_paths('ALIMENTOS NO BALCÃO', font_bd, 9.5, 3.8)
ali_x = 157.0 - ali_w / 2
ali_y = 163

svg_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 574 190" width="574" height="190">',
    '  <!-- Fundo Preto -->',
    '  <rect width="574" height="190" fill="#080808" rx="10" ry="10"/>',
    '  <!-- Borda Externa -->',
    '  <rect x="5.5" y="9.5" width="563" height="171" rx="8" ry="8" fill="none" stroke="#F5A602" stroke-width="2.2"/>',
    '  <!-- Divisores Verticais -->',
    '  <line x1="283" y1="50" x2="283" y2="153" stroke="#F5A602" stroke-width="2.2" stroke-linecap="round"/>',
    '  <line x1="431" y1="58" x2="431" y2="140" stroke="#F5A602" stroke-width="2.2" stroke-linecap="round"/>',
    '  <!-- Marin Script -->',
    '  <g id="logo-marin" transform="translate(20, 25) scale(0.25)">'
]

for p in extract_paths_from_svg('marin_clean.svg'):
    d = p.attrib.get('d', '')
    tf = p.attrib.get('transform', '')
    svg_lines.append(f'    <path d="{d}" fill="#FFFFFF" transform="{tf}"/>')
svg_lines.append('  </g>')

svg_lines.append('  <!-- Chapéu de Chef e Sublinhado -->')
svg_lines.append('  <g id="logo-chapeu-swoosh" transform="translate(20, 25) scale(0.25)">')
for p in extract_paths_from_svg('hat_swoosh_clean.svg'):
    d = p.attrib.get('d', '')
    tf = p.attrib.get('transform', '')
    svg_lines.append(f'    <path d="{d}" fill="#F5A602" transform="{tf}"/>')
svg_lines.append('  </g>')

svg_lines.append('  <!-- Ícone Moto Delivery -->')
svg_lines.append('  <g id="icone-scooter" transform="translate(305, 45) scale(0.25)">')
for p in extract_paths_from_svg('scooter_clean.svg'):
    d = p.attrib.get('d', '')
    tf = p.attrib.get('transform', '')
    svg_lines.append(f'    <path d="{d}" fill="#F5A602" transform="{tf}"/>')
svg_lines.append('  </g>')

svg_lines.append('  <!-- Ícone Sacola Retirada -->')
svg_lines.append('  <g id="icone-sacola" transform="translate(450, 45) scale(0.25)">')
for p in extract_paths_from_svg('bag_clean.svg'):
    d = p.attrib.get('d', '')
    tf = p.attrib.get('transform', '')
    svg_lines.append(f'    <path d="{d}" fill="#F5A602" fill-rule="evenodd" transform="{tf}"/>')
svg_lines.append('  </g>')

svg_lines.append('  <!-- Textos em Curvas -->')
svg_lines.append(f'  <g id="texto-delivery" transform="translate({del_x:.2f}, {del_y})">')
for d in del_paths:
    svg_lines.append(f'    <path d="{d}" fill="#FFFFFF"/>')
svg_lines.append('  </g>')

svg_lines.append(f'  <g id="texto-retirada" transform="translate({ret_x:.2f}, {ret_y})">')
for d in ret_paths:
    svg_lines.append(f'    <path d="{d}" fill="#FFFFFF"/>')
svg_lines.append('  </g>')

svg_lines.append(f'  <g id="texto-alimentos" transform="translate({ali_x:.2f}, {ali_y})">')
for d in ali_paths:
    svg_lines.append(f'    <path d="{d}" fill="#FFFFFF"/>')
svg_lines.append('  </g>')

svg_lines.append('</svg>')

with open('marin_alimentos.svg', 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg_lines))

# Version with transparent background
lines_transp = [line for line in svg_lines if 'id="bg"' not in line and 'fill="#080808"' not in line]
with open('marin_alimentos_transparente.svg', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines_transp))

import subprocess
# 1. PDF
subprocess.run(['magick', 'marin_alimentos.svg', '-density', '300', 'marin_alimentos.pdf'])
# 2. PNG Oficial 600 DPI (alta resolução para impressão)
subprocess.run(['magick', 'marin_alimentos.svg', '-density', '600', 'marin_alimentos_alta_resolucao.png'])
# 3. PNG Transparente 600 DPI
subprocess.run(['magick', 'marin_alimentos_transparente.svg', '-density', '600', '-background', 'none', 'marin_alimentos_transparente.png'])

print('All exports created successfully!')
