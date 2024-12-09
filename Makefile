DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env.test
DATA = ./data/data.json
APP_FILE = ./docker-compose.yml
APP_CONTAINER = main-app

.PHONY: build
build:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: up
up:
	${DC} -f ${APP_FILE} ${ENV} up -d

.PHONY: migrate
migrate:
	${DC} -f ${APP_FILE} ${ENV} run --rm ${APP_CONTAINER} python manage.py migrate

.PHONY: superuser
superuser:
	${DC} -f ${APP_FILE} ${ENV} run --rm ${APP_CONTAINER} python manage.py createsuperuser

.PHONY: down
down:
	${DC} -f ${APP_FILE} down

.PHONY: shell
shell:
	${EXEC} ${APP_CONTAINER} sh

.PHONY: logs
logs:
	${LOGS} ${APP_CONTAINER} -f