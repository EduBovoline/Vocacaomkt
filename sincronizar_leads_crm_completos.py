import os
import re
import csv
import subprocess

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
        print("SQL Error:", stderr[:300])
    return stdout

print("Iniciando alinhamento dos leads com os dossiês e CRMs da pasta 1 Leads...")

# 1. Dossiês Especiais Individuais da pasta 1 Leads
special_leads = [
    {
        "name": "Marcenaria Sucesso",
        "contact_first": "Responsável",
        "contact_last": "Comercial",
        "job_title": "Marceneiro & Proprietário",
        "phone": "(15) 99778-7394",
        "email": "contato@marcenariasucesso.com.br",
        "street": "R. Firmino Mineli, 259",
        "neighborhood": "Jd. Hungares / V. Mineirão",
        "city": "Sorocaba",
        "state": "SP",
        "cep": "18076-180",
        "domain": "",
        "domain_label": "",
        "annual_rev": 360000,
        "opp_amount": 450,
        "opp_stage": "PROPOSAL",
        "opp_name": "Blindagem Google Maps (Perfil Não Reivindicado) - Marcenaria Sucesso"
    },
    {
        "name": "Clinic Odonto",
        "contact_first": "Dra. Elza",
        "contact_last": "Peres Nunes",
        "job_title": "Cirurgiã-Dentista & Sócia-Fundadora",
        "phone": "(15) 98835-3333",
        "email": "contato@clinicodonto.com.br",
        "street": "R. Joaquim Ferreira Barbosa, 345",
        "neighborhood": "Jd. Maria do Carmo / Abaeté",
        "city": "Sorocaba",
        "state": "SP",
        "cep": "18081-090",
        "domain": "",
        "domain_label": "",
        "annual_rev": 480000,
        "opp_amount": 800,
        "opp_stage": "NEW",
        "opp_name": "Presença Local & Google Maps - Clinic Odonto"
    },
    {
        "name": "Marcos Dreher Marcenaria e Interiores",
        "contact_first": "Marcos",
        "contact_last": "Dreher",
        "job_title": "Marceneiro & Projetista",
        "phone": "(15) 98134-3770",
        "email": "contato@marcosdreher.com.br",
        "street": "Atendimento Regional Sorocaba",
        "neighborhood": "Sorocaba e Região",
        "city": "Sorocaba",
        "state": "SP",
        "cep": "18000-000",
        "domain": "",
        "domain_label": "",
        "annual_rev": 300000,
        "opp_amount": 1200,
        "opp_stage": "NEW",
        "opp_name": "Catálogo Digital & Google Maps - Marcos Dreher"
    },
    {
        "name": "Escola Policultural",
        "contact_first": "Coordenação",
        "contact_last": "Pedagógica",
        "job_title": "Diretoria & Admissões",
        "phone": "(15) 99108-7559",
        "email": "contato@escolapolicultural.com.br",
        "street": "R. Maria Cinto de Biaggi, 130",
        "neighborhood": "Jd. Santa Rosália",
        "city": "Sorocaba",
        "state": "SP",
        "cep": "18095-410",
        "domain": "escolapolicultural.com.br",
        "domain_label": "Site Atual",
        "annual_rev": 720000,
        "opp_amount": 1500,
        "opp_stage": "NEW",
        "opp_name": "Campanha de Matrículas & Presença Digital - Escola Policultural"
    },
    {
        "name": "Macadamor",
        "contact_first": "Atendimento",
        "contact_last": "Comercial",
        "job_title": "Gestão Comercial",
        "phone": "(11) 96562-2828",
        "email": "contato@macadamor.com.br",
        "street": "Atendimento Sorocaba e SP",
        "neighborhood": "Sorocaba",
        "city": "Sorocaba",
        "state": "SP",
        "cep": "18000-000",
        "domain": "",
        "domain_label": "",
        "annual_rev": 240000,
        "opp_amount": 800,
        "opp_stage": "NEW",
        "opp_name": "Presença Online & Catálogo - Macadamor"
    },
    {
        "name": "Golden Pet Sorocaba",
        "contact_first": "Recepção",
        "contact_last": "Pet",
        "job_title": "Gerente de Atendimento",
        "phone": "(15) 3019-3409",
        "email": "contato@goldenpet.com.br",
        "street": "R. Cel. Benedito Pires, 85",
        "neighborhood": "Centro",
        "city": "Sorocaba",
        "state": "SP",
        "cep": "18010-160",
        "domain": "",
        "domain_label": "",
        "annual_rev": 360000,
        "opp_amount": 600,
        "opp_stage": "NEW",
        "opp_name": "Google Maps & Presença Local - Golden Pet"
    },
    {
        "name": "Luis Carlos Fatima Sanches",
        "contact_first": "Luis Carlos",
        "contact_last": "Sanches",
        "job_title": "Proprietário",
        "phone": "",
        "email": "",
        "street": "Sorocaba e Região",
        "neighborhood": "Sorocaba",
        "city": "Sorocaba",
        "state": "SP",
        "cep": "18000-000",
        "domain": "",
        "domain_label": "",
        "annual_rev": 200000,
        "opp_amount": 800,
        "opp_stage": "NEW",
        "opp_name": "Presença Digital Local - Luis Carlos & Fatima"
    }
]

sql_updates = []

for s in special_leads:
    # Atualizar Company
    sql_updates.append(f"""
    UPDATE "{SCHEMA}"."company"
    SET 
        "addressAddressStreet1" = {escape_sql(s['street'])},
        "addressAddressStreet2" = {escape_sql(s['neighborhood'])},
        "addressAddressCity" = {escape_sql(s['city'])},
        "addressAddressState" = {escape_sql(s['state'])},
        "addressAddressCountry" = 'Brasil',
        "addressAddressPostcode" = {escape_sql(s['cep'])},
        "domainNamePrimaryLinkLabel" = {escape_sql(s['domain_label'])},
        "domainNamePrimaryLinkUrl" = {escape_sql(s['domain'])},
        "annualRevenueAmountMicros" = {int(s['annual_rev'] * 1_000_000)},
        "annualRevenueCurrencyCode" = 'BRL'
    WHERE LOWER(TRIM(name)) = LOWER('{s['name']}');
    """)

    # Atualizar ou Inserir Person
    sql_updates.append(f"""
    UPDATE "{SCHEMA}"."person"
    SET
        "nameFirstName" = {escape_sql(s['contact_first'])},
        "nameLastName" = {escape_sql(s['contact_last'])},
        "jobTitle" = {escape_sql(s['job_title'])},
        "phonesPrimaryPhoneNumber" = {escape_sql(s['phone'])},
        "emailsPrimaryEmail" = {escape_sql(s['email'])}
    WHERE "companyId" = (SELECT id FROM "{SCHEMA}"."company" WHERE LOWER(TRIM(name)) = LOWER('{s['name']}'));
    """)

    # Atualizar Opportunity
    sql_updates.append(f"""
    UPDATE "{SCHEMA}"."opportunity"
    SET
        name = {escape_sql(s['opp_name'])},
        "amountAmountMicros" = {int(s['opp_amount'] * 1_000_000)},
        "amountCurrencyCode" = 'BRL',
        stage = '{s['opp_stage']}'
    WHERE "companyId" = (SELECT id FROM "{SCHEMA}"."company" WHERE LOWER(TRIM(name)) = LOWER('{s['name']}'));
    """)

# 2. Processar e limpar os leads de Marcenarias, Garagens e Indústrias das planilhas CSV
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
            if not row or len(row) < 12:
                continue
            if not header:
                header = [c.strip().lower() for c in row]
                continue
            name = row[2].strip()
            if not name or name.lower().startswith("nome"):
                continue
            
            cidade_raw = row[6].strip()
            endereco = row[7].strip()
            telefone = row[8].strip()
            site = row[11].strip()
            
            # Limpar endereço: separar rua e cidade
            street1 = endereco
            city = "Sorocaba"
            state = "SP"
            cep = ""
            
            if "itu" in cidade_raw.lower():
                city = "Itu"
            elif "votorantim" in cidade_raw.lower():
                city = "Votorantim"
                
            cep_match = re.search(r'\d{5}-\d{3}', endereco)
            if cep_match:
                cep = cep_match.group(0)
                
            domain = site.replace("https://", "").replace("http://", "").split("/")[0]

            sql_updates.append(f"""
            UPDATE "{SCHEMA}"."company"
            SET 
                "addressAddressStreet1" = {escape_sql(street1)},
                "addressAddressCity" = {escape_sql(city)},
                "addressAddressState" = {escape_sql(state)},
                "addressAddressCountry" = 'Brasil',
                "addressAddressPostcode" = {escape_sql(cep)},
                "domainNamePrimaryLinkUrl" = {escape_sql(domain)}
            WHERE LOWER(TRIM(name)) = LOWER({escape_sql(name)});
            """)
            
            if telefone:
                sql_updates.append(f"""
                UPDATE "{SCHEMA}"."person"
                SET "phonesPrimaryPhoneNumber" = {escape_sql(telefone)}
                WHERE "companyId" = (SELECT id FROM "{SCHEMA}"."company" WHERE LOWER(TRIM(name)) = LOWER({escape_sql(name)}));
                """)

print(f"Executando {len(sql_updates)} comandos de sincronização e alinhamento...")
batch_size = 40
for i in range(0, len(sql_updates), batch_size):
    batch = "\n".join(sql_updates[i:i+batch_size])
    run_psql(batch)

print("Alinhamento concluído com sucesso!")
