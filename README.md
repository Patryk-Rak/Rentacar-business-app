# Rentacar Business App
## Service that helps you find suitable car in your location

[![N|Solid](https://seeklogo.com/images/G/github-logo-5F384D0265-seeklogo.com.png)](https://nodesource.com/products/nsolid)

<p align="center">
  <img width="200" src="https://i.imgur.com/0cYM5m3.png" href="">
</p>

Rentacar is an open-source web-app that simulates online service where people
can find suitable car and rent it for a specified period of time.
Website works with database that holds all informations about
offered products and also registered clients together with people
that works for the company. 

Mobile-ready, Django-powered, bootstrap 5.1.1 included.

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

####Service that helps you find suitable car in your location

![Frontpage](https://i.imgur.com/PenYUBA.png)
This is homepage on the website that contains navbar that navigates to common features

![Frontpage](https://i.imgur.com/4rr9g42.png)
This page u can choice our car to rent

![Frontpage](https://i.imgur.com/UmFF7Ut.png)
When u choice date to reservation you can check the total cost of your reservation

![Frontpage](https://i.imgur.com/HyaudnQ.png)
Client-side feature

## Tech

Rentacar uses a number of open source or free for use projects to work properly:

- [Python] - HTML enhanced for web apps!
- [Django] - HTML enhanced for web apps!
- [Django filters] - HTML enhanced for web apps!
- [Postgres] - awesome web-based text editor
- [Bootstrap] - Markdown parser done right. Fast and easy to extend.
- [Sendgrid] - great UI boilerplate for modern web apps
- [Heroku for Django] - evented I/O for the backend


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

**Open Source Software and three musketeers**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [SendGrid]: <https://sendgrid.com>
   [Patryk Rak]: <https://github.com/Patryk-Rak>
   [Bartłomiej Staniak]: <https://github.com/BartlomiejStaniak>
   [Mateusz Gralak]: <https://github.com/Muadib07>
