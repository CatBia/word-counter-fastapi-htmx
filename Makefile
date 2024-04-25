build:
	docker compose -f development/docker-compose.dev.yml build --no-cache  --build-arg UID=1000 --build-arg GID=1000
dev:
	docker compose -f development/docker-compose.dev.yml run --entrypoint /bin/bash --service-ports --rm web
test:
	docker compose -f development/docker-compose.dev.yml run --entrypoint "/bin/bash -c '/home/developer/app/development/venv/bin/python -m pytest'" --rm web
up:
	docker compose -f development/docker-compose.dev.yml run --entrypoint " /bin/bash -c '/home/developer/app/development/venv/bin/python main.py'" --service-ports --rm web