default: help

.PHONY: build

help: ## Show this help
	@echo "Targets:"
	@fgrep -h "##" $(MAKEFILE_LIST) | grep ":" | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/\(.*\):.*##[ \t]*/    \1 ## /' | sort | column -t -s '##'
	@echo

env: ## Create the .env file
	cp example.env .env

build: ## Build the docker image
	docker-compose build

up: ## Start the docker container (detached)
	docker-compose up -d

down: ## Stop the docker container
	docker-compose down

logs: ## Show the docker logs
	docker-compose logs -f

sh: ## Open a shell in the docker container
	docker-compose exec papermc sh

dev: down build up