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

3. **Acesse a documentação da API em seu navegador:**

    ```
    http://localhost:8080/docs
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

