# Estudo Para Automacao Com Whatsapp

Nesta nova versão, criamos na raiz do projeto apenas 1 arquivo docker-compose.yaml que contém as configurações de todos os container.

Ao executar

```
docker-compose up -d --build
```

Além de construir todos os container de uma vez, ele também iniciará os serviços.

O Evolution-API vai instalar o REDIS em um outro container.
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


### Instalando Node do Evolutio-API

Mesmo adicionando o node dentro de Settings->Community nodes->n8n-nodes-evolution-api, ele não aparecia na lista de nodes quando tentava buscar para criar a conexão.
A solução foi instalar manualmente dentro do container da seguinte forma:
```
docker exec -it n8n_container sh
cd /home/node/.n8n
npm install n8n-nodes-evolution-api
```
No final da instalação vai ter algo parecido com estas linhas:
```
+ n8n-nodes-evolution-api@x.y.z
added x packages from y contributors
```
Saia do container:
```
exit
```
Reinicie o container para que o n8n carregue o novo node:
```
docker restart n8n_container
```

