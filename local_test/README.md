# Instruções para Uso do Docker Compose e Redis

Este documento fornece instruções sobre como usar o Docker Compose e interagir com o Redis em um ambiente de desenvolvimento.

## Alterar Redis info no config.py
REDIS_HOST = "redis" # tem que ter o nome do nosso container que no caso é esse mesmo
REDIS_PORT = int("6379")
REDIS_DB = int("0")
REDIS_PASSWORD = "ignore"

## Alterar arquivo main.py
Comentar a linha que contem o password do redis
```password=config.REDIS_PASSWORD,```


## Alterar arquivo redis_cache

Comentar a linha que contem o password do redis
```password=config.REDIS_PASSWORD,```

## Adicionar no arquivo satellite.py a linha

```logger.add(sys.stdout, level="DEBUG")```

Para ver logs de nível DEBUG

## Copiar Dockerfile da pasta "local_test" para o diretório imediatamente superior

## Construir a Imagem

Para construir a imagem do Docker, você pode usar um dos seguintes comandos:

- Se estiver na mesma pasta que o `docker-compose.yml`:
  ```bash
  sudo docker-compose build
  ```

- Se o arquivo `docker-compose.yml` estiver localizado em `local_test`:
  ```bash
  sudo docker-compose -f local_test/docker-compose.yml build
  ```

## Listar Imagens

Para pegar o nome da imagem construída, você pode usar o seguinte comando:

```bash
docker images
```


## Executar o Contêiner

Para executar um contêiner, substitua a última palavra do comando abaixo pelo nome da imagem que você deseja usar:

```
bash
docker run -it --rm -p 8080:80 --env-file .env --link my-redis:redis plataforma-clima-api_app
```


## Acessar a Linha de Comando do Contêiner

Para acessar a linha de comando do contêiner, use o seguinte comando:


```
bash
docker run -it plataforma-clima-api_app /bin/bash
```


## Fazer Requisições HTTP

Para fazer uma requisição GET para o endpoint de informações do satélite, use o comando `curl`:

```
bash
curl -X 'GET' 'http://localhost:80/satellite/info/cp' -H 'accept: application/json'
```


## Acessar o Redis

Para acessar o Redis a partir de um contêiner, use o seguinte comando:

```
bash
docker run -it --network plataforma-clima-api_default --rm redis redis-cli -h redis -p 6379
```

### Acessar o Redis Internamente

- tem uma forma mais fácil, mas não funcionou

1. Descubra o IP interno do contêiner Redis com o seguinte comando:

   ```bash
   docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <nome_do_conteiner_redis>
   ```

2. Use o IP obtido para acessar o Redis:

   ```bash
   docker run -it --network plataforma-clima-api_default --rm redis redis-cli -h <ip_do_conteiner_redis> -p 6379
   ```

## Parar os Contêineres

Para parar e remover todos os contêineres definidos no `docker-compose.yml`, use:

```
bash
sudo docker-compose down
```
