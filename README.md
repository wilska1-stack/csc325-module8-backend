# CSC325 Module 8 Backend

A small Django + Django REST Framework API with two endpoints:

- `GET /api/health/` returns `{"status": "ok"}`
- `GET /api/greeting/?name=<name>` returns `{"message": "Hello, <name>!"}`

## Run the tests

```bash
python3 -m pip install -r requirements.txt
python3 manage.py test -v 2
```
