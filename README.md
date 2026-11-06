# Lab 9 — API REST com Flask e FastAPI

Laboratório 9 de Engenharia de Software (Mackenzie): a mesma API REST de itens feita em Flask e em FastAPI, com testes no Postman.

## Arquivos

- `default.py`: Hello World com Flask
- `rest.py`: API REST (CRUD) de itens com Flask
- `fastapi-default.py`: Hello World com FastAPI
- `fastapi-rest.py`: a mesma API REST de itens com FastAPI
- `postman/lab9-api-rest.postman_collection.json`: collection do Postman com os testes das duas APIs

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
