# Dockerfile
FROM python:3.9-buster

WORKDIR /app

# Copiar requirements.txt primeiro para aproveitar o cache do Docker
COPY requirements.txt requirements.txt

# Atualizar pip e instalar dependências Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar o resto do código da aplicação
COPY . /app

# Copiar o arquivo do Google Chrome baixado localmente para o container
COPY google-chrome-stable_114.0.5735.90-1_amd64.deb /tmp/google-chrome.deb

# Instalar dependências adicionais do sistema, locais e cron
RUN apt-get update && apt-get -y install \
    gcc make locales cron nano vim wget unzip fontconfig \
    libx11-xcb1 libxcomposite1 libxcursor1 libxdamage1 libxi6 libxtst6 libnss3 libxrandr2 \
    libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxss1 libasound2 libgbm1 libgtk-3-0 \
    libxshmfence1 xdg-utils fonts-liberation libu2f-udev libvulkan1 \
    && rm -rf /var/lib/apt/lists/*

# Definir localidade
RUN sed -i '/pt_BR.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt
ENV LC_ALL pt_BR.UTF-8

# Definir variáveis de ambiente
ENV SQLALCHEMY_WARN_20=1
ENV SQLALCHEMY_SILENCE_UBER_WARNING=1

# Definir variáveis de ambiente para suprimir avisos
ENV SQLALCHEMY_WARN_20 0
ENV SQLALCHEMY_SILENCE_UBER_WARNING 1

# Instalar o Google Chrome
RUN dpkg -i /tmp/google-chrome.deb || apt-get -f install -y \
    && rm /tmp/google-chrome.deb

# Bloquear a versão do Google Chrome para evitar atualizações
RUN echo "google-chrome-stable hold" | dpkg --set-selections

# Adicionar Google Chrome ao PATH
ENV PATH="/usr/bin/google-chrome-stable:$PATH"

# Instalar Chromedriver
RUN apt-get install -y tzdata
ENV TZ="America/Fortaleza"
RUN apt-get install -yqq unzip
# RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
COPY chromedriver_linux64.zip /tmp/chromedriver.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
RUN rm /tmp/chromedriver.zip

# Copiar o arquivo de crontab para o local apropriado e definir permissões
COPY crontab /etc/cron.d/hello-cron
RUN chmod 0644 /etc/cron.d/hello-cron

# Criar arquivos de log para poder rodar tail
RUN touch /var/log/cron.log /var/log/cronCapturaEmails.log

# Aplicar o crontab
RUN crontab /etc/cron.d/hello-cron

# Definir o fuso horário para o cron
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Expor porta para o serviço Python
EXPOSE 8000

# Iniciar o serviço cron e o processo principal (script Python)
CMD ["sh", "-c", "cron & uvicorn api:app --host 0.0.0.0 --port 8000 --reload & tail -f /var/log/cron.log /var/log/cron_app.log"]


