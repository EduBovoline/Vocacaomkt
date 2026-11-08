# 07 — Docker e Infraestrutura de Execução

## 1. Mapeamento de Containers e Serviços

A auditoria identificou **10 containers Docker** vinculados à operação da Vocação Comunicação & Marketing no host Windows:

| Nome do Container | Imagem | Função / Papel | Status Observado | Portas Host:Container | Origem Compose |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`twenty-server-1`** | `twentycrm/twenty:latest` | API e Interface Web do Twenty CRM | 🟢 Up (healthy) | `3000:3000` | `twenty-crm/docker-compose.yml` |
| **`twenty-worker-1`** | `twentycrm/twenty:latest` | Processamento assíncrono de filas CRM | 🟢 Up | N/A | `twenty-crm/docker-compose.yml` |
| **`twenty-db-1`** | `postgres:16` | Banco de dados relacional Twenty CRM | 🟢 Up (healthy) | `5432` (interno) | `twenty-crm/docker-compose.yml` |
| **`twenty-redis-1`** | `redis:latest` | Cache e mensageria interna do CRM | 🟢 Up (healthy) | `6379` (interno) | `twenty-crm/docker-compose.yml` |
| **`vocacao-evolution-api`** | `evoapicloud/evolution-api:latest` | Motor WhatsApp (Baileys/Node.js) | 🟢 Up | `8080:8080` | `D:\Funnel vendas objeção\local_stack` |
| **`vocacao-postgres-evolution`**| `postgres:15-alpine` | Banco de dados da Evolution API | 🟢 Up | `5432` (interno) | `D:\Funnel vendas objeção\local_stack` |
| **`vocacao-redis-evolution`** | `redis:alpine` | Cache de sessões WhatsApp | 🟢 Up | `6379:6379` | `D:\Funnel vendas objeção\local_stack` |
| **`vocacao-n8n`** | `n8nio/n8n:latest` | Orquestrador visual de automações | 🟢 Up | `5678:5678` | `D:\Funnel vendas objeção\local_stack` |
| **`serpbear-serpbear-1`** | `towfiqi/serpbear:latest` | Monitoramento de posições de SEO no Google | 🟢 Up | `5000:3000` | `serpbear/docker-compose.yml` |
| **`vocacao-auto-responder`** | `auto_responder_docker-auto-responder` | Webhook, Auto-Responder e Sub-CRM | 🔴 **Exited (127)** | `5680:5680`, `8000:5680` | `operacoes/auto_responder_docker` |

---

## 2. Diagnóstico da Falha no Container `vocacao-auto-responder`

O container central da prospecção encontra-se **interrompido (Exit Code 127)** há 11 dias.

### Evidência Extraída do Docker Inspect:
```json
{
  "State": {
    "ExitCode": 127,
    "FinishedAt": "2026-10-20T14:59:09.976786587Z",
    "Error": "failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: error mounting \"/run/desktop/mnt/host/c/Vocação 2027/QG Vocação 2027 do zero/auto_responder_docker/main.py\" to rootfs at \"/app/main.py\": mount src=/run/desktop/mnt/host/c/Vocação 2027/QG Vocação 2027 do zero/auto_responder_docker/main.py, dst=/app/main.py, dstFd=/proc/thread-self/fd/14, flags=MS_BIND|MS_REC: not a directory: Are you trying to mount a directory onto a file (or vice-versa)?"
  }
}
```

### Causa-Raiz do Erro:
O arquivo `docker-compose.yml` de `operacoes/auto_responder_docker` possui o seguinte bind mount:
```yaml
volumes:
  - ./data:/app/data
  - ../2 Leads:/app/leads:ro
  - ./main.py:/app/main.py
  - ./templates:/app/templates
```
Quando o projeto foi movido para o repositório worktree atual (`C:\Users\edubo\.gemini\antigravity\worktrees\QG Vocação 2027 do zero\audit_prospecting_system_vocacao`), o Docker Desktop manteve na configuração do container o caminho antigo `c/Vocação 2027/QG Vocação 2027 do zero/...`. Como esse caminho deixou de existir, o Docker criou um diretório fantasma e travou a inicialização com código 127.

---

## 3. Redes Docker e Comunicação Inter-Containers

O ecossistema utiliza duas redes externas compartilhadas:
- **`local_stack_default`:** Conecta a Evolution API, Redis e Postgres da automação conversacional.
- **`twenty_default`:** Conecta o servidor do Twenty CRM, worker, Postgres 16 e Redis.

O `vocacao-auto-responder` foi configurado para conectar em ambas as redes (`local_stack_default` e `twenty_default`), permitindo que chamadas internas alcancem:
- `http://vocacao-evolution-api:8080` (WhatsApp)
- `twenty-db-1:5432` (Banco do Twenty CRM)

---

## 4. Componentes Executados Fora do Docker (Ambiente Host)

1. **Geração de PDF e Layout Watanabe:**
   - Executado via Node.js local (`node generate_lead.js` e `node convert_pdf.js`).
   - Requer acesso ao executável local do Google Chrome (`C:\Program Files\Google\Chrome\Application\chrome.exe`).
2. **Scripts Batch e Disparadores Python:**
   - `operacoes/disparador_fila_*.py` rodam sob o interpretador Python do Windows.
   - Comunicação com a Evolution API é feita através de `http://localhost:8080`.
   - Comunicação com o Twenty CRM é feita chamando `docker exec -i twenty-db-1 psql`.
3. **Resolução de Mapas:**
   - `resolve_maps.js` roda no runtime Node.js nativo.

---

## 5. Inconsistência nos Scripts de Inicialização (.bat)

O script unificado `operacoes/INICIAR_TODAS_FERRAMENTAS.bat` apresenta um erro de localização de diretórios:
- Linha 9: `cd /d "%~dp0twenty-crm"`
- Linha 17: `cd /d "%~dp0openseo"`
- Linha 19: `cd /d "%~dp0serpbear"`
Como o arquivo está na pasta `operacoes/`, `%~dp0twenty-crm` tenta abrir `operacoes\twenty-crm\`, que **não existe** (as pastas estão na raiz do projeto). Se executado a partir de `operacoes\`, o script falha silenciosamente na subida dessas três ferramentas.
