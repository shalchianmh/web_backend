
# Pizzato back project

This project is the back-end of a web application named Pizzato.
Pizzato is a Django-based web application where you can make your custom pizza using different ingredients.
## Logo
![Logo](https://i.postimg.cc/W3tLsDVQ/res-logo.png)

## Deployment

To deploy this project after cloning it from Git Hub, you should run the requiremnet.txt file to install packages needed for python to run the app.

```bash
  pip install requirement.txt
```
## Environment Variables
There are some configs for postgresql database, debug mode and ..., you can set in the .env.dev file.
## Migrations
after configuring you can run the back project, before running you should make migrations and migrate them by these commands, note that the database must be active in this point:
```bash
  python manage.py makemigrations
  python manage.py migrate
```
## Run
Now you can run the project and set the desired host and port:
```bash
  python manage.py runserver [desired host]:[desired port]
```
If you run this it runs on default hot which is `localhost` and port `8000`:
```bash
  python manage.py runserver
```

And you have done it! The project will be open in a new browser tab with this url:
```bash
  http://[desired host]:[desired port]/
```
## Admin
Using this command you can make a super user to access all the models in the admin pannel:
```bash
  python manage.py createsuperuser
```


## Tech Stack

Python, Django, Django REST framework(drf), docker




## Authors

- [@Ali Banayeean](https://www.github.com/Alibanayeean)
- [@Ali Sadeghi](https://www.github.com/Ali-Sadeghi-Gh)
- [@Mohammad Hossein Shalchian](https://www.github.com/shalchianmh)



