# === CONFIGURATION ===
$projectPath = "C:\Python\Projects\Politibot"
$archivePath = "$projectPath\Archives"

# Crée le dossier Archives s'il n'existe pas
if (!(Test-Path $archivePath)) {
    New-Item -ItemType Directory -Path $archivePath | Out-Null
}

# === VERSIONING ===
# Version basée sur la date : ex : 2025-02
$version = (Get-Date -Format "yyyy-MM")

# Nom du fichier ZIP
$zipName = "Politibot-$version.zip"
$zipFullPath = "$archivePath\$zipName"

# === ARCHIVAGE ===
Write-Host "Archivage de la version $version..."

# Supprime l’archive si elle existe déjà
if (Test-Path $zipFullPath) {
    Remove-Item $zipFullPath -Force
}

# Crée l’archive ZIP
Compress-Archive -Path "$projectPath\*" -DestinationPath $zipFullPath

Write-Host "Archive creee : $zipFullPath"

# === FIN ===
Write-Host "Archivage termine. Vous pouvez maintenant mettre a jour Politibot."