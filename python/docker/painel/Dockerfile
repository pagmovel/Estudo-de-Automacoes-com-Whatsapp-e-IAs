FROM php:8.2-fpm-buster

# Definir diretório de trabalho
WORKDIR /var/www

# Atualizar pacotes e instalar dependências
RUN apt-get update --allow-releaseinfo-change && \
    apt-get install -y --no-install-recommends gnupg ca-certificates curl && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 0E98404D386FA1D9 6ED0E7B82643E131 F8D2585B8783D481 54404762BBB6E853 BDE6D2B9216EC7A8 && \
    apt-get update && \
    apt-get install -y \
    libpng-dev \
    zip \
    unzip \
    git \
    curl \
    libpq-dev \  
    libldap2-dev \
    libsasl2-dev \
    && docker-php-ext-install pdo_mysql gd pdo_pgsql \
    && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \
    && docker-php-ext-install ldap \
    && rm -rf /var/lib/apt/lists/*


# Instalar Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Copiar o código-fonte da aplicação
COPY . /var/www

# Definir permissões corretas
RUN chown -R www-data:www-data /var/www \
    && chmod -R 775 /var/www/storage /var/www/bootstrap/cache

EXPOSE 9000
CMD ["php-fpm"]