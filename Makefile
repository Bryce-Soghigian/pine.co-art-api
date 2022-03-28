up:
	docker-compose up -d

.test:
	docker-compose run -rm web pytest --cov --cov-report term-missing:skip-covered

test: up .test
