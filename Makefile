# Loading environment variables
ifneq (,$(wildcard ./.env))
    include .env
    export LOCAL_PORT
endif

# Setting defaults for env variables
ifdef LOCAL_PORT
	local_port := $(LOCAL_PORT)
else
	local_port := 8000
endif

# Commands
checkstyle:
	poetry run pre-commit run --all-files

collectstatic:
	poetry run python manage.py collectstatic --noinput

init:
	poetry install
	poetry run pre-commit install
	poetry run python manage.py migrate
	make collectstatic
	poetry run python manage.py import_sample_data
	poetry shell

.PHONY: messages
messages:
	poetry run django-admin makemessages -l fr --ignore=manage.py,docs/*,./venv/*,./workshop/*

.PHONY: compilemessages
compilemessages:
	poetry run django-admin compilemessages

runserver:
	poetry run python manage.py runserver $(local_port)

test:
	poetry run python manage.py test

update_design_system:
	bash scripts/download_latest.sh
	poetry run python manage.py trim_dist
	poetry run python manage.py integrity_checksums
	make collectstatic

static_server:
	python -m http.server 1$(local_port) -d docs/

export_static:
	poetry run python manage.py migrate
	poetry run python manage.py import_sample_data
	poetry run python manage.py distill-local docs --force --collectstatic
	poetry run python manage.py export_json

build_packages:
	python -m build --sdist .
	python -m build --wheel .

