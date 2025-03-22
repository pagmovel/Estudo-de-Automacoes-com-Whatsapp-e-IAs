@echo off
REM Nome do container PostgreSQL
set CONTAINER_NAME=postgres_base_container

REM Caminho dos arquivos de backup
set BACKUP_DIR=%~dp0backups
set BACKUP_N8N=%BACKUP_DIR%\backup_n8n.sql
set BACKUP_EVOLUTION=%BACKUP_DIR%\backup_evolution.sql

REM Verificação dos arquivos
if not exist "%BACKUP_N8N%" (
    echo Arquivo de backup do n8n não encontrado: %BACKUP_N8N%
    pause
    exit /b
)

if not exist "%BACKUP_EVOLUTION%" (
    echo Arquivo de backup do evolution não encontrado: %BACKUP_EVOLUTION%
    pause
    exit /b
)

echo Restaurando banco n8n...
type "%BACKUP_N8N%" | docker exec -i %CONTAINER_NAME% psql -U postgres

echo Restaurando banco evolution...
type "%BACKUP_EVOLUTION%" | docker exec -i %CONTAINER_NAME% psql -U postgres

echo Restauração concluída com sucesso!
pause
