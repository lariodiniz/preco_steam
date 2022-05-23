POETRY = poetry run

## @install
.PHONY: install
install: ## installing program using poetry. poetry needs is installed.
	poetry install

## @run server
.PHONY: run
runserver: ## activate development server.
	${POETRY} python main.py

## @tests
.PHONY: tests
tests: ## run system tests.
	${POETRY} pytest -v

## @format
.PHONY: blue
blue: ## format python code.
	${POETRY} blue .

## @import sort
.PHONY: isort
isort: ## order the imports.
	${POETRY} isort .

## @audit modules
.PHONY: audit
audit: ## checks the security flaws of the modules used.
	${POETRY} pip-audit

## @analyze 
.PHONY: analyze 
analyze : ## analyze python code.
	${POETRY} blue . --check
	${POETRY} pip-audit
	${POETRY} pytest -v

## @documentation 
.PHONY: docserver
docserver: ## format python code.
	${POETRY} mkdocs serve