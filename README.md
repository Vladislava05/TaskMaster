# TaskMaster
![GitHub forks](https://img.shields.io/github/forks/Vladislava05/TaskMaster?style=social)

Hey everyone!😊<br>
This TaskMaster was created in order to help you keep your busy life in order! 
Technology used: Python 3.9, Django 3, CSS, HTML
I would be more than happy if you could help me with this project!

**Link to our web-app**: https://todo-vladislava.herokuapp.com/

![Image](https://github.com/Vladislava05/TaskMaster/blob/main/peview.jpg)
Join us!

**Our Facebook**: https://www.facebook.com/groups/295736722419986

**Our Twitter**: https://twitter.com/VlaDis005

## Contents

* [Installation](#installation)
* [Installation to Heroku](#installation-to-heroku)
* [Contacts](#contacts)
* [License](#license)

## Installation

1. Create the environments file:

    ```console
    foo@bar: TaskMaster $ python3 -m venv ./.venv/
    ```

2. Migrate:

    ```console
    foo@bar: TaskMaster $ python3 manage.py migrate
    ```

3. Run server:

    ```console
    foo@bar: TaskMaster $ python3 manage.py runserver
    ```

## Installation with Docker

1. Build and up docker containers:

    ```console
    foo@bar: TaskMaster $ docker-compose up -d --build
    ```

2. Run migrations:

    ```console
    foo@bar: TaskMaster $ docker-compose exec web python manage.py migrate
    ```

## Installation to [Heroku](https://www.heroku.com/)

1. Create the Heroku app:

    ```console
    foo@bar: TaskMaster $ heroku create
    ```

2. Push repository to Heroku:

    ```console
    foo@bar: TaskMaster $ git push heroku main
    ```

3. Migrate:

    ```console
    foo@bar: TaskMaster $ heroku run python manage.py migrate
    ```

## Contacts

Created by [@vladislava05](https://github.com/Vladislava05) and [@stonedch](https://github.com/stonedch)

## License

[GNU GPL v3](LICENSE.md)
