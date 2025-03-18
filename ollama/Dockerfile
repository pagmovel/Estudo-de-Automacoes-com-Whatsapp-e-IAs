# Usando uma imagem base do Python
FROM python:3.9

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y curl unzip

# Baixar e instalar o Ollama corretamente
RUN curl -fsSL https://ollama.com/install.sh -o install.sh && \
    chmod +x install.sh && \
    ./install.sh && \
    rm install.sh

# Definir diretório de trabalho
WORKDIR /app

# Copiar os arquivos para dentro do container
COPY requirements.txt ollama_script.py ./

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask

# Expor a porta da API Flask
EXPOSE 5000

# Rodar o script automaticamente
CMD ["python", "ollama_script.py"]
