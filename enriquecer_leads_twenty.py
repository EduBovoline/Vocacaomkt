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
        print("SQL Error:", stderr[:300])
    return stdout

print("Carregando empresas e oportunidades existentes do Twenty...")
output = run_psql(f"""
SELECT c.id AS comp_id, c.name AS comp_name, o.id AS opp_id, o.name AS opp_name, o.stage
FROM "{SCHEMA}"."company" c
LEFT JOIN "{SCHEMA}"."opportunity" o ON o."companyId" = c.id;
""")

existing_data = {}
for line in output.splitlines():
    parts = [p.strip() for p in line.split("|")]
    if len(parts) >= 5 and parts[0] and parts[0] != "comp_id":
        comp_id = parts[0]
        comp_name = parts[1]
        opp_id = parts[2]
        opp_name = parts[3]
        stage = parts[4]
        if comp_name:
            existing_data[comp_name.lower().strip()] = {
                "comp_id": comp_id,
                "comp_name": comp_name,
                "opp_id": opp_id,
                "opp_name": opp_name,
                "stage": stage
            }

print(f"Empresas mapeadas no banco: {len(existing_data)}")

# Limpar notas e tarefas anteriores para reimportar com dados ricos e completos
print("Limpando notas e tarefas anteriores para recarga completa...")
run_psql(f"""
DELETE FROM "{SCHEMA}"."noteTarget";
DELETE FROM "{SCHEMA}"."note";
DELETE FROM "{SCHEMA}"."taskTarget";
DELETE FROM "{SCHEMA}"."task";
DELETE FROM "{SCHEMA}"."company" WHERE name IS NULL OR TRIM(name) = '';
""")

now_iso = datetime.now(timezone.utc).isoformat()
sql_commands = []
pos = 1

# Mapeamento detalhado dos dossiês prioritários
dossier_details = {
    "espaço naturê": {
        "title": "Onboarding & Diagnóstico — Espaço Naturê (Miriam)",
        "body": """### 🏆 Status: Cliente Fechado (R$ 1.500)
- **Responsável:** Miriam
- **Data de Fechamento:** 08/09/2026
- **Oferta Contratada:** Onboarding Estratégico + Reestruturação de Presença Local / Google Maps.

### 📁 Entregáveis Prontos / No Ar:
- **Formulário de Onboarding:** `https://vocacao.digital/espaconature`
- **Questionário Local:** `1 Leads/onboarding-espaco-nature-miriam.html`
- **Diagnóstico de Visibilidade:** `1 Leads/Análise Visibilidade Local Vocação - Espaco Nature.pdf`

### ⚠️ Ponto Crítico Atual:
Aguardando retorno da Miriam com dados e fotos para subir a otimização no Google Maps.

### 🚨 Próxima Ação:
Enviar lembrete amigável no WhatsApp solicitando o preenchimento do formulário.
""",
        "task": {
            "title": "Cobrar dados de onboarding da Miriam (Espaço Naturê) no WhatsApp",
            "status": "TODO"
        }
    },
    "safety first engenharia": {
        "title": "Entrega & Faturamento — Safety First (Fabio & Davi)",
        "body": """### 🏆 Status: Cliente Pago (R$ 450,00)
- **Responsáveis:** Fabio e Davi (sócio)
- **Serviço Entregue:** Site institucional minimalista industrial com scroll cinematográfico e vídeos em alta performance.

### 📁 Ativos Desenvolvidos:
- **Repositório Demo GitHub:** `https://github.com/EduBovoline/Safetyfirst_vocacaoDemo`
- **Pasta Local do Projeto:** `C:\\Vocação 2027\\Criente e portifa\\Safety First`

### 🚀 Próxima Ação:
Aguardando apenas o aval final do Davi para apontar o domínio oficial e virar a chave da hospedagem.
""",
        "task": {
            "title": "Apontar domínio oficial da Safety First assim que Davi confirmar",
            "status": "TODO"
        }
    },
    "clínica piacitelli": {
        "title": "Dossiê Estratégico — Clínica Piacitelli (Odontologia & Estética)",
        "body": """### 🟡 Status: Em Negociação Ativa
- **Responsável Vocação:** Edu Bovoline
- **Nicho:** Odontologia e Harmonização Facial de Alto Padrão
- **Localização:** Sorocaba - SP

### 🎯 Gargalo Crítico Identificado:
Presença no Google Maps subaproveitada e ausência de landing page focada em conversão de tratamentos estéticos de alto ticket.

### 🛠️ Proposta em Alinhamento:
Estruturação de autoridade médica local + Blindagem Google Maps + Campanha direcionada para pacientes de alto valor.
""",
        "task": {
            "title": "Fazer reunião/follow-up de alinhamento da proposta Piacitelli",
            "status": "IN_PROGRESS"
        }
    },
    "magen segurança eletrônica": {
        "title": "Dossiê & Abordagem — Magen Segurança Eletrônica",
        "body": """### 🟠 Status: Disparo Realizado (16/09)
- **Telefone:** (11) 94561-5331
- **Oferta Apresentada:** Vocação Update / Presença Digital B2B

### 💬 Histórico do Contato:
Primeiro contato enviado via WhatsApp com script consultivo focado na proteção de marca e captação institucional de condomínios.

### 🚨 Próxima Ação:
Cadência de follow-up D+2 caso o diretor comercial não responda até segunda-feira.
""",
        "task": {
            "title": "Follow-up de abordagem Magen Segurança Eletrônica",
            "status": "TODO"
        }
    },
    "marcenaria sucesso": {
        "title": "Alerta Crítico de Ficha — Marcenaria Sucesso",
        "body": """### 🔴 Status: Alerta Imediato / Risco de Sequestro de Ficha
- **Telefone:** (15) 99778-7394
- **Local:** Jd. Hungares / V. Mineirão, Sorocaba - SP
- **Ticket da Oferta:** R$ 450 (Pilar Presença Local)

### ⚠️ Gargalo Crítico Máximo:
O perfil no Google Maps da Marcenaria Sucesso **NÃO ESTÁ REIVINDICADO**. Qualquer usuário ou concorrente pode sugerir alteração ou tomar posse da ficha.

### 💬 Script Pronto para Envio:
*\"Olá! Notei que a ficha da Marcenaria Sucesso no Google Maps ainda consta como 'Não Reivindicada'. Isso é um risco grave pois qualquer um pode alterar o telefone ou o endereço da sua loja. Podemos blindar sua presença hoje mesmo?\"*
""",
        "task": {
            "title": "Disparar alerta de perfil não reivindicado para Marcenaria Sucesso",
            "status": "TODO"
        }
    },
    "dra. thaísa motta": {
        "title": "Dossiê de Autoridade Médica — Dra. Thaísa Motta (Geriatria)",
        "body": """### 🩺 Nicho: Geriatria & Longevidade no Parque Campolim
- **Localização:** Parque Campolim, Sorocaba - SP
- **Ticket Médio de Consulta/Acompanhamento:** R$ 500 - R$ 1.500
- **Dossiê Completo:** Pasta `2 Leads/Dra. Thaísa Motta - Geriatria Campolim`

### 🎯 Diagnóstico de Presença:
Falta de posicionamento orgânico na busca 'Geriatra Campolim Sorocaba' e ausência de página de agendamento ágil para familiares dos pacientes.

### 🛠️ Pilares Recomendados:
1. Google Maps Médico com fotos profissionais e avaliações blindadas.
2. Landing Page institucional de acolhimento e agendamento.
"""
    },
    "the blond sorocaba": {
        "title": "Dossiê de Conversão — The Blond Sorocaba",
        "body": """### 💇‍♀️ Nicho: Salão Premium & Loiros
- **Localização:** Sorocaba - SP
- **Dossiê Completo:** Pasta `2 Leads/The Blond Sorocaba`

### 🎯 Gargalo Crítico:
100% dependente do feed e Direct do Instagram. Sem catálogo interativo indexado no Google e sem fluxo automatizado de agendamento.

### 🛠️ Pilares Recomendados:
1. Catálogo Web Interativo de Serviços.
2. Otimização de Ficha Local do Google para noivas e loiros.
"""
    },
    "sempi serviços": {
        "title": "Dossiê B2B — SEMPI Serviços (Facilities)",
        "body": """### 🏢 Nicho: Terceirização de Portaria, Limpeza & Facilities
- **Telefone:** (15) 99798-8298
- **Localização:** Sorocaba - SP

### 🎯 Gargalo Crítico:
Site desatualizado sem foco na captação direta de síndicos e administradoras de condomínio de alto padrão em Sorocaba.

### 🛠️ Pilares Recomendados:
Landing Page B2B corporativa de alta conversão + Campanha de busca local focada em condomínios.
"""
    },
    "recanto cecilia": {
        "title": "Dossiê Espaço de Eventos — Recanto Cecilia",
        "body": """### 🌳 Nicho: Espaço para Festas e Eventos
- **Localização:** Sorocaba - SP
- **Dossiê Completo:** Pasta `2 Leads/Recanto Cecilia`

### 🎯 Gargalo Crítico:
Ficha do Google Maps com poucas fotos e sem imersão; o cliente de eventos precisa visitar pessoalmente antes de alugar.

### 🛠️ Solução Ideal Vocação:
Tour Virtual 360° com câmera GoPro Max 2 integrado ao Google Street View e ficha oficial otimizada.
"""
    }
}

# Processar as pastas e CSVs para extrair todos os detalhes
csv_files = [
    os.path.join("1 Leads", "Planilha_Prospeccao_Marcenaria_Alto_Ticket_Sorocaba.csv"),
    os.path.join("1 Leads", "Planilha_Prospeccao_Garagens_Seminovos_Sorocaba.csv"),
    os.path.join("1 Leads", "Planilha_Prospeccao_Industrias_Sorocaba.csv")
]

csv_details = {}
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
            name = row[2].strip() if len(row) > 2 else ""
            if not name or name.lower().startswith("nome"):
                continue
            key = name.lower().strip()
            
            status = row[3].strip() if len(row) > 3 else ""
            categoria = row[5].strip() if len(row) > 5 else ""
            cidade = row[6].strip() if len(row) > 6 else ""
            endereco = row[7].strip() if len(row) > 7 else ""
            telefone = row[8].strip() if len(row) > 8 else ""
            maps_link = row[9].strip() if len(row) > 9 else ""
            email = row[10].strip() if len(row) > 10 else ""
            site = row[11].strip() if len(row) > 11 else ""
            gargalo = row[12].strip() if len(row) > 12 else ""
            pilares = row[13].strip() if len(row) > 13 else ""
            ticket = row[14].strip() if len(row) > 14 else ""
            roi = row[15].strip() if len(row) > 15 else ""
            prioridade = row[16].strip() if len(row) > 16 else ""
            script_ini = row[17].strip() if len(row) > 17 else ""
            script_fup1 = row[18].strip() if len(row) > 18 else ""
            notas = row[21].strip() if len(row) > 21 else ""
            
            body = f"""### 🎯 Diagnóstico Estratégico & Gargalo
- **Categoria:** {categoria}
- **Região:** {cidade}
- **Gargalo Crítico:** {gargalo}
- **Pilares Recomendados:** {pilares}
- **Ticket Médio Estimado:** {ticket}
- **ROI Esperado:** {roi}
- **Prioridade Comercial:** {prioridade}

### 💬 Scripts de Abordagem Personalizados
- **Abordagem Inicial:**
> *"{script_ini}"*

- **Follow-up 1:**
> *"{script_fup1}"*

### 📍 Dados de Contato & Localização
- **Telefone:** {telefone}
- **E-mail:** {email}
- **Site Atual:** {site}
- **Google Maps:** {maps_link}
- **Endereço:** {endereco}
- **Notas Internas:** {notas}
"""
            csv_details[key] = {
                "title": f"Dossiê Completo — {name}",
                "body": body
            }

# Agora inserir Notas e Tarefas no Twenty
print("Vinculando notas ricas e tarefas às empresas do Twenty...")

total_notes = 0
total_tasks = 0

for comp_name_lower, info in existing_data.items():
    comp_id = info["comp_id"]
    opp_id = info["opp_id"]
    
    # Encontrar detalhe prioritário ou do CSV
    detail = None
    task_info = None
    
    # Busca exata ou por substring
    for d_key, d_val in dossier_details.items():
        if d_key in comp_name_lower or comp_name_lower in d_key:
            detail = d_val
            if "task" in d_val:
                task_info = d_val["task"]
            break
            
    if not detail:
        for c_key, c_val in csv_details.items():
            if c_key in comp_name_lower or comp_name_lower in c_key:
                detail = c_val
                break
                
    if not detail:
        detail = {
            "title": f"Dossiê Comercial — {info['comp_name']}",
            "body": f"Lead cadastrado no pipeline da Vocação Digital 2027. Localização: Sorocaba e Região."
        }
        
    note_id = str(uuid.uuid4())
    note_target_id = str(uuid.uuid4())
    
    # 1. Inserir Note
    sql_commands.append(f"""
    INSERT INTO "{SCHEMA}"."note" (
        id, "createdAt", "updatedAt", position, title, "bodyV2Markdown",
        "createdBySource", "createdByName", "createdByWorkspaceMemberId",
        "updatedBySource", "updatedByName", "updatedByWorkspaceMemberId"
    ) VALUES (
        '{note_id}', '{now_iso}', '{now_iso}', {pos}, {escape_sql(detail['title'])}, {escape_sql(detail['body'])},
        'MANUAL', {escape_sql(ADMIN_NAME)}, '{ADMIN_MEMBER_ID}',
        'MANUAL', {escape_sql(ADMIN_NAME)}, '{ADMIN_MEMBER_ID}'
    );
    """)
    
    # 2. Inserir NoteTarget (vinculando a Empresa e Oportunidade)
    opp_clause = f"'{opp_id}'" if opp_id else "NULL"
    sql_commands.append(f"""
    INSERT INTO "{SCHEMA}"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId",
        "updatedBySource", "updatedByName", "updatedByWorkspaceMemberId"
    ) VALUES (
        '{note_target_id}', '{now_iso}', '{now_iso}', '{note_id}', '{comp_id}', {opp_clause},
        {pos}, 'MANUAL', {escape_sql(ADMIN_NAME)}, '{ADMIN_MEMBER_ID}',
        'MANUAL', {escape_sql(ADMIN_NAME)}, '{ADMIN_MEMBER_ID}'
    );
    """)
    total_notes += 1
    
    # 3. Inserir Tarefa se houver
    if task_info:
        task_id = str(uuid.uuid4())
        task_target_id = str(uuid.uuid4())
        sql_commands.append(f"""
        INSERT INTO "{SCHEMA}"."task" (
            id, "createdAt", "updatedAt", position, title, status,
            "createdBySource", "createdByName", "createdByWorkspaceMemberId",
            "updatedBySource", "updatedByName", "updatedByWorkspaceMemberId"
        ) VALUES (
            '{task_id}', '{now_iso}', '{now_iso}', {pos}, {escape_sql(task_info['title'])}, '{task_info['status']}',
            'MANUAL', {escape_sql(ADMIN_NAME)}, '{ADMIN_MEMBER_ID}',
            'MANUAL', {escape_sql(ADMIN_NAME)}, '{ADMIN_MEMBER_ID}'
        );
        INSERT INTO "{SCHEMA}"."taskTarget" (
            id, "createdAt", "updatedAt", "taskId", "targetCompanyId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId",
            "updatedBySource", "updatedByName", "updatedByWorkspaceMemberId"
        ) VALUES (
            '{task_target_id}', '{now_iso}', '{now_iso}', '{task_id}', '{comp_id}', {opp_clause},
            {pos}, 'MANUAL', {escape_sql(ADMIN_NAME)}, '{ADMIN_MEMBER_ID}',
            'MANUAL', {escape_sql(ADMIN_NAME)}, '{ADMIN_MEMBER_ID}'
        );
        """)
        total_tasks += 1
        
    pos += 1

print(f"Executando inserção em lote de {len(sql_commands)} queries no banco...")
batch_size = 40
for i in range(0, len(sql_commands), batch_size):
    batch = "\n".join(sql_commands[i:i+batch_size])
    run_psql(batch)

print(f"Sucesso! {total_notes} notas detalhadas e {total_tasks} tarefas foram vinculadas aos leads no Twenty!")
