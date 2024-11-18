set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

alias i := install

install:
    poetry install

lock:
    poetry lock

lint:
    poetry run ruff check
    poetry run ruff format --check

fix:
    poetry run ruff check --fix
    poetry run ruff format

run:
    poetry run python aca_protocols/__init__.py