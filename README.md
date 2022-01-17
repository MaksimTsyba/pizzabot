## The Pizzabot

This is program for generate instruction for Pizzabot.

## Install local virtual environment
It must to be python >= 3.5  in system!
For creating local virtual environment to run this command:
> ./create_env

## Install using docker
You need to install docker and docker-compose to system.
The easiest way to install [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/)

If you have make file you can build container by this command:

> make build

and run container:

> make run

If you don't have makefile you need to build docker container follow this command:
> docker-compose build

Next you need to run container: 
> docker-compose run --rm pizzabot /bin/sh
## Run the Pizzabot

For run the Pizzabot follow this command:
> ./pizzabot "5x5 (1, 3) (4, 4)"

## Run python tests

For run python tests follow this command:
> pytest