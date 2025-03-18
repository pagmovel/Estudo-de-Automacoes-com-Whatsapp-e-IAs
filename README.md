# Estudo Para Automacao Com Whatsapp

Nesta nova versão, criamos na raiz do projeto apenas 1 arquivo docker-compose.yaml que contém as configurações de todos os container.

Ao executar

```
docker-compose up -d --build
```

Além de construir todos os conteiner de uma vez, ele também iniciará os serviços.

O Evolution-API vai instalar o REDIS em um outro conteiner.
Acessando o gerenciador pelo link http://localhost:8104/manager/login
O gerenciador do Evolution-API vai solicitar um API Key Global\* na tela de autenticação.
Este valor está na variavel AUTHENTICATION_API_KEY do docker-composer.yml na pasta evolution-api

```
    environment:
      AUTHENTICATION_API_KEY: "bXVkZS1tZQ=="
```

Links de acesso:

- Porteiner: http://localhost:9000
- EvolutionAPI: http://localhost:8104
- n8n: http://localhost:8101
- Portgres:
  - HOST: "localhost"
  - DB: "postgres"
  - USER: "postgres"
  - PASSWORD: "postgres"
  - PORT: 5432

Caso ocorra algum erro na construção dos containers referente a banco de dados n8n/evolution-api, basta acessar o postgres, criá-lo(s) manualmente, e em segyidar executar novamente o comando docker-compose up -d --build.
