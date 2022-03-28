up:
	docker-compose up -d

.test:
	docker-compose run --rm web pytest .

test: up .test
