# Games API Microservice

A microservice written in Django to display details about stored games.

## Installation

1. Install docker
2. Install docker-compose
    - Depending on your OS, docker-compose may be pre-installed with Docker.
    - For more details, check [here](https://docs.docker.com/compose/install/)
3. Clone this repo.

That's it!

## Running
Ensure that docker is running.
Run `docker-compose up`. Docker will take care of the rest for you.
You can now access the microservice on `localhost:8080`

## About the app
This app has 2 sets of endpoints:
- `/games/<game_id>`
    - This will give return the details of a particular game.
    - Returns a 404 response if a game with the given ID is not found.
    - The app comes seeded with 3 games, so valid ID's are [1,2,3]
- `/games/report`
    - This will return a summary of all games installed.

NOTE: If you are trying to hit this endpoint outside of a browser context,
such as using `curl` or Postman, ensure you add a trailing `/` to your endpoint
(e.g. `http://localhost:8080/games/1/`). This is because Django is opinionated
about having a trailing `/` on URIs; without it Django will return a `301` response instead.

The seeded data can be found [here](./app/games/fixtures). After modifying the data,
you will need to run `docker-compose up --build` to re-seed the data.