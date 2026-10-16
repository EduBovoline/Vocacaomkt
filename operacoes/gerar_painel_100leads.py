import os
import sys
import json
import urllib.request
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')


TYPESAFE_API_KEY = os.environ.get(
    "TYPESAFE_API_KEY",
    "apikey_278f4d2c99533a740b5bf6020382067c3ac_b34e23a969f2da90dbbf1e2c838fd90b5be744be8f333c43bce904635c26c40c"
)
TYPESAFE_URL = "https://api.typesafe.ai/v1/systemone"

OFFER_PRICES = {
    "vocacao_start_850": {"name": "Vocação Start (Maps + Vitrine One-Page)", "price": 850.0, "micros": 850000000},
    "vocacao_update_980": {"name": "Vocação Update (Reforma Mobile-First)", "price": 980.0, "micros": 980000000},
    "combo_maps_tour360_950": {"name": "Combo Maps + Tour 360° GoPro Max", "price": 950.0, "micros": 950000000},
    "vocacao_maps_450": {"name": "Vocação Presença no Maps (Blindagem)", "price": 450.0, "micros": 450000000}
}

LEADS_RAW = [
    # ==================== SANTA ROSÁLIA (60 LEADS) ====================
    # Odonto & Saúde (15)
    {"name": "Silvério Odontologia", "bairro": "Santa Rosália", "cat": "Odontologia", "addr": "Av. Pereira da Silva, 169", "phone": "551530165548", "presence": "Maps básico sem fotos 360, site antigo"},
    {"name": "Orodent Unidade Santa Rosália", "bairro": "Santa Rosália", "cat": "Odontologia", "addr": "Av. Pereira da Silva, 1631", "phone": "551533571363", "presence": "Site institucional nacional, sem vitrine local direta"},
    {"name": "Clínica Russo Odontologia", "bairro": "Santa Rosália", "cat": "Odontologia", "addr": "Av. Pereira da Silva, 127", "phone": "551532331516", "presence": "Ficha no Maps antiga sem WhatsApp direto"},
    {"name": "Dr. Gaspar Martins da Silva", "bairro": "Santa Rosália", "cat": "Odontologia", "addr": "Av. Pereira da Silva, 1175", "phone": "551532310205", "presence": "Apenas telefone fixo no Maps, sem site"},
    {"name": "RP Prime Odontologia", "bairro": "Santa Rosália", "cat": "Odontologia", "addr": "Av. Pereira da Silva, 56", "phone": "551530111204", "presence": "Instagram ativo mas sem página rápida de agendamento"},
    {"name": "Clínica Vanessa Nogueira Emagrecimento", "bairro": "Santa Rosália", "cat": "Saúde & Estética", "addr": "Av. Pereira da Silva, 1099", "phone": "551530313394", "presence": "Site lento, sem tour virtual da clínica"},
    {"name": "Clínica Equilíbrio Saúde", "bairro": "Santa Rosália", "cat": "Saúde Multidisciplinar", "addr": "Av. Pereira da Silva, 828", "phone": "551532348890", "presence": "Maps não reivindicado, informações desatualizadas"},
    {"name": "Clínica LES Medicina e Reabilitação", "bairro": "Santa Rosália", "cat": "Clínica Médica", "addr": "R. Maria Cinto de Biaggi, 125", "phone": "551532335772", "presence": "Ambiente médico de alto padrão, sem Tour 360 no Street View"},
    {"name": "CeiPre Saúde & Fisioterapia", "bairro": "Santa Rosália", "cat": "Fisioterapia & Saúde", "addr": "R. João dos Santos, 600", "phone": "551534188848", "presence": "Ficha boa no Maps mas sem vitrine mobile própria"},
    {"name": "Fisio Santa Rosália", "bairro": "Santa Rosália", "cat": "Fisioterapia", "addr": "R. Rev. Henrique de Oliveira Camargo, 411", "phone": "551532321450", "presence": "Sem site, depende só de indicações e telefone"},
    {"name": "Consultório Pediátrico Santa Rosália", "bairro": "Santa Rosália", "cat": "Pediatria", "addr": "R. Mascarenhas Camelo, 310", "phone": "551532314560", "presence": "Maps básico sem agendamento facilitado"},
    {"name": "Clínica de Psicologia & Terapias Rosália", "bairro": "Santa Rosália", "cat": "Psicologia", "addr": "R. Nicolau Alonso Filho, 88", "phone": "5515998124010", "presence": "Apenas perfil em diretórios genéricos"},
    {"name": "Espaço Reab Postural & RPG", "bairro": "Santa Rosália", "cat": "Fisioterapia", "addr": "Av. Pereira da Silva, 430", "phone": "5515997812030", "presence": "Instagram ativo sem link direto estruturado"},
    {"name": "Consultório de Fonoaudiologia Integrada", "bairro": "Santa Rosália", "cat": "Fonoaudiologia", "addr": "R. Mascarenhas Camelo, 190", "phone": "551532349010", "presence": "Sem presença digital estruturada no Google"},
    {"name": "Clínica Dermatológica Dra. Paula", "bairro": "Santa Rosália", "cat": "Dermatologia", "addr": "Av. Pereira da Silva, 920", "phone": "5515996145520", "presence": "Alta procura local, sem vitrine com botão WhatsApp"},

    # Pilates & Movimento (10)
    {"name": "Clínica Paes Pilates & Fisio", "bairro": "Santa Rosália", "cat": "Pilates", "addr": "Av. Pereira da Silva, 164", "phone": "5515991767971", "presence": "Aparelhos modernos sem fotos 360 no Maps"},
    {"name": "Sem Limites Studio Pilates", "bairro": "Santa Rosália", "cat": "Pilates", "addr": "R. Nicolau Alonso Filho, 215", "phone": "5515997230411", "presence": "Ficha no Maps sem avaliações organizadas"},
    {"name": "Pure Pilates Santa Rosália", "bairro": "Santa Rosália", "cat": "Pilates", "addr": "R. Maria Cinto de Biaggi, 80", "phone": "5515998104400", "presence": "Franquia forte, sem personalização regional"},
    {"name": "Studio Corpo & Mente Pilates", "bairro": "Santa Rosália", "cat": "Pilates", "addr": "R. Mascarenhas Camelo, 450", "phone": "5515991442100", "presence": "Sem site independente, perfil no Insta com pouca bio"},
    {"name": "Espaço Movimento Pilates Clássico", "bairro": "Santa Rosália", "cat": "Pilates", "addr": "Av. Pereira da Silva, 780", "phone": "5515981223300", "presence": "Metodologia clássica sem destaque visual no Maps"},
    {"name": "Studio Vital Pilates & Yoga", "bairro": "Santa Rosália", "cat": "Pilates & Yoga", "addr": "R. João dos Santos, 320", "phone": "5515996551200", "presence": "Local agradável sem tour virtual no Street View"},
    {"name": "Instituto Postura & Movimento", "bairro": "Santa Rosália", "cat": "Pilates Clínico", "addr": "Av. Pereira da Silva, 1420", "phone": "5515997334411", "presence": "Falta vitrine rápida de triagem de alunos particulares"},
    {"name": "Studio Funcional Rosália Fitness", "bairro": "Santa Rosália", "cat": "Treino Funcional", "addr": "R. Mascarenhas Camelo, 580", "phone": "5515991887722", "presence": "Público do bairro não acha planos de treino no Google"},
    {"name": "Personal Studio Santa Rosália", "bairro": "Santa Rosália", "cat": "Personal Trainer", "addr": "R. Nicolau Alonso Filho, 310", "phone": "5515997116633", "presence": "Atendimento exclusivo sem vitrine profissional"},
    {"name": "Espaço Zen Terapias & Pilates", "bairro": "Santa Rosália", "cat": "Pilates & Terapias", "addr": "R. Ramos de Azevedo, 140", "phone": "5515981559944", "presence": "Presença dispersa no Maps"},

    # Estética & Beleza (10)
    {"name": "Dra. Cauane Guelfi Estética Avançada", "bairro": "Santa Rosália", "cat": "Estética Avançada", "addr": "R. Rev. Henrique de Oliveira Camargo, 120", "phone": "5515996411220", "presence": "Harmonização e tratamentos sem vitrine de autoridade"},
    {"name": "Rô Ferreira Estética", "bairro": "Santa Rosália", "cat": "Estética Facial", "addr": "Av. Pereira da Silva, 1953, Sl 4", "phone": "5515991166474", "presence": "Atendimento excelente sem ficha blindada no Maps"},
    {"name": "Studio D'Elas Salão & Estética", "bairro": "Santa Rosália", "cat": "Salão & Estética", "addr": "Av. Pereira da Silva, 610", "phone": "551532338900", "presence": "Grande movimento físico sem botão ágil no WhatsApp"},
    {"name": "Espaço Bella Donna Santa Rosália", "bairro": "Santa Rosália", "cat": "Estética Corporal", "addr": "R. Mascarenhas Camelo, 270", "phone": "5515997443322", "presence": "Sem site rápido mobile-first"},
    {"name": "Laser Care Depilação & Estética", "bairro": "Santa Rosália", "cat": "Estética a Laser", "addr": "Av. Pereira da Silva, 1250", "phone": "551530334410", "presence": "Concorrentes de shopping atraem clientes por falta de anúncios"},
    {"name": "Barbearia Tradicional Santa Rosália", "bairro": "Santa Rosália", "cat": "Barbearia", "addr": "Av. Pereira da Silva, 810", "phone": "5515991228899", "presence": "Espaço charmoso sem tour 360 no Street View"},
    {"name": "Ateliê da Beleza & Sobrancelhas", "bairro": "Santa Rosália", "cat": "Micropigmentação", "addr": "R. Nicolau Alonso Filho, 115", "phone": "5515998337711", "presence": "Apenas Instagram sem funil de conversão"},
    {"name": "Clínica de Estética Silhouette", "bairro": "Santa Rosália", "cat": "Estética Avançada", "addr": "Av. Pereira da Silva, 1540", "phone": "5515996225544", "presence": "Fotos do Maps com baixa resolução"},
    {"name": "Espaço Homem Barbearia & Estética", "bairro": "Santa Rosália", "cat": "Barbearia Masculina", "addr": "R. Maria Cinto de Biaggi, 190", "phone": "551532114400", "presence": "Sem integração com WhatsApp no Google Maps"},
    {"name": "Studio Nails & Beauty Santa Rosália", "bairro": "Santa Rosália", "cat": "Unhas & Beleza", "addr": "R. Mascarenhas Camelo, 125", "phone": "5515997661188", "presence": "Depende apenas de WhatsApp boca a boca"},

    # Pet Centers & Veterinárias (8)
    {"name": "Vet Care Saúde Animal", "bairro": "Santa Rosália", "cat": "Clínica Veterinária", "addr": "Av. Pereira da Silva, 68", "phone": "5515981722170", "presence": "Clínica completa sem página web rápida de plantão"},
    {"name": "Deniane Almeida Fisiovet", "bairro": "Santa Rosália", "cat": "Reabilitação Veterinária", "addr": "Av. Pereira da Silva, 68", "phone": "5515996841434", "presence": "Nicho de altíssimo valor sem vitrine dedicada"},
    {"name": "BastVet Centro Veterinário", "bairro": "Santa Rosália", "cat": "Hospital Veterinário", "addr": "R. José Del Ben, 140", "phone": "551532328811", "presence": "Estrutura grande sem tour 360 no Street View"},
    {"name": "Pet Shop & Clínica Santa Rosália", "bairro": "Santa Rosália", "cat": "Pet Shop & Banho", "addr": "Av. Pereira da Silva, 940", "phone": "551532345566", "presence": "Bairro de condomínios sem catálogo online de serviços"},
    {"name": "Boutique Animal Estética Pet", "bairro": "Santa Rosália", "cat": "Estética Pet", "addr": "R. Nicolau Alonso Filho, 420", "phone": "5515991332211", "presence": "Atendimento carinhoso sem presença forte no Google"},
    {"name": "Consultório Veterinário Dr. Marcelo", "bairro": "Santa Rosália", "cat": "Veterinária", "addr": "R. Mascarenhas Camelo, 380", "phone": "551532317788", "presence": "Sem vitrine de serviços preventivos e vacinas"},
    {"name": "Amigo dos Bichos Pet Shop", "bairro": "Santa Rosália", "cat": "Pet Shop", "addr": "Av. Pereira da Silva, 1340", "phone": "5515997448822", "presence": "Falta botão direto para WhatsApp de busca rápida"},
    {"name": "Espaço Pet Spa & Hotelzinho", "bairro": "Santa Rosália", "cat": "Hotel Pet", "addr": "R. Ramos de Azevedo, 210", "phone": "5515981446655", "presence": "Serviço premium de diárias sem página com fotos 360"},

    # Gastronomia & Cafés Conceito (9)
    {"name": "Izakaya Tsuchi Gastronomia Japonesa", "bairro": "Santa Rosália", "cat": "Gastronomia", "addr": "Av. Pereira da Silva, 1867", "phone": "551532114258", "presence": "Restaurante conceituado sem Tour 360 no Google Maps"},
    {"name": "Café com Gato Sorocaba", "bairro": "Santa Rosália", "cat": "Cafeteria Conceito", "addr": "Av. Pereira da Silva, 866", "phone": "551533260658", "presence": "Ponto turístico da cidade sem vitrine de reservas direta"},
    {"name": "Di Garden Restaurante & Eventos", "bairro": "Santa Rosália", "cat": "Restaurante", "addr": "Av. Pereira da Silva, 272", "phone": "551532323152", "presence": "Jardim lindíssimo sem fotos 360 no Street View"},
    {"name": "Cão Véio Sorocaba Gastropub", "bairro": "Santa Rosália", "cat": "Gastropub", "addr": "Av. Pereira da Silva, 1919", "phone": "551530335500", "presence": "Marca de renome com cardápio online lento no celular"},
    {"name": "Bistrô da Praça Santa Rosália", "bairro": "Santa Rosália", "cat": "Bistrô", "addr": "Praça Pio XII, 45", "phone": "551532349911", "presence": "Ambiente acolhedor sem presença otimizada no Maps"},
    {"name": "Forneria & Pizzaria Santa Rosália", "bairro": "Santa Rosália", "cat": "Pizzaria Artesanal", "addr": "Av. Pereira da Silva, 1120", "phone": "551532337744", "presence": "Delivery concorrido sem landing page própria de cardápio"},
    {"name": "Empório Gourmet Santa Rosália", "bairro": "Santa Rosália", "cat": "Empório & Vinhos", "addr": "Av. Pereira da Silva, 640", "phone": "5515998221144", "presence": "Produtos selecionados sem catálogo rápido para WhatsApp"},
    {"name": "Doce Encanto Confeitaria Fina", "bairro": "Santa Rosália", "cat": "Confeitaria", "addr": "R. Mascarenhas Camelo, 150", "phone": "5515991554433", "presence": "Bolos e festas sem canal de orçamento direto"},
    {"name": "Choperia & Espetaria Santa Rosália", "bairro": "Santa Rosália", "cat": "Bar & Gastronomia", "addr": "Av. Pereira da Silva, 1720", "phone": "5515997339900", "presence": "Movimentado à noite sem Google Maps otimizado"},

    # Automotivo, Serviços & Educação (8)
    {"name": "Motory Locadora & Veículos", "bairro": "Santa Rosália", "cat": "Locadora de Carros", "addr": "Av. Pereira da Silva, 1312", "phone": "551532323002", "presence": "Falta vitrine rápida de reservas para Sorocaba"},
    {"name": "Posto CIC Santa Rosália & Conveniência", "bairro": "Santa Rosália", "cat": "Posto & Serviços", "addr": "Av. Pereira da Silva, 557", "phone": "551532344782", "presence": "Ponto de alto fluxo sem blindagem de ficha no Maps"},
    {"name": "Centro Automotivo Pereira da Silva", "bairro": "Santa Rosália", "cat": "Oficina Mecânica", "addr": "Av. Pereira da Silva, 480", "phone": "551532336622", "presence": "Oficina de confiança sem avaliações ativas no Google"},
    {"name": "Santa Rosália Pneus & Alinhamento", "bairro": "Santa Rosália", "cat": "Auto Center", "addr": "Av. Pereira da Silva, 1490", "phone": "551532318844", "presence": "Perdendo orçamentos para grandes redes por falta de site"},
    {"name": "Colégio Cristão Almeida Barros", "bairro": "Santa Rosália", "cat": "Educação / Escola", "addr": "R. Aparecida, 780", "phone": "551532326090", "presence": "Escola tradicional sem Tour Virtual 360 das salas e quadras"},
    {"name": "Escola de Música Notas de Ouro", "bairro": "Santa Rosália", "cat": "Escola de Música", "addr": "R. Mascarenhas Camelo, 210", "phone": "5515996118833", "presence": "Cursos presenciais sem vitrine de matrícula ágil"},
    {"name": "Escola de Idiomas Santa Rosália", "bairro": "Santa Rosália", "cat": "Idiomas", "addr": "Av. Pereira da Silva, 1020", "phone": "551532341122", "presence": "Sem campanhas locais segmentadas para o bairro"},
    {"name": "Lavanderia Express Santa Rosália", "bairro": "Santa Rosália", "cat": "Lavanderia", "addr": "R. Maria Cinto de Biaggi, 230", "phone": "5515997224488", "presence": "Excelente serviço sem botão direto no Google Maps"},

    # ==================== JARDIM BRASILÂNDIA (40 LEADS) ====================
    # Odonto & Saúde (8)
    {"name": "Brasilândia Odontologia Especializada", "bairro": "Jardim Brasilândia", "cat": "Odontologia", "addr": "Av. Brasil, 420", "phone": "551532314411", "presence": "Atendimento da família do bairro sem site mobile"},
    {"name": "Clínica Dr. Marcos Dental", "bairro": "Jardim Brasilândia", "cat": "Odontologia", "addr": "R. Maciel Vaz, 180", "phone": "5515997123344", "presence": "Ficha no Maps com fotos antigas"},
    {"name": "Dra. Camila Odontologia e Estética", "bairro": "Jardim Brasilândia", "cat": "Odontologia", "addr": "R. Olavo Bilac, 95", "phone": "5515991448855", "presence": "Apenas WhatsApp de agendamento sem vitrine"},
    {"name": "Fisioterapia Integrada Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Fisioterapia", "addr": "Av. Brasil, 780", "phone": "551532341290", "presence": "Sem site próprio, perda de pacientes da Zona Norte"},
    {"name": "Consultório de Psicologia & Família", "bairro": "Jardim Brasilândia", "cat": "Psicologia", "addr": "R. Castanho Taques, 110", "phone": "5515981336622", "presence": "Invisível nas pesquisas do Google"},
    {"name": "Clínica Médica Popular Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Clínica Médica", "addr": "Av. Brasil, 1150", "phone": "551532338877", "presence": "Grande demanda sem vitrine de especialidades"},
    {"name": "Laboratório & Coleta Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Análises Clínicas", "addr": "R. Bartolomeu de Gusmão, 140", "phone": "551532327700", "presence": "Falta agendamento de exames simplificado"},
    {"name": "Espaço Saúde & Podologia Brasil", "bairro": "Jardim Brasilândia", "cat": "Podologia & Cuidados", "addr": "R. Maciel Vaz, 310", "phone": "5515996554411", "presence": "Sem ficha de Google Maps verificada"},

    # Estética, Salões & Beleza (8)
    {"name": "Studio Vip Brasilândia Beleza", "bairro": "Jardim Brasilândia", "cat": "Salão de Beleza", "addr": "Av. Brasil, 560", "phone": "5515997331199", "presence": "Salão com clientela fiel sem presença web"},
    {"name": "Espaço Divas Cabelo & Estética", "bairro": "Jardim Brasilândia", "cat": "Estética & Cabelo", "addr": "R. Olavo Bilac, 240", "phone": "5515991225588", "presence": "Fotos de trabalhos só no Instagram sem vitrine"},
    {"name": "Barbearia Tradicional Brasil", "bairro": "Jardim Brasilândia", "cat": "Barbearia", "addr": "Av. Brasil, 890", "phone": "5515981447733", "presence": "Falta botão direto para agendamento no WhatsApp"},
    {"name": "Salão Bela Imagem Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Cabeleireiro", "addr": "R. Maciel Vaz, 420", "phone": "551532349900", "presence": "Maps desatualizado sem horário de funcionamento"},
    {"name": "Espaço Estética & Sobrancelhas Mary", "bairro": "Jardim Brasilândia", "cat": "Estética Facial", "addr": "R. Castanho Taques, 220", "phone": "5515996113377", "presence": "Depende unicamente do boca a boca"},
    {"name": "Barbearia Black & Gold Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Barbearia Moderna", "addr": "Av. Brasil, 1320", "phone": "5515997886644", "presence": "Excelente decoração sem tour virtual 360 no Maps"},
    {"name": "Studio Nails Brasilândia Unhas", "bairro": "Jardim Brasilândia", "cat": "Manicure & Nails", "addr": "R. Bartolomeu de Gusmão, 80", "phone": "5515991669922", "presence": "Sem posicionamento no Google Maps"},
    {"name": "Clínica de Massoterapia & Relaxamento", "bairro": "Jardim Brasilândia", "cat": "Massoterapia", "addr": "R. Rodrigues Alves, 190", "phone": "5515981224400", "presence": "Pacientes de dores musculares não encontram o espaço"},

    # Automotivo, Oficinas & Peças (8)
    {"name": "Auto Center Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Oficina Mecânica", "addr": "Av. Brasil, 310", "phone": "551532328844", "presence": "Mecânica tradicional sem site e com ficha básica"},
    {"name": "Mecânica e Injeção Sorocaba Norte", "bairro": "Jardim Brasilândia", "cat": "Injeção Eletrônica", "addr": "R. Maciel Vaz, 540", "phone": "551532339911", "presence": "Especialistas sem canal rápido de socorro/WhatsApp"},
    {"name": "Oficina Brasil Car Funilaria", "bairro": "Jardim Brasilândia", "cat": "Funilaria & Pintura", "addr": "Av. Brasil, 980", "phone": "551532317733", "presence": "Perdendo clientes segurados por falta de vitrine"},
    {"name": "Moto Peças & Oficina Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Motopeças", "addr": "R. Olavo Bilac, 380", "phone": "5515997226611", "presence": "Grande movimento sem catálogo de peças online"},
    {"name": "Pneus & Alinhamento Brasil", "bairro": "Jardim Brasilândia", "cat": "Auto Center", "addr": "Av. Brasil, 1450", "phone": "551532345511", "presence": "Maps não blindado, falta WhatsApp direto"},
    {"name": "Auto Elétrica & Baterias Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Auto Elétrica", "addr": "R. Castanho Taques, 340", "phone": "5515991557788", "presence": "Serviço de socorro de bateria invisível na busca móvel"},
    {"name": "Ar Condicionado Automotivo Norte", "bairro": "Jardim Brasilândia", "cat": "Climatização Auto", "addr": "R. Bartolomeu de Gusmão, 250", "phone": "5515981338899", "presence": "Forte no verão sem campanhas ativas no Maps"},
    {"name": "Lava Rápido & Estética Automotiva Brasil", "bairro": "Jardim Brasilândia", "cat": "Estética Automotiva", "addr": "Av. Brasil, 710", "phone": "5515996442200", "presence": "Serviços de polimento sem fotos profissionais no Google"},

    # Pet & Agro (4)
    {"name": "Pet Shop Brasil & Veterinária", "bairro": "Jardim Brasilândia", "cat": "Pet Shop", "addr": "Av. Brasil, 640", "phone": "551532334499", "presence": "Banho e tosa concorrido sem agendamento no celular"},
    {"name": "Agropecuária & Rações Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Agropecuária", "addr": "R. Maciel Vaz, 210", "phone": "551532316622", "presence": "Comércio forte sem WhatsApp no Google Maps"},
    {"name": "Amigo Fiel Banho e Tosa", "bairro": "Jardim Brasilândia", "cat": "Banho & Tosa", "addr": "R. Olavo Bilac, 410", "phone": "5515997118833", "presence": "Sem site ou página rápida de planos mensais"},
    {"name": "Consultório Veterinário Brasil Animal", "bairro": "Jardim Brasilândia", "cat": "Veterinária", "addr": "Av. Brasil, 1200", "phone": "5515998335522", "presence": "Vacinas e consultas sem vitrine de atendimento"},

    # Alimentação & Comércio (6)
    {"name": "Padaria & Confeitaria Pão Brasil", "bairro": "Jardim Brasilândia", "cat": "Padaria", "addr": "Av. Brasil, 510", "phone": "551532321188", "presence": "Ponto tradicional sem fotos 360 no Street View"},
    {"name": "Restaurante & Marmitaria Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Restaurante", "addr": "R. Maciel Vaz, 120", "phone": "551532347744", "presence": "Marmitas para empresas da ZN sem cardápio online ágil"},
    {"name": "Pizzaria Forno Nobre Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Pizzaria", "addr": "Av. Brasil, 1050", "phone": "551532335566", "presence": "Delivery concorrido com site pesado e lento"},
    {"name": "Pastelaria & Lanchonete do Bairro", "bairro": "Jardim Brasilândia", "cat": "Lanchonete", "addr": "R. Olavo Bilac, 180", "phone": "5515991443311", "presence": "Sem ficha de Google Maps estruturada"},
    {"name": "Açougue & Casa de Carnes Brasil", "bairro": "Jardim Brasilândia", "cat": "Casa de Carnes", "addr": "Av. Brasil, 820", "phone": "551532319944", "presence": "Carnes nobres sem catálogo para pedidos pelo WhatsApp"},
    {"name": "Drogaria & Farmácia Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Farmácia", "addr": "Av. Brasil, 390", "phone": "551532324400", "presence": "Falta botão de tele-entrega direta na ficha do Maps"},

    # Serviços & Marcenaria / Manutenção (6)
    {"name": "Marcenaria Brasil Móveis Planejados", "bairro": "Jardim Brasilândia", "cat": "Marcenaria", "addr": "R. Bartolomeu de Gusmão, 320", "phone": "5515997558811", "presence": "Fábrica própria sem portfólio digital moderno"},
    {"name": "Serralheria & Estruturas Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Serralheria", "addr": "R. Maciel Vaz, 610", "phone": "5515991884422", "presence": "Sem presença na internet, apenas telefone local"},
    {"name": "Vidraçaria & Box Brasil Norte", "bairro": "Jardim Brasilândia", "cat": "Vidraçaria", "addr": "Av. Brasil, 1280", "phone": "551532346611", "presence": "Perdendo obras e reformas residenciais no Google"},
    {"name": "Elétrica & Hidráulica Brasil Materiais", "bairro": "Jardim Brasilândia", "cat": "Materiais Elétricos", "addr": "R. Castanho Taques, 450", "phone": "551532331155", "presence": "Sem catálogo no WhatsApp ou Maps blindado"},
    {"name": "Gráfica Rápida & Comunicação Brasilândia", "bairro": "Jardim Brasilândia", "cat": "Gráfica", "addr": "R. Olavo Bilac, 520", "phone": "5515996227700", "presence": "Falta página rápida para envio de arquivos de impressão"},
    {"name": "Assistência Técnica de Celulares & Informática", "bairro": "Jardim Brasilândia", "cat": "Informática", "addr": "Av. Brasil, 670", "phone": "5515981552233", "presence": "Alta busca de conserto sem site com botão de socorro"}
]

def qualify_lead_rules_jev(lead):
    name = lead["name"]
    bairro = lead["bairro"]
    cat = lead["cat"]
    presence = lead["presence"]

    # Critérios calibrados Jev System One
    if any(k in cat.lower() for k in ["pilates", "restaurante", "cafeteria", "bistrô", "gastronomia", "gastropub", "escola", "clínica médica", "hospital"]):
        oferta_key = "combo_maps_tour360_950"
        urgencia = 2 if "sem tour" in presence.lower() or "não encontra" in presence.lower() else 1
        perda = 0.85
        perfil = "espaco_ambiente"
    elif any(k in cat.lower() for k in ["odontologia", "estética", "fisioterapia", "veterinária", "pediatria", "psicologia"]):
        if "site antigo" in presence.lower() or "lento" in presence.lower():
            oferta_key = "vocacao_update_980"
            urgencia = 2
            perda = 0.80
            perfil = "site_legado"
        else:
            oferta_key = "vocacao_start_850"
            urgencia = 2
            perda = 0.88
            perfil = "sem_presenca"
    elif any(k in cat.lower() for k in ["oficina", "auto center", "funilaria", "motopeças", "auto elétrica", "serralheria", "vidraçaria", "marcenaria"]):
        oferta_key = "vocacao_start_850"
        urgencia = 2 if "invisível" in presence.lower() or "sem site" in presence.lower() else 1
        perda = 0.78
        perfil = "sem_presenca"
    else:
        oferta_key = "vocacao_maps_450"
        urgencia = 1
        perda = 0.65
        perfil = "regularizacao_maps"

    oferta_meta = OFFER_PRICES[oferta_key]

    # Gera Hook persuasivo de acordo com o bairro real
    if "360" in oferta_key:
        hook = (
            f"Olá! Analisei a presença digital de vocês no bairro {bairro} e notei algo importante: "
            f"o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue "
            f"fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. "
            f"Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas?"
        )
    elif "update" in oferta_key:
        hook = (
            f"Olá! Analisei a presença digital da empresa no bairro {bairro} e vi que vocês já possuem um site estabelecido, "
            f"mas o carregamento no celular pode estar fazendo vocês perderem clientes para concorrentes locais. "
            f"Posso te enviar um diagnóstico visual de 2 minutos mostrando como acelerar a conversão da página?"
        )
    elif "maps" in oferta_key:
        hook = (
            f"Olá! Analisei a ficha de vocês no Google Maps no {bairro} e notei oportunidades para blindar o perfil contra concorrentes "
            f"e facilitar o contato direto pelo WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos sobre isso?"
        )
    else:
        hook = (
            f"Olá! Analisei a presença digital de vocês no {bairro} e notei que quem pesquisa pelos seus serviços no Google "
            f"encontra pouca informação institucional independente antes de chamar no WhatsApp. "
            f"Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região?"
        )

    # Adiciona conformidade LGPD
    hook += " (Se preferir não receber mensagens comerciais, responda PARAR)."

    return {
        **lead,
        "oferta_key": oferta_key,
        "oferta_nome": oferta_meta["name"],
        "oferta_preco": oferta_meta["price"],
        "oferta_micros": oferta_meta["micros"],
        "oferta_confianca": 0.88,
        "perfil_maturidade": perfil,
        "perda_conversao_local": perda,
        "urgencia_score": urgencia,
        "hook_whatsapp": hook
    }

def main():
    print(f"[*] Processando e qualificando {len(LEADS_RAW)} leads com Jev System One...")
    qualified = []
    for lead in LEADS_RAW:
        q = qualify_lead_rules_jev(lead)
        qualified.append(q)

    json_path = r"C:\Vocação 2027\QG Vocação 2027 do zero\leads_100_santa_rosalia_brasilandia.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(qualified, f, indent=2, ensure_ascii=False)
    print(f"[✓] Arquivo JSON gerado: {json_path}")

    # Estatísticas
    total_sr = sum(1 for l in qualified if l["bairro"] == "Santa Rosália")
    total_br = sum(1 for l in qualified if l["bairro"] == "Jardim Brasilândia")
    criticos = sum(1 for l in qualified if l["urgencia_score"] == 2)
    start_count = sum(1 for l in qualified if l["oferta_key"] == "vocacao_start_850")
    tour_count = sum(1 for l in qualified if l["oferta_key"] == "combo_maps_tour360_950")
    update_count = sum(1 for l in qualified if l["oferta_key"] == "vocacao_update_980")
    maps_count = sum(1 for l in qualified if l["oferta_key"] == "vocacao_maps_450")

    print(f"    • Santa Rosália: {total_sr}")
    print(f"    • Jardim Brasilândia: {total_br}")
    print(f"    • Urgência Crítica: {criticos}")
    print(f"    • Ofertas: Start ({start_count}), Tour 360° ({tour_count}), Update ({update_count}), Maps ({maps_count})")

if __name__ == "__main__":
    main()
