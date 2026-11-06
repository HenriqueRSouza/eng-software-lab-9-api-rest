# Lab 9 — API REST com Flask

Laboratório 9 de Engenharia de Software (Mackenzie): uma API REST simples com Flask.

## Arquivos

- `default.py`: Hello World com Flask
- `rest.py`: API REST (CRUD) de itens, com os dados guardados em memória

## Como rodar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python rest.py
```

O servidor sobe em http://127.0.0.1:5001. A porta 5000 não é usada porque o macOS a reserva para o AirPlay.

## Rotas

| Método | Rota | Descrição |
|---|---|---|
| GET | `/items` | Lista todos os itens |
| GET | `/items/<id>` | Busca um item pelo id |
| POST | `/items` | Cria um item (`{"name": "..."}`) |
| PUT | `/items/<id>` | Atualiza o nome de um item |
| DELETE | `/items/<id>` | Remove um item |

## Exemplos

```bash
curl http://127.0.0.1:5001/items
curl -X POST http://127.0.0.1:5001/items -H "Content-Type: application/json" -d '{"name": "Item 3"}'
curl -X PUT http://127.0.0.1:5001/items/1 -H "Content-Type: application/json" -d '{"name": "Novo nome"}'
curl -X DELETE http://127.0.0.1:5001/items/2
```
