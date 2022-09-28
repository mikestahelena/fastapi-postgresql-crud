# fastapi-postgresql-crud

This is a simple CRUD application using FastAPI and PostgreSQL.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
uvicorn main:app --reload
```

```bash
chmod +x project/entrypoint.sh
```

```bash
docker-compose up -d --build
```

```bash
docker-compose logs web
```

```bash
docker-compose exec web-db psql -U postgres
```
\c web_dev
\dt
select * from customer; (If generate_schemas=True table exists)

Initialize the database:

```bash
docker-compose exec web aerich init -t app.db.TORTOISE_ORM
```

```bash
docker-compose exec web aerich init-db
```

```bash
docker-compose exec web python -m pytest
```

autopep8 --in-place --aggressive --aggressive project/app/*.py -v
