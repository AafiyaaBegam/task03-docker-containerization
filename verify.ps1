$ErrorActionPreference = "Stop"
Write-Host "== Compose services ==" -ForegroundColor Cyan
docker compose ps
Write-Host "== Health endpoint ==" -ForegroundColor Cyan
Invoke-RestMethod "http://localhost:8000/health" | ConvertTo-Json -Depth 5
Write-Host "== Image size in bytes ==" -ForegroundColor Cyan
docker image inspect task03-docker-containerization-app:local --format='{{.Size}}'
Write-Host "== Runtime user (expected 10001:10001) ==" -ForegroundColor Cyan
docker inspect task03-docker-containerization-app --format='{{.Config.User}}'
Write-Host "== App logs ==" -ForegroundColor Cyan
docker compose logs --tail=60 app
Write-Host "Record actual results; script output is not automatically proof of the image-size target." -ForegroundColor Yellow
