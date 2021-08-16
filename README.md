# TicketWorld

[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)


# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

As mentioned above, this project is based on [Cookiecutter Django Rest](https://github.com/agconti/cookiecutter-django-rest) and contains some code that is not written by me.

**[IMPORTANT] My code can be found in the `ticketworld/reservations` module.**

Note: Tickets will never be released once booked. As agreed, this functionality is out of scope.


Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

Restore dummy data (a couple of Events and Tickets available for reservation)
```bash
docker-compose run --rm web python manage.py loaddata ticketworld/reservations/fixtures/initial_data.json
```

There are two endpoints available(local development):
- `GET localhost:8000/api/v1/reservations/` - retrieve reservations and associated tickets
- `POST localhost:8000/api/v1/reservations/` Body: ```{"tickets": [1, 2]}``` - Create new reservations
