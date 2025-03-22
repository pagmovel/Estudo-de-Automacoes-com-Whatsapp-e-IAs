@echo off
REM Nome do container PostgreSQL
set CONTAINER_NAME=postgres_base_container

REM Diretório local para salvar os backups
set BACKUP_DIR=%~dp0backups
mkdir "%BACKUP_DIR%"

echo Fazendo backup do banco n8n...
docker exec -t %CONTAINER_NAME% pg_dump -U postgres -d n8n --inserts --column-inserts --clean --create > "%BACKUP_DIR%\backup_n8n.sql"

echo Fazendo backup do banco evolution...
docker exec -t %CONTAINER_NAME% pg_dump -U postgres -d evolution --inserts --column-inserts --clean --create > "%BACKUP_DIR%\backup_evolution.sql"

echo Backup concluído com sucesso!
echo Os arquivos estão salvos em: %BACKUP_DIR%

pause
