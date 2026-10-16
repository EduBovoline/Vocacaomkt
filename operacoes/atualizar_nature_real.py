import subprocess

SCHEMA = "workspace_2xmx8hech9nybwidia3404k2z"

sql = f"""
UPDATE "{SCHEMA}"."company"
SET 
    name = 'Espaço Naturê',
    "domainNamePrimaryLinkLabel" = 'Onboarding Oficial',
    "domainNamePrimaryLinkUrl" = 'vocacao.digital/espaconature',
    "addressAddressStreet1" = 'Av. Miguel Achiole da Fonseca, 1484 - 1º Andar',
    "addressAddressStreet2" = 'Jardim São Paulo (Zona Leste)',
    "addressAddressCity" = 'São Paulo',
    "addressAddressState" = 'SP',
    "addressAddressCountry" = 'Brasil',
    "addressAddressPostcode" = '08460-010',
    "annualRevenueAmountMicros" = 180000000000,
    "annualRevenueCurrencyCode" = 'BRL',
    "linkedinLinkPrimaryLinkLabel" = 'Instagram Oficial',
    "linkedinLinkPrimaryLinkUrl" = 'https://instagram.com/espaconatureoficial'
WHERE id = '3e5c0c5d-b68f-4bbf-8ff2-31451af10ef9';

UPDATE "{SCHEMA}"."person"
SET
    "nameFirstName" = 'Miriam',
    "nameLastName" = 'Naturê',
    "jobTitle" = 'Proprietária & Gestora',
    "phonesPrimaryPhoneNumber" = '(11) 99139-4281',
    "emailsPrimaryEmail" = 'contato@espaconature.com.br'
WHERE "companyId" = '3e5c0c5d-b68f-4bbf-8ff2-31451af10ef9';

UPDATE "{SCHEMA}"."opportunity"
SET
    name = 'Onboarding Estratégico & Google Maps - Espaço Naturê',
    "amountAmountMicros" = 1500000000,
    "amountCurrencyCode" = 'BRL',
    stage = 'CUSTOMER'
WHERE "companyId" = '3e5c0c5d-b68f-4bbf-8ff2-31451af10ef9';
"""

proc = subprocess.Popen(
    ["C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe", "exec", "-i", "twenty-db-1", "psql", "-U", "postgres", "-d", "twenty"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    encoding="utf-8"
)
out, err = proc.communicate(input=sql)
print("OUT:", out)
if err:
    print("ERR:", err)
