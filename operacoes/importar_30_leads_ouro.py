import json
import uuid

WORKSPACE_SCHEMA = "workspace_2xmx8hech9nybwidia3404k2z"
MEMBER_ID = "1c0b8905-7e8f-4f50-90a1-6c67135bb381"

def generate_sql():
    with open('leads_100_santa_rosalia_brasilandia.json', 'r', encoding='utf-8') as f:
        all_leads = json.load(f)

    gold_leads = [l for l in all_leads if l.get('interesse_vendedor', 0) >= 90]
    print(f"Total de Leads Ouro: {len(gold_leads)}")

    sql_lines = []
    imported_leads = []

    for l in gold_leads:
        company_id = str(uuid.uuid4())
        person_id = str(uuid.uuid4())
        opp_id = str(uuid.uuid4())
        note_id = str(uuid.uuid4())
        target_id = str(uuid.uuid4())

        c_name = l['name'].replace("'", "''")
        c_street = l['addr'].replace("'", "''")
        c_phone = l['phone']
        c_cat = l['cat'].replace("'", "''")
        c_bairro = l['bairro'].replace("'", "''")
        c_oferta_nome = l['oferta_nome'].replace("'", "''")
        c_oferta_micros = int(l.get('oferta_micros', 850000000))
        c_preco = l.get('oferta_preco', 850.0)
        c_score = l.get('interesse_vendedor', 90)
        c_tag = l.get('interesse_tag', 'Ouro').replace("'", "''")
        c_presence = l.get('presence', '').replace("'", "''")
        c_hook = l.get('hook_whatsapp', '').replace("'", "''")

        opp_title = f"{c_name} — {c_oferta_nome.split('(')[0].strip()}"
        note_body = (
            f"**Bairro:** {c_bairro} ({c_street})\\n"
            f"**Categoria:** {c_cat}\\n"
            f"**Canal:** WhatsApp Celular ({c_phone})\\n\\n"
            f"**Qualificação Jev System One:**\\n"
            f"- **Oferta de Melhor Fit:** {c_oferta_nome} (R$ {c_preco:.2f})\\n"
            f"- **Score de Interesse Vocação:** {c_score}% (⭐ {c_tag})\\n"
            f"- **Presença Digital:** {c_presence}\\n\\n"
            f"**Hook Oficial de Abordagem:**\\n> \"{c_hook}\""
        )

        sql_lines.append(f"""
        INSERT INTO "{WORKSPACE_SCHEMA}"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '{company_id}', NOW(), NOW(), '{c_name}', '{c_street}',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '{MEMBER_ID}'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "{WORKSPACE_SCHEMA}"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '{person_id}', NOW(), NOW(), 'Responsável Comercial', '{c_name}',
            '{c_phone}', '{company_id}', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '{MEMBER_ID}'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "{WORKSPACE_SCHEMA}"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '{opp_id}', NOW(), NOW(), '{opp_title}', 'NEW', {c_oferta_micros}, 'BRL',
            '{company_id}', '{person_id}', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '{MEMBER_ID}'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "{WORKSPACE_SCHEMA}"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '{note_id}', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '{note_body}',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '{MEMBER_ID}'
        );

        INSERT INTO "{WORKSPACE_SCHEMA}"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '{target_id}', NOW(), NOW(), '{note_id}', '{company_id}', '{person_id}', '{opp_id}',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '{MEMBER_ID}'
        );
        """)

        lead_entry = dict(l)
        lead_entry['company_id'] = company_id
        lead_entry['person_id'] = person_id
        lead_entry['opportunity_id'] = opp_id
        imported_leads.append(lead_entry)

    with open('importar_30_leads_ouro.sql', 'w', encoding='utf-8') as f:
        f.write("\n".join(sql_lines))

    with open('leads_ouro_fila_disparo.json', 'w', encoding='utf-8') as f:
        json.dump(imported_leads, f, indent=2, ensure_ascii=False)

    print("Gerados importar_30_leads_ouro.sql e leads_ouro_fila_disparo.json com sucesso!")

if __name__ == '__main__':
    generate_sql()
