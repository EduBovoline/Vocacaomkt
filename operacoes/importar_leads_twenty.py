import os
import re
import csv
import uuid
import subprocess
from datetime import datetime, timezone

SCHEMA = "workspace_2xmx8hech9nybwidia3404k2z"
ADMIN_MEMBER_ID = "1c0b8905-7e8f-4f50-90a1-6c67135bb381"
ADMIN_NAME = "EDUARDO BOVOLINE"

def escape_sql(val):
    if val is None:
        return "NULL"
    val_str = str(val).replace("'", "''").strip()
    return f"'{val_str}'"

def run_psql(sql_content):
    proc = subprocess.Popen(
        ["C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe", "exec", "-i", "twenty-db-1", "psql", "-U", "postgres", "-d", "twenty"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )
    stdout, stderr = proc.communicate(input=sql_content)
    if proc.returncode != 0:
        print("SQL Error:", stderr)
    return stdout

print("Iniciando limpeza de dados demo...")
cleanup_sql = f"""
DELETE FROM "{SCHEMA}"."opportunity" WHERE "createdBySource" = 'SYSTEM';
DELETE FROM "{SCHEMA}"."person" WHERE "createdBySource" = 'SYSTEM';
DELETE FROM "{SCHEMA}"."company" WHERE "createdBySource" = 'SYSTEM';
"""
run_psql(cleanup_sql)

companies = {} # key: normalized name -> dict

# 1. Base Especial: Clientes e Leads Diretos dos Dossiês
dossier_leads = [
    {
        "name": "Espaço Naturê",
        "contact_name": "Miriam",
        "phone": "(11) 99139-4281",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "espaconature.com.br",
        "stage": "CUSTOMER",
        "amount": 1500,
        "notes": "Cliente fechado em 08/09. Onboarding Estratégico + Reestruturação Google Maps."
    },
    {
        "name": "Safety First Engenharia",
        "contact_name": "Fabio",
        "phone": "(15) 99100-0000",
        "email": "contato@safetyfirst.eng.br",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "safetyfirst.eng.br",
        "stage": "CUSTOMER",
        "amount": 450,
        "notes": "Cliente pago (R$ 450). Site institucional pronto no GitHub, aguardando apontamento de domínio."
    },
    {
        "name": "Clínica Piacitelli",
        "contact_name": "Dr. Piacitelli",
        "phone": "",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "clinicapiacitelli.com.br",
        "stage": "MEETING",
        "amount": 1500,
        "notes": "Negociação ativa conduzida pelo Edu Bovoline. Odontologia e Estética."
    },
    {
        "name": "Magen Segurança Eletrônica",
        "contact_name": "Diretor Comercial",
        "phone": "(11) 94561-5331",
        "email": "contato@magenseguranca.com.br",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba e Região",
        "domain": "magenseguranca.com.br",
        "stage": "SCREENING",
        "amount": 1200,
        "notes": "Disparo inicial realizado em 16/09. Vocação Update."
    },
    {
        "name": "Marcenaria Sucesso",
        "contact_name": "Responsável Comercial",
        "phone": "(15) 99778-7394",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Jd. Hungares / V. Mineirão, Sorocaba - SP",
        "domain": "",
        "stage": "PROPOSAL",
        "amount": 450,
        "notes": "Perfil no Google Maps NÃO REIVINDICADO. Oferta de blindagem e presença local (R$ 450)."
    },
    {
        "name": "Dra. Thaísa Motta",
        "contact_name": "Thaísa Motta",
        "phone": "",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Parque Campolim, Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 1500,
        "notes": "Geriatria Campolim. Sem blindagem de buscas no Google Maps para Geriatria no Campolim."
    },
    {
        "name": "The Blond Sorocaba",
        "contact_name": "Gerente",
        "phone": "",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 900,
        "notes": "Catálogo e agendamento dependente exclusivamente do Instagram. Catálogo Web Interativo."
    },
    {
        "name": "SEMPI Serviços",
        "contact_name": "Gestor de Contratos",
        "phone": "(15) 99798-8298",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 1500,
        "notes": "Facilities sem página moderna de captação de condomínios. Apresentação institucional B2B."
    },
    {
        "name": "MV Viagens",
        "contact_name": "Atendimento",
        "phone": "(15) 99128-1971",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 800,
        "notes": "Pacotes e turismo sem landing de destino. Catálogo de viagens interativo."
    },
    {
        "name": "Recanto Cecilia",
        "contact_name": "Administração",
        "phone": "",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 1200,
        "notes": "Ficha do Google Maps com poucas fotos e sem tour. Tour Virtual 360° + Google Maps."
    },
    {
        "name": "Bruna Nacarato",
        "contact_name": "Bruna",
        "phone": "",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 800,
        "notes": "Dossiê pasta 2 Leads."
    },
    {
        "name": "Locação Carretinha Sorocaba",
        "contact_name": "Comercial",
        "phone": "",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 450,
        "notes": "Otimização Google Maps e presença local."
    },
    {
        "name": "Marido de Aluguel — Reparos e Manutenção",
        "contact_name": "Responsável",
        "phone": "",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 450,
        "notes": "Reparos e Manutenção Residencial."
    },
    {
        "name": "Supermercado Irmãos Nogueira",
        "contact_name": "Gerente Geral",
        "phone": "",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 1500,
        "notes": "Varejo local Sorocaba."
    },
    {
        "name": "Clinic Odonto",
        "contact_name": "Atendimento Odonto",
        "phone": "(15) 98835-3333",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 800,
        "notes": "Dossiê pronto com análise de visibilidade local."
    },
    {
        "name": "Marcos Dreher Marcenaria e Interiores",
        "contact_name": "Marcos Dreher",
        "phone": "(15) 98134-3770",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 1200,
        "notes": "Dossiê pronto. Marcenaria e interiores."
    },
    {
        "name": "Macadamor",
        "contact_name": "Atendimento",
        "phone": "(11) 96562-2828",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 800,
        "notes": "Dossiê de visibilidade online pronto."
    },
    {
        "name": "Escola Policultural",
        "contact_name": "Coordenação",
        "phone": "(15) 99108-7559",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 1500,
        "notes": "Captação de matrículas e presença digital institucional."
    },
    {
        "name": "Golden Pet Sorocaba",
        "contact_name": "Recepção Pet",
        "phone": "(15) 3019-3409",
        "email": "",
        "city": "Sorocaba",
        "state": "SP",
        "address": "Sorocaba - SP",
        "domain": "",
        "stage": "NEW",
        "amount": 600,
        "notes": "Nicho veterinário / pet shop."
    }
]

for d in dossier_leads:
    key = d["name"].lower().strip()
    companies[key] = d

# 2. Ler os 3 CSVs em "1 Leads"
csv_files = [
    os.path.join("1 Leads", "Planilha_Prospeccao_Marcenaria_Alto_Ticket_Sorocaba.csv"),
    os.path.join("1 Leads", "Planilha_Prospeccao_Garagens_Seminovos_Sorocaba.csv"),
    os.path.join("1 Leads", "Planilha_Prospeccao_Industrias_Sorocaba.csv")
]

for csv_path in csv_files:
    if not os.path.exists(csv_path):
        continue
    with open(csv_path, mode="r", encoding="latin-1", errors="replace") as f:
        reader = csv.reader(f, delimiter=";")
        header = None
        for row in reader:
            if not row or len(row) < 3:
                continue
            if not header:
                header = [c.strip().lower() for c in row]
                continue
            
            # Mapear campos básicos
            # header tem: id, data lote, nome da empresa, status crm funil, categoria, cidade/bairro, endereco, telefone, link maps, email, site, gargalo...
            try:
                name = row[2].strip() if len(row) > 2 else ""
                if not name or name.lower().startswith("nome"):
                    continue
                key = name.lower().strip()
                if key in companies:
                    continue # Já cadastrado com dados prioritários
                
                status_raw = row[3].strip() if len(row) > 3 else ""
                category = row[5].strip() if len(row) > 5 else ""
                city_raw = row[6].strip() if len(row) > 6 else "Sorocaba"
                address = row[7].strip() if len(row) > 7 else ""
                phone = row[8].strip() if len(row) > 8 else ""
                maps_link = row[9].strip() if len(row) > 9 else ""
                email = row[10].strip() if len(row) > 10 else ""
                site = row[11].strip() if len(row) > 11 else ""
                gargalo = row[12].strip() if len(row) > 12 else ""
                
                stage = "NEW"
                if "enviada" in status_raw.lower() or "disparo" in status_raw.lower():
                    stage = "SCREENING"
                elif "agendado" in status_raw.lower():
                    stage = "MEETING"
                elif "proposta" in status_raw.lower():
                    stage = "PROPOSAL"

                # Extrair cidade
                city = "Sorocaba"
                if "itu" in city_raw.lower():
                    city = "Itu"
                elif "votorantim" in city_raw.lower():
                    city = "Votorantim"

                domain = site.replace("https://", "").replace("http://", "").split("/")[0]

                companies[key] = {
                    "name": name,
                    "contact_name": "Contato " + name.split()[0],
                    "phone": phone,
                    "email": email,
                    "city": city,
                    "state": "SP",
                    "address": address,
                    "domain": domain,
                    "stage": stage,
                    "amount": 800,
                    "notes": f"Categoria: {category} | Gargalo: {gargalo} | Maps: {maps_link}"
                }
            except Exception as e:
                continue

print(f"Total de leads processados e deduplicados: {len(companies)}")

# Gerar comandos SQL em lote
sql_commands = []
now_iso = datetime.now(timezone.utc).isoformat()
pos = 1

for key, c in companies.items():
    company_id = str(uuid.uuid4())
    person_id = str(uuid.uuid4())
    opp_id = str(uuid.uuid4())
    
    # Inserir Company
    sql_commands.append(f"""
    INSERT INTO "{SCHEMA}"."company" (
        id, "createdAt", "updatedAt", name, "domainNamePrimaryLinkUrl", 
        "addressAddressCity", "addressAddressState", "addressAddressStreet1",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '{company_id}', '{now_iso}', '{now_iso}', {escape_sql(c['name'])}, {escape_sql(c['domain'])},
        {escape_sql(c['city'])}, {escape_sql(c['state'])}, {escape_sql(c['address'])},
        {pos}, 'MANUAL', {escape_sql(ADMIN_NAME)}, '{ADMIN_MEMBER_ID}'
    );
    """)

    # Inserir Person se tiver telefone ou contato
    if c['phone'] or c['contact_name']:
        sql_commands.append(f"""
        INSERT INTO "{SCHEMA}"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "emailsPrimaryEmail", "phonesPrimaryPhoneNumber", "companyId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '{person_id}', '{now_iso}', '{now_iso}', {escape_sql(c['contact_name'])}, '',
            {escape_sql(c['email'])}, {escape_sql(c['phone'])}, '{company_id}',
            {pos}, 'MANUAL', {escape_sql(ADMIN_NAME)}, '{ADMIN_MEMBER_ID}'
        );
        """)

    # Inserir Opportunity (Negócio no Funil)
    amount_micros = int(c['amount'] * 1_000_000)
    sql_commands.append(f"""
    INSERT INTO "{SCHEMA}"."opportunity" (
        id, "createdAt", "updatedAt", name, "amountAmountMicros", "amountCurrencyCode",
        stage, "companyId", "ownerId", position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '{opp_id}', '{now_iso}', '{now_iso}', {escape_sql('Assessoria Digital - ' + c['name'])}, {amount_micros}, 'BRL',
        '{c['stage']}', '{company_id}', '{ADMIN_MEMBER_ID}', {pos}, 'MANUAL', {escape_sql(ADMIN_NAME)}, '{ADMIN_MEMBER_ID}'
    );
    """)
    
    pos += 1

print(f"Executando inserção de {len(sql_commands)} registros no banco Twenty...")
batch_size = 50
for i in range(0, len(sql_commands), batch_size):
    batch = "\n".join(sql_commands[i:i+batch_size])
    run_psql(batch)

print("Inserção concluída com sucesso!")
