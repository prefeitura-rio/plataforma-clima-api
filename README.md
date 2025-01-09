# Plataforma Clima API

Este projeto é uma API que pode ser executada em um contêiner Docker ou localmente.

## Pré-requisitos

- Docker instalado ou
- Python e a ferramenta `uv` instalados para execução local

## Configuração do ambiente

1. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

    ```env
    INFISICAL_ADDRESS=<seu_endereço_infisical>
    INFISICAL_TOKEN=<seu_token_infisical>
    ```

    Substitua `<seu_endereço_infisical>` e `<seu_token_infisical>` pelos valores apropriados.

## Executando com Docker

1. **Construa a imagem Docker:**

    ```bash
    docker build -t test .
    ```

2. **Execute o contêiner Docker:**

    ```bash
    docker run -it --rm -p 8080:80 --env-file .env test
    ```

## Executando com Docker + Redis

1. **Construa a imagem Docker:**

    ```bash
    docker build -t test .
    ```

2. **Execute o contêiner Redis:** Primeiro, você deve iniciar o contêiner Redis. Você pode usar o seguinte comando para executar o Redis em um contêiner Docker, expondo a porta 6379:

    ```bash
    docker run --name my-redis -p 6379:6379 -d redis
    ```

3. **Executar o Contêiner da API:** Em seguida, você pode executar o contêiner da sua API, garantindo que ele possa se conectar ao Redis. Se a sua API estiver configurada para se conectar ao Redis em localhost, você precisará alterar isso para o nome do contêiner Redis (my-redis), pois os contêineres Docker podem se comunicar entre si usando os nomes dos contêineres.

    ```bash
    docker run -it --rm -p 8080:80 --env-file .env --link my-redis:test test
    ```

4. **Configurar a Conexão com o Redis na API:** Certifique-se de que a sua aplicação está configurada para se conectar ao Redis usando o nome do contêiner. Por exemplo, se você estiver usando Python com a biblioteca redis-py, a conexão deve ser assim:

```python
import redis

# Conectar ao Redis usando o nome do contêiner
r = redis.Redis(host='localhost', port=6379, db=0)
```

5. **Acesse a documentação da API em seu navegador:**

    ```
    http://localhost:8080/docs
    ```

6. **Acessar o Redis:** Para interagir com o Redis, você pode usar um cliente Redis local ou um cliente de linha de comando dentro do contêiner Redis:

```bash
docker exec -it my-redis redis-cli
```

## Executando Localmente com `uv`

Se preferir rodar localmente:

1. Ative seu ambiente virtual (caso use um).
2. Instale as dependências conforme necessário.

3. **Execute o servidor localmente usando o `uv`:**

    ```bash
    uv run task serve
    ```

4. Acesse a documentação da API em:

    ```
    http://localhost:8080/docs
    ```

