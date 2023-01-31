# Class 31 - Lab: Django REST Framework & Docker

### Author: DeShon Dixon

---

- To run Docker


    python manage.py runserver 0.0.0.0:8000


- To login
  - username: admin
  - password: 1234
  

    http://127.0.0.1:8000/admin

- Run in browser


    http://0.0.0.0:8000/api/v1/myapi/

## Overview

- Use Django REST Framework to create an API, then “containerize” it with Docker.

## Feature Tasks and Requirements

- Rebuild a custom version of Things API demo project from scratch.
- Replace things_project and Thing with your own application and model.
- Your model must have at least as many fields as demo’s model.
- Your model must have one field that is a foreign key to user.

### Features - Docker

- Update Dockerfile and docker-compose.yml if needed.

## Stretch Goals

- Research using a production server vs. the built in development server.
- Research using postgres instead of sqlite as database.
- Implementation Notes
- If you get an allowed host error examine the bug details and update code as needed.
- When Docker installed and docker files are ready to go then run…

      $ docker-compose up

- To shut docker down enter ctrl+c

## User Acceptance Tests

- Modify provided unit tests in demo to work for your project.
- Configuration
- Create a virtual environment inside drf-api.
- Use the drf-api folder as the root of your project’s git repository.

---