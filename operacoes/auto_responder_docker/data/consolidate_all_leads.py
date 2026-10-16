import json
import re
import urllib.parse

# 1. Carrega os 100 leads originais
seed_path = 'c:/Vocação 2027/MAQUINA_PROSPECCAO_1ST_TOUCH/05_BANCO_DADOS_SEEDS/leads_100_santa_rosalia_brasilandia.json'
with open(seed_path, 'r', encoding='utf-8') as f:
    seed_leads = json.load(f)

# 2. Carrega os leads reais verificados de hoje
real_verified_path = 'auto_responder_docker/data/build_real_leads.py'
# Vamos definir os leads novos e consolidados:
novos_reais = [
    {
        "id": "sr_real_01",
        "name": "Equilíbrio Saúde - Medicina Integrada",
        "category": "santa_rosalia",
        "segment": "Clínica Médica & Especialidades",
        "bairro": "Santa Rosália",
        "address": "Av. Pereira da Silva, 828, Sorocaba - SP",
        "phone": "5515992883434",
        "site": "https://equilibriosaude.med.br",
        "gargalo": "Ficha no Maps com alta busca mas sem agendamento mobile direto integrado ao WhatsApp da recepção",
        "ticket": "R$ 3.500 - R$ 12.000",
        "priority": "Alta",
        "jev_oferta": "Vocação Update (Reforma Mobile-First)",
        "jev_urgencia": 2,
        "hook_a": "Olá! Sou o Eduardo, da Vocação aqui de Santa Rosália (pertinho de vocês na Pereira da Silva). Vi o trabalho de excelência da Equilíbrio Saúde, mas notei que quem pesquisa pelas especialidades no Google pelo celular não encontra uma vitrine de agendamento ágil. Posso te enviar um diagnóstico visual de 2 minutos mostrando como transformar buscas locais em consultas? (Se preferir não receber, responda PARAR).",
        "hook_b": "Olá equipe da Equilíbrio Saúde! Aqui é o Eduardo, vizinho de vocês em Santa Rosália. Fiz uma análise da presença mobile de clínicas na Pereira da Silva e vi uma oportunidade rápida de posicionamento no Google Maps. Podemos alinhar um resumo de 2 minutos?"
    },
    {
        "id": "sr_real_02",
        "name": "Studio Espaço Pilates",
        "category": "santa_rosalia",
        "segment": "Pilates & Bem-Estar",
        "bairro": "Santa Rosália",
        "address": "Av. Pereira da Silva, 1163, Sorocaba - SP",
        "phone": "5515997118853",
        "site": "",
        "gargalo": "Ficha do Maps sem fotos 360 do studio e sem vitrine rápida de horários e planos no celular",
        "ticket": "R$ 1.800 - R$ 4.500",
        "priority": "Alta",
        "jev_oferta": "Vocação Update (Reforma Mobile-First)",
        "jev_urgencia": 2,
        "hook_a": "Olá! Sou o Eduardo, da Vocação aqui de Santa Rosália. Vi o Studio Espaço Pilates na Pereira da Silva e notei que quem busca aulas de pilates na nossa região acaba caindo em anúncios patrocinados antes de encontrar vocês. O meu trabalho aqui no bairro é estruturar a presença mobile no Maps. Posso te mandar uma prévia visual de 2 minutos?",
        "hook_b": "Oi pessoal do Studio Espaço Pilates! Como estão as turmas na Pereira da Silva? Notei que a ficha do Maps pode captar muito mais moradores do Santa Rosália que pesquisam no smartphone. Vale um áudio de 2 min?"
    },
    {
        "id": "sr_real_03",
        "name": "Maju Vitalis Centro Integrativo",
        "category": "santa_rosalia",
        "segment": "Terapias & Saúde Integrativa",
        "bairro": "Vila Santana / Santa Rosália",
        "address": "R. Mascarenhas Camelo, 945, Sorocaba - SP",
        "phone": "5515988204559",
        "site": "",
        "gargalo": "Ausência de página mobile rápida para apresentação de terapias integrativas e agendamento",
        "ticket": "R$ 2.000 - R$ 6.000",
        "priority": "Alta",
        "jev_oferta": "Vocação Update (Reforma Mobile-First)",
        "jev_urgencia": 2,
        "hook_a": "Olá! Sou o Eduardo, da Vocação aqui da região de Santa Rosália. Vi o espaço Maju Vitalis na Mascarenhas Camelo e achei o conceito excelente. Quem pesquisa por terapias integrativas em Sorocaba hoje decide em menos de 5 segundos no celular. Posso te enviar um diagnóstico de 2 minutos para fortalecer sua presença local?",
        "hook_b": "Olá equipe da Maju Vitalis! Sou o Eduardo, trabalho com autoridade digital aqui na região da Mascarenhas Camelo. Vi uma oportunidade de colocar seu espaço em destaque no Google Maps para atrair clientes do bairro. Podemos falar 2 minutos?"
    },
    {
        "id": "sr_real_04",
        "name": "FISIOMUV - Fisioterapia e Pilates",
        "category": "santa_rosalia",
        "segment": "Fisioterapia & Reabilitação",
        "bairro": "Santa Rosália",
        "address": "R. Prof. Daniel Paulo Verano Pontes, 220, Sorocaba - SP",
        "phone": "5515976039835",
        "site": "",
        "gargalo": "Presença no Maps com poucos destaques visuais e sem página mobile independente de captura",
        "ticket": "R$ 2.500 - R$ 8.000",
        "priority": "Alta",
        "jev_oferta": "Vocação Update (Reforma Mobile-First)",
        "jev_urgencia": 2,
        "hook_a": "Olá! Sou o Eduardo, da Vocação aqui de Santa Rosália. Conheço a região da Daniel Paulo Verano Pontes e notei que a FISIOMUV tem um atendimento impecável, mas quem pesquisa fisioterapia no Google Maps muitas vezes não vê a estrutura completa de primeira. Posso te mandar uma análise visual rápida de 2 min?",
        "hook_b": "Oi pessoal da FISIOMUV! Aqui é o Eduardo da Vocação, também de Santa Rosália. Notei um ponto cego na busca mobile do Maps para o segmento de fisioterapia no bairro. Vale conversarmos 2 minutinhos?"
    },
    {
        "id": "sr_real_06",
        "name": "Gold Outlet Premium",
        "category": "santa_rosalia",
        "segment": "Eletrônicos & Eletrodomésticos",
        "bairro": "Santa Rosália",
        "address": "R. Nicolau Alonso Filho, 51, Sorocaba - SP",
        "phone": "5515998629088",
        "site": "",
        "gargalo": "Loja com grande apelo visual no bairro mas dependente de posts sociais sem catálogo mobile indexado no Maps",
        "ticket": "R$ 2.000 - R$ 10.000",
        "priority": "Alta",
        "jev_oferta": "Vocação Update (Reforma Mobile-First)",
        "jev_urgencia": 2,
        "hook_a": "Olá! Sou o Eduardo, da Vocação aqui de Santa Rosália (pertinho de vocês na Nicolau Alonso Filho). Vi os produtos da Gold Outlet e reparei que vocês dependem quase que exclusivamente de redes sociais, enquanto quem busca ofertas no Google da nossa região não encontra um catálogo direto no Maps. Posso te enviar uma demonstração de 2 minutos?",
        "hook_b": "Oi pessoal da Gold Outlet! Como estão as vendas aqui na Nicolau Alonso Filho? Notei que um catálogo mobile indexado no Maps aceleraria muito os pedidos no WhatsApp. Vale batermos um papo rápido de 2 min?"
    },
    {
        "id": "sr_real_07",
        "name": "Fino Faro Pet Shop",
        "category": "santa_rosalia",
        "segment": "Pet Shop & Banho e Tosa",
        "bairro": "Santa Rosália",
        "address": "R. Aparecida, 1565, Sorocaba - SP",
        "phone": "5515996111325",
        "site": "https://finofarosorocaba.com.br",
        "gargalo": "Ficha do Maps sem destaque dos serviços de leva-e-traz e agendamento rápido de banho e tosa via celular",
        "ticket": "R$ 1.500 - R$ 4.000",
        "priority": "Média",
        "jev_oferta": "Vocação Update (Reforma Mobile-First)",
        "jev_urgencia": 1,
        "hook_a": "Olá! Sou o Eduardo, da Vocação aqui de Santa Rosália. Vi a Fino Faro na Rua Aparecida. Tutores da região costumam buscar banho e tosa no celular de última hora no Maps. Notamos um detalhe na presença mobile de vocês que pode aumentar os agendamentos semanais. Posso te mandar um diagnóstico de 2 minutos?",
        "hook_b": "Olá equipe da Fino Faro! Sou o Eduardo, moro aqui perto da Aparecida. Fiz um levantamento dos pet shops do bairro no Google Maps e identifiquei um ganho imediato de posicionamento para vocês. Podemos alinhar em 2 minutos?"
    },
    {
        "id": "sr_real_08",
        "name": "Restaurante Bella Parma",
        "category": "santa_rosalia",
        "segment": "Gastronomia & Delivery",
        "bairro": "Santa Rosália",
        "address": "Av. Pereira da Silva, 1752, Sorocaba - SP",
        "phone": "5515998461717",
        "site": "",
        "gargalo": "Cardápio e reservas no celular dependentes de PDF pesado; falta de página mobile-first veloz no Maps",
        "ticket": "R$ 2.500 - R$ 8.000",
        "priority": "Alta",
        "jev_oferta": "Vocação Update (Reforma Mobile-First)",
        "jev_urgencia": 2,
        "hook_a": "Olá! Sou o Eduardo, da Vocação aqui da Pereira da Silva. O Bella Parma é um clássico aqui em Santa Rosália, mas quem pesquisa pelo cardápio no celular muitas vezes tem dificuldade de ver as opções rápido antes de pedir no WhatsApp. Posso te mostrar um modelo de cardápio mobile veloz de 2 minutos?",
        "hook_b": "Olá equipe Bella Parma! Aqui é o Eduardo, vizinho de vocês na Pereira da Silva. Notei uma oportunidade de modernizar o acesso ao cardápio e reservas direto pelo Google Maps. Com quem posso falar sobre isso?"
    },
    {
        "id": "sr_real_09",
        "name": "Kikavest",
        "category": "santa_rosalia",
        "segment": "Moda & Vestuário",
        "bairro": "Vila Santana / Santa Rosália",
        "address": "R. Mascarenhas Camelo, 462, Sorocaba - SP",
        "phone": "5515996064556",
        "site": "https://kikavest.com.br",
        "gargalo": "Site com layout antigo sem otimização de conversão para atendimento rápido de lojista ou cliente final no WhatsApp",
        "ticket": "R$ 2.500 - R$ 7.000",
        "priority": "Média",
        "jev_oferta": "Vocação Update (Reforma Mobile-First)",
        "jev_urgencia": 1,
        "hook_a": "Olá! Sou o Eduardo, da Vocação aqui da região da Mascarenhas Camelo. Vi a tradição da Kikavest e reparei que quem visita o site pelo celular hoje encontra uma estrutura pesada. Podemos transformar sua vitrine numa experiência fluida de compra. Posso te enviar uma análise rápida de 2 minutos?",
        "hook_b": "Oi pessoal da Kikavest! Aqui é o Eduardo da Vocação. Fiz uma análise técnica do carregamento mobile do site de vocês no celular. Vale 2 minutinhos para vermos os pontos de melhoria?"
    },
    {
        "id": "sr_real_10",
        "name": "Mega Make Hair",
        "category": "santa_rosalia",
        "segment": "Salão de Beleza & Estética",
        "bairro": "Vila Santana / Santa Rosália",
        "address": "R. Mascarenhas Camelo, 690, Sorocaba - SP",
        "phone": "5515996937331",
        "site": "",
        "gargalo": "Atendimento restrito a direct e WhatsApp sem vitrine dos serviços de cabelo e make no Google",
        "ticket": "R$ 1.800 - R$ 5.000",
        "priority": "Alta",
        "jev_oferta": "Vocação Update (Reforma Mobile-First)",
        "jev_urgencia": 2,
        "hook_a": "Olá! Sou o Eduardo, da Vocação aqui de Santa Rosália/Vila Santana. Vi os trabalhos impecáveis da Mega Make Hair na Mascarenhas Camelo. No Google Maps, muitas clientes que procuram salão de beleza no bairro acabam não vendo a tabela e portfólio de vocês de imediato. Posso te mandar uma prévia de 2 minutos?",
        "hook_b": "Oi equipe da Mega Make Hair! Aqui é o Eduardo da Vocação. Notei como a presença de vocês no Maps da Mascarenhas Camelo pode atrair muito mais clientes de eventos e noivas do bairro. Vale conversarmos 2 min?"
    },
    {
        "id": "sr_real_11",
        "name": "Arteliê Artesanatos e Presentes",
        "category": "santa_rosalia",
        "segment": "Decoração & Artesanato",
        "bairro": "Vila Santana / Santa Rosália",
        "address": "R. Mascarenhas Camelo, 1133, Sorocaba - SP",
        "phone": "5515997915853",
        "site": "",
        "gargalo": "Falta de presença digital estruturada; negócio focado no balcão sem catálogo digital no Maps",
        "ticket": "R$ 1.500 - R$ 3.500",
        "priority": "Média",
        "jev_oferta": "Vocação Update (Reforma Mobile-First)",
        "jev_urgencia": 1,
        "hook_a": "Olá! Sou o Eduardo, da Vocação aqui da região da Mascarenhas Camelo. Vi a loja do Arteliê e acho o trabalho de vocês incrível. Hoje quem busca presentes criativos no bairro pesquisa no Maps antes de sair de casa. Posso te enviar uma ideia de 2 minutos para colocar seus produtos na vitrine digital?",
        "hook_b": "Olá pessoal do Arteliê! Aqui é o Eduardo, vizinho de vocês em Sorocaba. Vale vermos como atrair mais moradores da região para a loja através do Google Maps em 2 minutos?"
    }
]

def clean_query_term(text):
    # Remove pontuação excessiva que confunde o Google Maps
    text = re.sub(r'[,;.\-\/]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def build_perfect_maps_url(name, address, bairro="Santa Rosália"):
    # Extrai o nome limpo e a rua principal
    c_name = clean_query_term(name)
    c_addr = clean_query_term(address.split(',')[0] if ',' in address else address)
    # Ex: "Silvério Odontologia Av Pereira da Silva 169 Sorocaba"
    query = f"{c_name} {c_addr} Sorocaba".strip()
    # Usa o formato universal cross-platform que abre direto a ficha
    encoded = urllib.parse.quote_plus(query)
    return f"https://www.google.com/maps/search/?api=1&query={encoded}"

# Junta os novos reais com a lista seed de 100
all_leads_dict = {}

# Adiciona primeiro os novos reais
for l in novos_reais:
    l["category"] = "santa_rosalia"
    l["maps_url"] = build_perfect_maps_url(l["name"], l["address"], l.get("bairro", "Santa Rosália"))
    l["whatsapp_url"] = f"https://wa.me/{l['phone']}"
    l["instagram_search_url"] = f"https://www.google.com/search?q={urllib.parse.quote_plus(l['name'] + ' Sorocaba instagram')}"
    all_leads_dict[l["name"].lower().strip()] = l

# Adiciona os da lista seed garantindo:
# 1. Zero marcenarias
# 2. Maps URL 100% limpa e funcional
for l in seed_leads:
    name_clean = l.get("name", "").strip()
    seg = l.get("segment", "").lower()
    if "marcenaria" in seg or "marcenaria" in name_clean.lower():
        continue # REGRA: ZERO MARCENARIAS!
    
    k = name_clean.lower()
    if k not in all_leads_dict:
        l["category"] = "santa_rosalia"
        l["maps_url"] = build_perfect_maps_url(l["name"], l.get("address", ""), l.get("bairro", "Santa Rosália"))
        l["whatsapp_url"] = f"https://wa.me/{l.get('phone', '')}"
        l["instagram_search_url"] = f"https://www.google.com/search?q={urllib.parse.quote_plus(l['name'] + ' Sorocaba instagram')}"
        all_leads_dict[k] = l

final_list = list(all_leads_dict.values())

# Ordena: Celulares móveis (15 9...) no topo absoluto
def is_mobile(lead):
    clean = re.sub(r'\D', '', str(lead.get('phone', '')))
    return clean.startswith('55159') or (len(clean) == 11 and clean.startswith('159'))

mobiles = [l for l in final_list if is_mobile(l)]
landlines = [l for l in final_list if not is_mobile(l)]
sorted_final = mobiles + landlines

# Salva nos dois diretórios
dest1 = 'auto_responder_docker/data/leads_100_santa_rosalia_brasilandia.json'
with open(dest1, 'w', encoding='utf-8') as f:
    json.dump(sorted_final, f, indent=2, ensure_ascii=False)

dest2 = 'c:/Vocação 2027/MAQUINA_PROSPECCAO_1ST_TOUCH/03_MOTORES_PYTHON/data/leads_100_santa_rosalia_brasilandia.json'
with open(dest2, 'w', encoding='utf-8') as f:
    json.dump(sorted_final, f, indent=2, ensure_ascii=False)

print(f"Sucesso Total: {len(sorted_final)} leads salvos!")
print(f"- {len(mobiles)} celulares móveis no topo (15 9...)")
print(f"- {len(landlines)} telefones fixos ao final")
print(f"- Zero marcenarias.")
print(f"- Exemplo Maps URL 1: {sorted_final[0]['name']} -> {sorted_final[0]['maps_url']}")
print(f"- Exemplo Maps URL 2: {sorted_final[1]['name']} -> {sorted_final[1]['maps_url']}")
