import re

main_path = r"c:\Vocação 2027\QG Vocação 2027 do zero\auto_responder_docker\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Adicionar AUTO_RESPONDER_ENABLED = False
if "AUTO_RESPONDER_ENABLED =" not in code:
    code = code.replace("QUEUE_PAUSED = True", "QUEUE_PAUSED = True\nAUTO_RESPONDER_ENABLED = False")

# 2. Atualizar res_data em /api/subcrm-data para incluir high_ticket_leads e auto_responder_enabled
old_res_data = '''            res_data = {
                "queue": {'''

new_res_data = '''            high_ticket = load_json_file(os.path.join(DATA_DIR, "leads_alto_ticket_verificados.json"))
            res_data = {
                "auto_responder_enabled": AUTO_RESPONDER_ENABLED,
                "high_ticket_leads": high_ticket if isinstance(high_ticket, list) else [],
                "queue": {'''

if old_res_data in code:
    code = code.replace(old_res_data, new_res_data)

# 3. Adicionar endpoints /api/toggle-auto-responder e /api/add-to-queue em do_POST
old_toggle_queue = '''        if parsed == "/api/toggle-queue":
            global QUEUE_PAUSED
            QUEUE_PAUSED = not QUEUE_PAUSED
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "is_paused": QUEUE_PAUSED}).encode())
            return'''

new_toggle_queue = '''        if parsed == "/api/toggle-auto-responder":
            global AUTO_RESPONDER_ENABLED
            AUTO_RESPONDER_ENABLED = not AUTO_RESPONDER_ENABLED
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "auto_responder_enabled": AUTO_RESPONDER_ENABLED}).encode())
            return

        if parsed == "/api/add-to-queue":
            try:
                payload = json.loads(body)
                fila_path = os.path.join(DATA_DIR, "leads_ouro_fila_disparo.json")
                cur_fila = load_json_file(fila_path) if os.path.exists(fila_path) else []
                if not isinstance(cur_fila, list): cur_fila = []
                cur_fila.append(payload)
                save_json_file(fila_path, cur_fila)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "total": len(cur_fila)}).encode())
                return
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode())
                return

        if parsed == "/api/toggle-queue":
            global QUEUE_PAUSED
            QUEUE_PAUSED = not QUEUE_PAUSED
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "is_paused": QUEUE_PAUSED}).encode())
            return'''

if old_toggle_queue in code:
    code = code.replace(old_toggle_queue, new_toggle_queue)

# 4. Inserir bloqueio se AUTO_RESPONDER_ENABLED estiver desligado
old_process_start = '''        lead_name = lead["name"] if lead else push_name
        company_id = lead["id"] if lead else None
        person_id = lead.get("person_id") if lead else None
        opportunity_id = lead.get("opportunity_id") if lead else None

        # 2. Qualificação Semântica com Jev (TypeSafe System One)'''

new_process_start = '''        lead_name = lead["name"] if lead else push_name
        company_id = lead["id"] if lead else None
        person_id = lead.get("person_id") if lead else None
        opportunity_id = lead.get("opportunity_id") if lead else None

        # SE AUTO-RESPONDER DESATIVADO: Apenas qualifica e prepara sugestões A/B sem disparar
        if not AUTO_RESPONDER_ENABLED:
            print(f"🔒 [MODO MANUAL SEGURO] Lead {lead_name} ({clean_phone}) respondeu: '{text}'. Sugestões A/B salvas no painel.")
            sug_a = f"Olá! Sou o Eduardo, da Vocação Comunicação aqui de Sorocaba. Vi que vocês possuem um trabalho de excelência, mas quem pesquisa pelos seus serviços no Google ainda não encontra uma vitrine digital à altura para passar confiança de primeira. O meu trabalho aqui é justamente estruturar essa autoridade visual no Maps e no celular. Como é um assunto ligado à imagem da empresa, com quem posso falar sobre isso?"
            sug_b = f"Olá! Sou o Eduardo, da Vocação aqui de Sorocaba. Analisei a busca local do segmento de vocês na nossa região e notei que quem pesquisa pelos seus serviços no Google acaba encontrando opções vizinhas antes de vocês por detalhes de otimização no Maps e ausência de canal direto rápido. Posso te enviar um resumo mostrando como posicionar a empresa como primeira escolha local?"
            PENDING_APPROVALS["last_pending"] = {
                "phone": clean_phone,
                "name": lead_name,
                "reply": sug_a,
                "reply_b": sug_b,
                "company_id": company_id,
                "person_id": person_id,
                "opportunity_id": opportunity_id
            }
            notify_admin(
                f"📩 *NOVA RESPOSTA DE LEAD (Modo Manual):*\\n"
                f"• *Lead:* {lead_name} ({clean_phone})\\n"
                f"• *Mensagem:* \\"{text}\\"\\n"
                f"• *Painel:* Sugestões A e B disponíveis em http://localhost:5680/painel"
            )
            return

        # 2. Qualificação Semântica com Jev (TypeSafe System One)'''

if old_process_start in code:
    code = code.replace(old_process_start, new_process_start)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(code)

print("main.py atualizado com sucesso com suporte ao toggle de auto-responder e A/B customizável!")
