.PHONY: dev-env
dev-env:
	poetry install
	poetry run pre-commit install
	@[ ! -e .env ] \
		&& echo "Copying ./.env.example to ./.env; Populate the values before running anything!" \
		&& cp .env.example .env  \
		|| echo "You already have a .env file. You're all set!"

.PHONY: run-local
run-local:
	poetry run python main.py
