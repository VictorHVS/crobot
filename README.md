[![CircleCI](https://circleci.com/gh/VictorHVS/crobot/tree/master.svg?style=svg)](https://circleci.com/gh/VictorHVS/crobot/tree/master)

<p align="center">
  <a href="https://calltraderbot.com/">
    <img height="30" src="https://calltraderbot.com/images/ctb_logo-black.gif">
  </a>
</p>

[![CircleCI](https://circleci.com/gh/VictorHVS/calltraderbot.svg?style=svg)](https://circleci.com/gh/VictorHVS/calltraderbot)

# Crobot - Mordomo do Apto 22

Projeto open source para gerenciamento domiciliar.

## Python

This project required Python >= 3.7.

### Getting started

#### Prerequisites

+ [Docker](https://www.docker.com)
+ [Docker Compose](https://docs.docker.com/compose/)


#### Development

```bash
# Install Dependencies
$ pip install -r requirements.txt

# Start the postgres instance.
$ docker-compose up

# Create the .env file
$ cp .env.example .env

# Run migrations
$ python manage.py migrate

# Create admin user, only on first setup
$ python manage.py createsuperuser

# Start the development server
$ python manage.py runserver

# Start the telegrambot
$ python bot/bot.py
```

#### Testing

See: docs/testing.md

```bash
$ python manage.py test
```

## Deployment

See: [docs/deployment.md](docs/deployment.md)

## Monitoring

See: [docs/monitoring.md](docs/monitoring.md)

## Troubleshooting

See: [docs/troubleshooting.md](docs/troubleshooting.md)

## Links

- TODO: Links

# Maintainers

Vanessa Martins <@gmail.com>
Felipe Saraiva da Costa<@gmail.com>
Victor Hugo Vieira de Sousa <vhv.sousa@gmail.com>