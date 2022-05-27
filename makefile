migrate:
	poetry run python3 manage.py migrate

migrations:
	poetry run python3 manage.py makemigrations

runserver:
	poetry run python manage.py runserver

.PHONY: migrate, makemigrations, runserver