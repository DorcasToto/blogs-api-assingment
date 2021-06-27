# Blog Api
## Description
An application that displays all the blogs to users



# Features

- Register with username and password (Username should be unique)
- Login with username and password.
- A logged in user can add, edit and delete their blogs.
- All users including the not logged in ones can view all blogs.
- -Use jwt authentication



# Technologies Used
- Python.
- Django (Python framework)

# Installation

- Create and activate virtualenv.
- Install required packages: 
- pip install -r backend/requirements.txt.

# Setup

- copy settings.py.txt to settings.py and update the db credentials.(If you are using SQLLite)
- Setup database
- run python manage.py migrate
- Run the server
- Check if the application is running correctly
- Create a superuser for the admin backend
- run python manage.py createsuperuser and input the credentials
- Login as superuser

# Endpoints
Download [ postman]( https://www.postman.com/downloads/ ) to access the following endpoints

- loginendpoint (https://hood256.herokuapp.com/auth/login/)
- view hoods endpoint (https://hood256.herokuapp.com/api/v1/view_hood/%3Cpk%3E/)
- edit profile endpoint (https://hood256.herokuapp.com/api/v1/profile/%3Cpk%3E/ )
- signupendpoint (https://hood256.herokuapp.com/auth/signup/)
- view hoods endpoint (https://hood256.herokuapp.com/api/v1/hoods/)
- create post on a hood endpoint (https://hood256.herokuapp.com/api/v1/post/)
- current user endpoint (https://hood256.herokuapp.com/currentuser/)
- create hood endpoint (https://hood256.herokuapp.com/api/v1/create_hood/) username:moringa, password:1234


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/DorcasToto/Neighborhood-Frontend/blob/master/LICENSE)

© [DorcasToto](https://github.com/DorcasToto)

:satisfied: