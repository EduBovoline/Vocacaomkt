import os
import uuid
import psycopg2
from psycopg2.extras import RealDictCursor

SCHEMA = os.environ.get("POSTGRES_CRM_SCHEMA", "workspace_2xmx8hech9nybwidia3404k2z")
PG_HOST = os.environ.get("POSTGRES_CRM_HOST", "twenty-db-1")
PG_PORT = int(os.environ.get("POSTGRES_CRM_PORT", 5432))
PG_USER = os.environ.get("POSTGRES_CRM_USER", "postgres")
PG_PASS = os.environ.get("POSTGRES_CRM_PASSWORD", "postgres")
PG_DB = os.environ.get("POSTGRES_CRM_DB", "twenty")
EDUARDO_MEMBER_ID = "1c0b8905-7e8f-4f50-90a1-6c67135bb381"

def get_connection():
    try:
        conn = psycopg2.connect(
            host=PG_HOST,
            port=PG_PORT,
            user=PG_USER,
            password=PG_PASS,
            dbname=PG_DB,
            connect_timeout=3
        )
        return conn
    except Exception as e:
        print(f"[!] Aviso conexão Twenty Postgres: {e}")
        return None

def find_lead_in_db(phone_digits: str):
    last_digits = phone_digits[-8:] if len(phone_digits) >= 8 else phone_digits
    conn = get_connection()
    if not conn:
        return None

    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            sql = f"""
            SELECT c.id as company_id, c.name as company_name, p.id as person_id, o.id as opportunity_id
            FROM "{SCHEMA}"."company" c
            JOIN "{SCHEMA}"."person" p ON p."companyId" = c.id
            LEFT JOIN "{SCHEMA}"."opportunity" o ON o."companyId" = c.id
            WHERE regexp_replace(p."phonesPrimaryPhoneNumber", '[^0-9]', '', 'g') LIKE %s
            LIMIT 1;
            """
            cur.execute(sql, (f"%{last_digits}%",))
            row = cur.fetchone()
            if row:
                return {
                    "id": str(row["company_id"]),
                    "name": str(row["company_name"]),
                    "person_id": str(row["person_id"]) if row["person_id"] else None,
                    "opportunity_id": str(row["opportunity_id"]) if row["opportunity_id"] else None
                }
    except Exception as e:
        print(f"[!] Erro ao consultar CRM via Postgres: {e}")
    finally:
        conn.close()

    return None

def record_lead_interaction(company_id: str, person_id: str, opportunity_id: str, title: str, markdown_content: str):
    conn = get_connection()
    if not conn:
        return False

    note_id = str(uuid.uuid4())
    try:
        with conn.cursor() as cur:
            # 1. Cria a nota oficial
            sql_note = f"""
            INSERT INTO "{SCHEMA}"."note" (
                id, "createdAt", "updatedAt", title, "bodyV2Markdown",
                position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
            ) VALUES (
                %s, NOW(), NOW(),
                %s, %s,
                1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', %s
            );
            """
            cur.execute(sql_note, (note_id, title, markdown_content, EDUARDO_MEMBER_ID))

            # 2. Vincula a nota à Company, Person e Opportunity (aparece no feed visual)
            target_id = str(uuid.uuid4())
            sql_target = f"""
            INSERT INTO "{SCHEMA}"."noteTarget" (
                id, "createdAt", "updatedAt", "noteId",
                "targetCompanyId", "targetPersonId", "targetOpportunityId",
                position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
            ) VALUES (
                %s, NOW(), NOW(), %s,
                %s, %s, %s,
                1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', %s
            );
            """
            cur.execute(sql_target, (
                target_id, note_id,
                company_id if company_id else None,
                person_id if person_id else None,
                opportunity_id if opportunity_id else None,
                EDUARDO_MEMBER_ID
            ))

            conn.commit()
            print(f"[✓] Twenty CRM: Nota e vínculos registrados com sucesso para empresa {company_id}.")
            return True
    except Exception as e:
        print(f"[!] Erro ao inserir nota vinculada no CRM: {e}")
        conn.rollback()
    finally:
        conn.close()

    return False

def update_lead_opportunity(company_id: str, stage: str = "MEETING", amount_micros: int = None):
    conn = get_connection()
    if not conn or not company_id:
        return False

    try:
        with conn.cursor() as cur:
            if amount_micros:
                sql = f"""
                UPDATE "{SCHEMA}"."opportunity"
                SET stage = %s,
                    "amountAmountMicros" = %s,
                    "amountCurrencyCode" = 'BRL',
                    "updatedAt" = NOW()
                WHERE "companyId" = %s;
                """
                cur.execute(sql, (stage, amount_micros, company_id))
            else:
                sql = f"""
                UPDATE "{SCHEMA}"."opportunity"
                SET stage = %s, "updatedAt" = NOW()
                WHERE "companyId" = %s;
                """
                cur.execute(sql, (stage, company_id))

            conn.commit()
            print(f"[✓] Twenty CRM: Oportunidade atualizada para '{stage}' (Valor: {amount_micros}).")
            return True
    except Exception as e:
        print(f"[!] Erro ao atualizar oportunidade: {e}")
        conn.rollback()
    finally:
        conn.close()

    return False

def create_followup_task(company_id: str, person_id: str, opportunity_id: str, title: str, markdown_content: str):
    conn = get_connection()
    if not conn:
        return False

    task_id = str(uuid.uuid4())
    try:
        with conn.cursor() as cur:
            # 1. Cria a tarefa de follow-up atribuída a Eduardo
            sql_task = f"""
            INSERT INTO "{SCHEMA}"."task" (
                id, "createdAt", "updatedAt", title, "bodyV2Markdown",
                "dueAt", status, "assigneeId",
                position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
            ) VALUES (
                %s, NOW(), NOW(), %s, %s,
                NOW() + INTERVAL '24 hours', 'TODO', %s,
                1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', %s
            );
            """
            cur.execute(sql_task, (task_id, title, markdown_content, EDUARDO_MEMBER_ID, EDUARDO_MEMBER_ID))

            # 2. Vincula a tarefa à Company
            target_id = str(uuid.uuid4())
            sql_target = f"""
            INSERT INTO "{SCHEMA}"."taskTarget" (
                id, "createdAt", "updatedAt", "taskId",
                "targetCompanyId", "targetPersonId", "targetOpportunityId",
                position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
            ) VALUES (
                %s, NOW(), NOW(), %s,
                %s, %s, %s,
                1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', %s
            );
            """
            cur.execute(sql_target, (
                target_id, task_id,
                company_id if company_id else None,
                person_id if person_id else None,
                opportunity_id if opportunity_id else None,
                EDUARDO_MEMBER_ID
            ))

            conn.commit()
            print(f"[✓] Twenty CRM: Tarefa de follow-up criada com sucesso no pipeline.")
            return True
    except Exception as e:
        print(f"[!] Erro ao criar tarefa no CRM: {e}")
        conn.rollback()
    finally:
        conn.close()

    return False
