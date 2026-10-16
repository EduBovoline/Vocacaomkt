import os, re

cases = ['safety-first', 'maca-de-amor', 'tiwshirts', 'jardim-vivo-essencial', 'samurai', '']
base_dir = r'C:\Vocação 2027\QG Vocação 2027 do zero\Site'

for case in cases:
    html_file = os.path.join(base_dir, case, 'index.html')
    if not os.path.exists(html_file):
        print(f'{case}: index.html NOT FOUND')
        continue
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # find src, href, url()
    refs = re.findall(r'(?:src|href)=["\']([^"\'>#]+)["\']', content)
    refs += re.findall(r'url\(["\']?([^"\'\)]+)["\']?\)', content)
    
    missing = []
    found = []
    for r in set(refs):
        if r.startswith(('http:', 'https:', 'mailto:', 'tel:', 'data:', 'javascript:')):
            continue
        clean_r = r.split('?')[0].split('#')[0].strip()
        if not clean_r:
            continue
        local_path = os.path.normpath(os.path.join(base_dir, case, clean_r))
        if not os.path.exists(local_path):
            root_path = os.path.normpath(os.path.join(base_dir, clean_r))
            if os.path.exists(root_path):
                missing.append((r, f'EXISTS AT ROOT BUT WRONG RELATIVE PATH ({root_path})'))
            else:
                missing.append((r, 'NOT FOUND ANYWHERE'))
        else:
            found.append(r)
    
    print(f'=== CASE: {case} ===')
    print(f'Found {len(found)} assets, Missing {len(missing)} assets')
    for m, status in sorted(missing):
        print(f'  MISSING: {m} -> {status}')
