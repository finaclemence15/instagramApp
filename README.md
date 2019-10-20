## Instagram App

Instagram App is a clone of the website for the popular photo app Instagram(desktop version) 

## Created by [finaclemence15](https://github.com/finaclemence15)

## Date

20/10/2019

## How to Use it

You must login or register. Once you logged in, you will be able to see posts made by other users. You can add your own photos from your profile page. As a user you can also follow other users and view images posted by those users. You also have the possibility to edit your profile and view the photos that you have posted.

## User Stories

1. Sign in to the application to start using.
2. Upload your pictures to the application.
3. See your profile with all your pictures.
4. Follow other users and see their pictures on your timeline.
5. Like a picture and leave a comment on it.

 
## Installation Requirement


```
git clone https://github.com/finaclemence15/instagramApp

virtualenv virtual

source virtual/bin/activate

pip3 install -r requirements.txt

psql CREATE DATABASE instagram

python manage.py makemigrations instagramapp

python manage.py migrate

python3.6 manage.py runserver

python manage.py test

```

## Running the web app in development

``` python3.6 manage.py server ```

Open the app on your browser, by default on ``` http://127.0.0.1:8000/ ```

## Technologies Used

* HTML
* css
* boostrap4
* Django
* python
* Vs code
* Git Hub
* Terminal
* Postgres database 

## Support and contact details

+ Email:finaclemence15@gmail.com

## License

Copyright (c) All right reserved 2019
