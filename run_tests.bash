# !bin/bash

docker-compose run --rm web bash pytest "$@"
