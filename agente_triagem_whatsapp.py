import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import re
import urllib.parse
import webbrowser
import time
from pathlib import Path

LEADS_DIR = Path(r"C:\Vocação 2027\QG Vocação 2027 do zero\2 Leads")

def sanitize_phone(phone_str):
    if not phone_str:
        return None
    clean = re.sub(r"\D", "", phone_str)
    if clean.startswith("55"):
        num = clean[2:]
    else:
        num = clean
    
    # Validações
    if "99999" in num or "00000" in num or num.startswith("12345") or len(num) < 10 or len(num) > 11:
        return None
    return "55" + num

def extract_pitch_from_dossie(dossie_path):
    try:
        with open(dossie_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Procurar link do WhatsApp já formatado
        match_wa = re.search(r'href="https://api\.whatsapp\.com/send\?phone=[^&]*&text=([^"]+)"', content)
        if match_wa:
            return urllib.parse.unquote(match_wa.group(1))
        
        # Fallback de script
        match_script = re.search(r'class="script-box"[^>]*>([\s\S]*?)</div>', content)
        if match_script:
            clean_txt = re.sub(r'<[^>]+>', '', match_script.group(1)).strip()
            return clean_txt
    except Exception as e:
        pass
    return None

def analyze_leads():
    triaged = []
    print("\n" + "="*65)
    print(" 🤖 AGENTE VOCAÇÃO: TRIAGEM INTELIGENTE DE LEADS (PASTA 2 LEADS)")
    print("="*65)

    for item in sorted(LEADS_DIR.iterdir()):
        if not item.is_dir():
            continue
        
        lead_name = item.name
        dossies = list(item.glob("dossie-interno*.html"))
        reports = list(item.glob("Análise de Presença*.html"))
        
        status = "REPROVADO"
        phone = None
        pitch = None
        motivo = ""

        if not dossies:
            motivo = "Dossiê interno ausente"
        else:
            dossie = dossies[0]
            # Tentar extrair telefone do nome do arquivo
            match_phone = re.search(r'dossie-interno-.*?-([0-9]+)\.html', dossie.name)
            raw_phone = match_phone.group(1) if match_phone else None
            phone = sanitize_phone(raw_phone)
            
            if not phone:
                motivo = f"Telefone inválido ou temporário ({raw_phone or 'sem número'})"
            else:
                pitch = extract_pitch_from_dossie(dossie)
                if not pitch:
                    # Pitch padrão humanizado Vocação
                    pitch = f"Olá, tudo bem? Aqui é o Edu da Vocação Digital de Sorocaba. Fizemos um diagnóstico técnico do posicionamento online da {lead_name} e mapeamos pontos importantes para atrair mais clientes locais. Você é o responsável pelo atendimento?"
                status = "APROVADO"

        triaged.append({
            "name": lead_name,
            "status": status,
            "phone": phone,
            "pitch": pitch,
            "motivo": motivo,
            "folder": str(item)
        })

    # Exibir resumo da triagem
    aprovados = [l for l in triaged if l["status"] == "APROVADO"]
    reprovados = [l for l in triaged if l["status"] == "REPROVADO"]

    print(f"\n✅ LEADS APROVADOS PARA DISPARO ({len(aprovados)}):")
    for i, lead in enumerate(aprovados, 1):
        print(f" [{i}] {lead['name']}")
        print(f"     📞 WhatsApp: +{lead['phone']}")
        print(f"     💬 Prévia: {lead['pitch'][:75]}...")

    print(f"\n⚠️ LEADS COM TRIAGEM PENDENTE ({len(reprovados)}):")
    for lead in reprovados:
        print(f"  • {lead['name']}: {lead['motivo']}")

    print("\n" + "="*65)
    return aprovados, reprovados

def send_via_chrome(lead):
    encoded_text = urllib.parse.quote(lead["pitch"])
    url = f"https://web.whatsapp.com/send?phone={lead['phone']}&text={encoded_text}"
    print(f"\n🚀 Abrindo WhatsApp no Chrome para: {lead['name']} (+{lead['phone']})")
    webbrowser.open(url)

if __name__ == "__main__":
    aprovados, _ = analyze_leads()
    if not aprovados:
        print("Nenhum lead aprovado para envio no momento.")
    else:
        print("\nOPÇÕES DE EXECUÇÃO:")
        print(" [1] Disparar o PRIMEIRO lead aprovado no Chrome agora")
        print(" [2] Disparar TODOS os leads aprovados (com intervalo de 10s)")
        print(" [3] Apenas gerar painel de disparo")
        
        choice = input("\nEscolha uma opção (1, 2 ou 3): ").strip()
        if choice == "1":
            send_via_chrome(aprovados[0])
        elif choice == "2":
            for lead in aprovados:
                send_via_chrome(lead)
                time.sleep(10)
        else:
            print("Triagem concluída. Pronto para execução.")


