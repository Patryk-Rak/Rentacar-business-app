<p align="center">
  <img width="200" src="https://i.imgur.com/0cYM5m3.png" href="">
</p>

# Rentacar Business App
## Service that helps you find suitable car in your location




Rentacar is an open-source web-app that simulates online service where people
can find suitable car and rent it for a specified period of time.
Website works with database that holds all informations about
offered products and also registered clients together with people
that works for the company. 

Mobile-ready, Django-powered, bootstrap 5.1.1 included. Website was initially written in polish, gradually being translated into english language.
## Features

- Create an account as a client directly from website
- Edit your profile info, change passwords and check your payment history
- Manage database related content on website as admin
- Add and edit cars, facilities, users
- Send email through website form

Many features even if working are still unpolished and there's
always room for improvements. We consider this a good practice 
and way to learn right flow when adding new features.

> This project is still under development and we will
> make updates consisting new ideas and solutions
> during process. We consider this app to be finished when
> end look will be ready for comercial use or at least 
> prepared for implementation.


## Preview

![Frontpage](https://i.imgur.com/PenYUBA.png)
This is homepage on the website that contains navbar that navigates to common features.

![Frontpage](https://i.imgur.com/4rr9g42.png)
Product page with listed items and functional filtering option.

![Frontpage](https://i.imgur.com/UmFF7Ut.png)
Raw page (for now) with confirmation of the transaction.

![Frontpage](https://i.imgur.com/HyaudnQ.png)
Client-side features with profile edit option and history of transactions.

## Tech

Rentacar uses a number of open source or free for use projects to work properly:

- [Python] - 3.9.2 version
- [Django] - 3.2.3 version
- [Django filters] - 2.4.0 version
- [Postgres] - 14.0 version
- [Bootstrap] - 5.1.1 version, installed in static files
- [Sendgrid] - 6.7.1 version, API for email feature, needs account to operate
- [Heroku for Django] - 0.3.1 version


## Installation

### This installation is for a project on a local server

Create virtualenv and install the dependencies from requirements.txt
```sh
- virtualenv venv
- pip install -r path_to_your requirements.txt
```

This project use PostgreSQL data service, so before run the server 
you have set up your database in settings:

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'NameOFYourDataBase',
        'USER': 'YourUser',
        'PASSWORD': 'YourPassword',
        'HOST': 'YourPortHost',
        'PORT': 'YourPortAddress',
    }
}
```

Start the server by following command.
```sh
- python manage.py makemigrations
- python manage.py migrate 
- python manage.py runserver
```

#### *** Optional feature 
If you want use send mail feature you have crate account on [SendGrid] and follow the instructions 
 

## Creators
   
- [Patryk Rak] - Cobra
- [Bartłomiej Staniak] - Mamba 
- [Mateusz Gralak] -  Boa


## License

**Open Source Software**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [SendGrid]: <https://sendgrid.com>
   [Patryk Rak]: <https://github.com/Patryk-Rak>
   [Bartłomiej Staniak]: <https://github.com/BartlomiejStaniak>
   [Mateusz Gralak]: <https://github.com/Muadib07>
