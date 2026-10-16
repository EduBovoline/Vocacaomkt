import json
import re

path = 'auto_responder_docker/data/leads_100_santa_rosalia_brasilandia.json'
with open(path, 'r', encoding='utf-8') as f:
    leads = json.load(f)

for l in leads:
    name = l.get("name", "").strip()
    addr = l.get("address", "").strip()
    street = addr.split(',')[0] if ',' in addr else addr
    street_clean = re.sub(r'[\.\-]', '', street).strip()
    street_phrase = f" na {street_clean}" if street_clean and len(street_clean) > 3 else ""
    
    bairro = l.get("bairro", "Santa Rosália")
    if "brasilândia" in bairro.lower():
        bairro_ref = "aqui da região do Santa Rosália"
    else:
        bairro_ref = "aqui do Santa Rosália"
        
    site = (l.get("site") or "").strip()
    gargalo = (l.get("gargalo") or "").lower()
    
    # REGRA: Condicional estrito sobre o gargalo real verificado
    if site and len(site) > 5:
        # 1. TEM SITE VERIFICADO
        l["hook_a"] = (
            f"Oi, tudo bem? Aqui é o Eduardo, da Vocação {bairro_ref}.\n"
            f"Estava olhando o site de vocês pelo celular e reparei num contraste: o espaço físico de vocês{street_phrase} é excelente, mas na tela do smartphone a página tem um visual antigo que não passa essa mesma autoridade de primeira.\n"
            f"A gente faz a modernização dessas páginas em 5 dias aqui na região. Com quem eu consigo falar sobre o site de vocês?"
        )
        l["hook_b"] = (
            f"Opa, tudo bem? Eduardo, da Vocação {bairro_ref}.\n"
            f"Dei uma olhada na versão de celular do site de vocês{street_phrase} e vi uma oportunidade rápida de aumentar a conversão de quem pesquisa na região.\n"
            f"Posso te mandar uma prévia visual de 1 minuto mostrando como a gente faz isso em 5 dias?"
        )
    elif "maps" in gargalo and ("foto" in gargalo or "ficha" in gargalo or "tour" in gargalo):
        # 2. GARGALO VERIFICADO NO MAPS (Sem falar de site que não existe)
        l["hook_a"] = (
            f"Oi, tudo bem? Aqui é o Eduardo, da Vocação {bairro_ref}.\n"
            f"Vi a ficha de vocês no Google Maps{street_phrase}. O trabalho de vocês é ótimo, mas a apresentação no Google ainda não reflete a qualidade do espaço físico para quem pesquisa na nossa região.\n"
            f"A gente estrutura essa autoridade visual em 5 dias aqui no bairro. Quem cuida dessa parte de imagem com vocês?"
        )
        l["hook_b"] = (
            f"Opa, tudo bem? Eduardo, da Vocação {bairro_ref}.\n"
            f"Reparei num detalhe na presença de vocês no Maps{street_phrase} que pode trazer mais contatos diretos no WhatsApp de quem mora no bairro.\n"
            f"Posso te mandar um resumo visual de 1 minuto sobre isso?"
        )
    else:
        # 3. NÃO TEM SITE PRÓPRIO (Depende de redes/Maps)
        l["hook_a"] = (
            f"Oi, tudo bem? Aqui é o Eduardo, da Vocação {bairro_ref}.\n"
            f"Vi a estrutura e o trabalho de vocês{street_phrase}, mas reparei que quem procura pelos serviços no Google aqui pelo celular não encontra uma página própria da empresa para passar confiança de primeira antes de chamar no WhatsApp.\n"
            f"A gente estrutura essa vitrine profissional em 5 dias aqui na região. Quem cuida dessa parte digital com vocês?"
        )
        l["hook_b"] = (
            f"Opa, tudo bem? Eduardo, da Vocação {bairro_ref}.\n"
            f"Reparei que vocês têm um trabalho muito bom{street_phrase}, mas quem pesquisa no celular ainda não encontra uma vitrine digital oficial da empresa.\n"
            f"Posso te mandar um exemplo rápido de como estruturamos isso aqui no bairro em 5 dias?"
        )

with open(path, 'w', encoding='utf-8') as f:
    json.dump(leads, f, indent=2, ensure_ascii=False)

# Também salva em MAQUINA_PROSPECCAO_1ST_TOUCH
dest2 = 'c:/Vocação 2027/MAQUINA_PROSPECCAO_1ST_TOUCH/03_MOTORES_PYTHON/data/leads_100_santa_rosalia_brasilandia.json'
with open(dest2, 'w', encoding='utf-8') as f:
    json.dump(leads, f, indent=2, ensure_ascii=False)

print("Ganchos humanizados e condicionados atualizados com sucesso para todos os 109 leads!")
print(f"Exemplo Studio Espaço Pilates (SEM site):\n{leads[1]['hook_a']}\n")
print(f"Exemplo Equilíbrio Saúde (COM site):\n{leads[0]['hook_a']}")
