.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python -m bi360.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m bi360.manage makemigrations

.PHONY: collectstatic
collectstatic:
	poetry run python -m bi360.manage collectstatic --clear --no-input

.PHONY: run-server
run-server:
	poetry run python -m bi360.manage runserver

.PHONY: run-prod
run-prod:
	poetry run gunicorn bi360.project.wsgi:application --bind 0.0.0.0:8000 --timeout 1200

.PHONY: run-prod-daemon
run-prod-daemon:
	poetry run gunicorn bi360.project.wsgi:application --bind 0.0.0.0:8000 --timeout 1200 --daemon

.PHONY: superuser
superuser:
	poetry run python -m bi360.manage createsuperuser

.PHONY: update
update: install migrate install-pre-commit;
