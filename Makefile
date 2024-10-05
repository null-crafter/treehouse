.PHONY: venv devdeps deps dev prod
venv:
	python -m venv .venv --prompt='Treehouse Virtual Environment'
dev:
	cd src/treehouse && DEBUG=True python manage.py runserver 127.0.0.1:9000
prod:
	cd src/treehouse && gunicorn -b 127.0.0.1:9000 -k gevent --workers `nproc` treehouse.wsgi:application
devdeps:
	python -m pip install -U pip-tools
	pip-compile requirements/dev.in -o requirements/dev.txt
	pip-sync requirements/dev.txt

deps:
	python -m pip install -U pip-tools
	pip-compile requirements/deps.in -o requirements/deps.txt
	pip-sync requirements/deps.txt
