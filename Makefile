format:
	uv run ruff format .

fix:
	uv run ruff check --fix .

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs

migrations:
	docker compose exec main-app alembic revision --autogenerate

migrate:
	docker compose exec main-app alembic upgrade +1
