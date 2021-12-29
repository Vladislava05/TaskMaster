# TaskMaster

![Github issues](https://img.shields.io/github/issues/Vladislava05/TaskMaster.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/)
<br><br><br>
![Image](https://github.com/Vladislava05/TaskMaster/blob/main/peview.jpg)

## Overview

<h3 align="left">Built with:</h3>
<p align="left"> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

This **TaskMaster** is an open source project created in order to help you keep your busy life in order and boost your productivity.

**Link to our web-app**: https://todo-vladislava.herokuapp.com/ <br><br>
<img src="https://github.com/Vladislava05/TaskMaster/blob/main/gif.gif"></img>



**Our Facebook**: https://www.facebook.com/groups/295736722419986

**Our Twitter**: https://twitter.com/VlaDis005

## Contents

* [Installation](#installation)
* [Installation to Heroku](#installation-to-heroku)
* [Contributing](#contributing)
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
## Contributing ##
If you want to contribute to our project, check <a href="https://github.com/Vladislava05/TaskMaster/blob/main/Contributing.md">**this**</a>

## Contacts

Created by [@vladislava05](https://github.com/Vladislava05) and [@stonedch](https://github.com/stonedch)

## License

[GNU GPL v3](LICENSE.md)
