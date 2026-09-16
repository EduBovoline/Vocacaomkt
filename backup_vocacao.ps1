$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm"
$backupDir = "C:\Vocação 2027\Backups"
$backupFile = "$backupDir\Backup_Vocacao_$timestamp.zip"
$sourceDir = "C:\Vocação 2027\QG Vocação 2027 do zero"

Write-Host "[1/3] Criando pasta de backup se necessário..." -ForegroundColor Cyan
if (!(Test-Path $backupDir)) {
    New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
}

Write-Host "[2/3] Compactando ativos essenciais para $backupFile..." -ForegroundColor Cyan
$tempList = @(
    "$sourceDir\Site",
    "$sourceDir\1 Leads",
    "$sourceDir\2 Leads",
    "$sourceDir\Catálogo",
    "$sourceDir\MANUAL_ACESSO_GOOGLE_MAPS.md",
    "$sourceDir\MANUAL_TREINAMENTO_TOUR_VIRTUAL_GOPRO_MAX_2.md",
    "$sourceDir\PAINEL_CLIENTES_VOCACAO.md",
    "C:\Vocação 2027\Criente e portifa",
    "C:\Vocação 2027\Planilhas leads prospecção"
)

# Criar pasta temporaria para empacotar
$tempFolder = "$backupDir\temp_backup_$timestamp"
New-Item -ItemType Directory -Force -Path $tempFolder | Out-Null

foreach ($item in $tempList) {
    if (Test-Path $item) {
        $name = Split-Path -Leaf $item
        Copy-Item -Path $item -Destination "$tempFolder\$name" -Recurse -Force
    }
}

Compress-Archive -Path "$tempFolder\*" -DestinationPath $backupFile -Force
Remove-Item -Path $tempFolder -Recurse -Force

Write-Host ">>> Backup compactado gerado com sucesso: $backupFile" -ForegroundColor Green

Write-Host "[3/3] Sincronizando repositório Git local..." -ForegroundColor Cyan
Set-Location -Path $sourceDir
git add .
git commit -m "chore(backup): salvaguarda automatica consolidada $timestamp"

Write-Host "===================================================" -ForegroundColor Green
Write-Host "  BACKUP CONCLUÍDO COM SUCESSO E DADOS PROTEGIDOS!  " -ForegroundColor Green
Write-Host "===================================================" -ForegroundColor Green
