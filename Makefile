up:
	docker-compose up -d

.test:
	docker-compose run --rm web pytest .

test: up .test

down:
	docker-compose down

force_recreate:
	docker-compose up -d --force-recreate