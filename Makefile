.PHONY: venv devdeps deps dev prod
venv:
	python -m venv .venv --prompt='Treehouse Virtual Environment'
dev:
	cd src/treehouse && python manage.py runserver
prod:
	cd src/treehouse && uvicorn --no-server-header --workers `nproc` treehouse.asgi:application
devdeps:
	python -m pip install -U pip-tools
	pip-compile requirements/dev.in -o requirements/dev.txt
	pip-sync requirements/dev.txt

deps:
	python -m pip install -U pip-tools
	pip-compile requirements/deps.in -o requirements/deps.txt
	pip-sync requirements/deps.txt