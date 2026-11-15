# Lab 9 — API REST com Flask e FastAPI

Laboratório 9 de Engenharia de Software (Mackenzie): a mesma API REST de itens feita em Flask e em FastAPI, com testes no Postman, Docker e deploy na Azure.

## Links (9.3 a 9.6)

| Exercício | Código | Aplicação online |
|---|---|---|
| 9.3 Flask e Nuvem (Hello World) | [`flask-azure/`](flask-azure) | https://engsoft-lab9-flask.azurewebsites.net |
| 9.4 Flask e Nuvem (API REST) | [`flask-azure/app.py`](flask-azure/app.py) | https://engsoft-lab9-flask.azurewebsites.net/items |
| 9.5 FastAPI e Docker | [`fastapi-docker/`](fastapi-docker) | local: http://127.0.0.1:8000/items |
| 9.6 FastAPI, Docker e Deploy | [`fastapi-docker/`](fastapi-docker) | https://engsoft-lab9-fastapi.azurewebsites.net/items |

- Pipelines de CI/CD: [`.github/workflows/flask-azure.yml`](.github/workflows/flask-azure.yml) e [`.github/workflows/fastapi-docker-azure.yml`](.github/workflows/fastapi-docker-azure.yml) ([execuções](https://github.com/HenriqueRSouza/eng-software-lab-9-api-rest/actions)).
- Imagem Docker: `ghcr.io/henriquersouza/lab9-fastapi`.
- Coleção do Postman: [`postman/lab9-nuvem-docker.postman_collection.json`](postman/lab9-nuvem-docker.postman_collection.json).
- Prints: pasta [`prints/`](prints).

### Como funciona o deploy

- **Flask (9.3/9.4)**: a cada push em `flask-azure/`, o GitHub Actions instala as dependências, testa o app e faz o deploy do código na Azure App Service (Linux, Python 3.12, plano F1 gratuito). O app roda com `gunicorn app:app`.
- **FastAPI (9.6)**: a cada push em `fastapi-docker/`, o GitHub Actions faz o build da imagem, publica no GitHub Container Registry, testa o container e atualiza a Azure App Service (container, plano F1 gratuito) para a nova imagem.

### Docker local (9.5)

```bash
cd fastapi-docker
docker build -t lab9-fastapi .
docker run -d --name lab9-fastapi -p 8000:8000 lab9-fastapi
curl http://127.0.0.1:8000/items
```

## Prints
Prints tirados da tela com o código rodando e o resultado, organizados por exercício.

### 9.3 Flask e Nuvem (Hello World)

- [01 codigo hello world](prints/9.3/01-codigo-hello-world.png)
- [02 repositorio github](prints/9.3/02-repositorio-github.png)
- [03 ambiente azure app service](prints/9.3/03-ambiente-azure-app-service.png)
- [04 pipeline cicd pycharm](prints/9.3/04-pipeline-cicd-pycharm.png)
- [05 pipeline cicd workflow](prints/9.3/05-pipeline-cicd-workflow.png)
- [06 pipeline execucao terminal](prints/9.3/06-pipeline-execucao-terminal.png)
- [07 pipeline execucao github](prints/9.3/07-pipeline-execucao-github.png)
- [08 pagina online](prints/9.3/08-pagina-online.png)

### 9.4 Flask e Nuvem (API REST)

- [01 api flask pycharm](prints/9.4/01-api-flask-pycharm.png)
- [02 api flask codigo](prints/9.4/02-api-flask-codigo.png)
- [03 commit e deploy automatico](prints/9.4/03-commit-e-deploy-automatico.png)
- [04 deploy automatico github](prints/9.4/04-deploy-automatico-github.png)
- [05 api online navegador](prints/9.4/05-api-online-navegador.png)
- [06 api online curl](prints/9.4/06-api-online-curl.png)
- [07 testes postman](prints/9.4/07-testes-postman.png)

### 9.5 FastAPI e Docker

- [01 api fastapi pycharm](prints/9.5/01-api-fastapi-pycharm.png)
- [02 api fastapi codigo](prints/9.5/02-api-fastapi-codigo.png)
- [03 dockerignore pycharm](prints/9.5/03-dockerignore-pycharm.png)
- [04 dockerfile pycharm](prints/9.5/04-dockerfile-pycharm.png)
- [05 dockerignore e dockerfile](prints/9.5/05-dockerignore-e-dockerfile.png)
- [06 docker build](prints/9.5/06-docker-build.png)
- [07 docker run e teste](prints/9.5/07-docker-run-e-teste.png)
- [08 docker swagger navegador](prints/9.5/08-docker-swagger-navegador.png)
- [09 docker items navegador](prints/9.5/09-docker-items-navegador.png)
- [10 testes postman](prints/9.5/10-testes-postman.png)

### 9.6 FastAPI, Docker e Deploy

Os passos 1 a 4 do 9.6 (API FastAPI, imagem Docker, execução local e testes no Postman) são os mesmos do 9.5. Veja os prints em [`prints/9.5`](prints/9.5).

- [01 pipeline cicd pycharm](prints/9.6/01-pipeline-cicd-pycharm.png)
- [02 pipeline cicd workflow](prints/9.6/02-pipeline-cicd-workflow.png)
- [03 commit e deploy automatico](prints/9.6/03-commit-e-deploy-automatico.png)
- [04 deploy automatico github](prints/9.6/04-deploy-automatico-github.png)
- [05 imagem docker ghcr](prints/9.6/05-imagem-docker-ghcr.png)
- [06 ambiente azure container](prints/9.6/06-ambiente-azure-container.png)
- [07 api online swagger](prints/9.6/07-api-online-swagger.png)
- [08 api online items](prints/9.6/08-api-online-items.png)
- [09 testes postman](prints/9.6/09-testes-postman.png)

## Arquivos

- `default.py`: Hello World com Flask
- `rest.py`: API REST (CRUD) de itens com Flask
- `fastapi-default.py`: Hello World com FastAPI
- `fastapi-rest.py`: a mesma API REST de itens com FastAPI
- `postman/lab9-api-rest.postman_collection.json`: collection do Postman com os testes das duas APIs
- `flask-azure/`: app Flask (Hello World + API REST) publicado na Azure (9.3 e 9.4)
- `fastapi-docker/`: API FastAPI com `Dockerfile` e `.dockerignore` (9.5 e 9.6)
- `postman/lab9-nuvem-docker.postman_collection.json`: testes das APIs na Azure e no Docker

Os dados ficam em memória: ao reiniciar o servidor, a lista volta aos 2 itens iniciais.

## Como rodar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

| Arquivo | Comando | Endereço |
|---|---|---|
| `default.py` | `python default.py` | http://127.0.0.1:5001 |
| `rest.py` | `python rest.py` | http://127.0.0.1:5001/items |
| `fastapi-default.py` | `uvicorn fastapi-default:app --reload` | http://127.0.0.1:8000 |
| `fastapi-rest.py` | `uvicorn fastapi-rest:app --reload` | http://127.0.0.1:8000/items |

O Flask usa a porta 5001 porque, no macOS, a porta 5000 é reservada pelo AirPlay.
No FastAPI, a página http://127.0.0.1:8000/docs permite testar as rotas pelo navegador.

## Rotas

| Método | Rota | Descrição |
|---|---|---|
| GET | `/items` | Lista todos os itens |
| GET | `/items/<id>` | Busca um item pelo id |
| POST | `/items` | Cria um item (`{"name": "..."}`) |
| PUT | `/items/<id>` | Atualiza o nome de um item |
| DELETE | `/items/<id>` | Remove um item |

Respostas de erro:

| Situação | Flask | FastAPI |
|---|---|---|
| Item não existe | `404` `{"error": "Item not found"}` | `404` `{"detail": "Item not found"}` |
| POST/PUT sem `name` | `400` `{"error": "Field 'name' is required"}` | `422` com o detalhe da validação |

## Testes no Postman

1. No Postman, clique em **Import** e escolha `postman/lab9-api-rest.postman_collection.json`.
2. Suba as duas APIs (`python rest.py` e `uvicorn fastapi-rest:app --reload`).
3. Use **Run collection**.

São 11 requisições por API, com 44 testes no total (status e conteúdo da resposta).
Cada requisição também tem um **Example** com a resposta real gravada durante a execução dos testes.

## Exemplos com curl

```bash
curl http://127.0.0.1:5001/items
curl -X POST http://127.0.0.1:5001/items -H "Content-Type: application/json" -d '{"name": "Item 3"}'
curl -X PUT http://127.0.0.1:5001/items/1 -H "Content-Type: application/json" -d '{"name": "Novo nome"}'
curl -X DELETE http://127.0.0.1:5001/items/2
```

Para o FastAPI, troque a porta por `8000`.
