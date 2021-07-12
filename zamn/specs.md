# Version 1 for Project Playground

Completed Tasks:
- Developer will be apple to recieve all thoughts with GET request for all three playgrounds.
- Developer will be able to add a thought with a POST request for all three playgrounds.
- Developer will be able to add a edit a thought with a PUT request for all three playgrounds.
- Developer will be able to delete a rthought with a DELETE request for all three playgrounds.


# How to run an application

- Make a virutal environment. 

 ```python
virtualenv {virtual environment name}
 ```
- Install and update using PIP

 ```python
 pip install -r requirements.txt
 ```
 
 Install Django:
```
pip install djangorestframework
pip install markdown       
pip install django-filter  
```
# Requirements.
```
appdirs==1.4.4
astroid==2.4.2
attrs==20.3.0
certifi==2020.12.5
chardet==4.0.0
click==7.1.2
configparser==5.0.2
distlib==0.3.1
filelock==3.0.12
Flask==1.1.2
Flask-MySQLdb==0.2.0
idna==2.10
iniconfig==1.1.1
isort==5.7.0
itsdangerous==1.1.0
Jinja2==2.11.3
lazy-object-proxy==1.4.3
MarkupSafe==1.1.1
mccabe==0.6.1
mysqlclient==2.0.3
packaging==20.9
pluggy==0.13.1
protobuf==3.17.1
py==1.10.0
pyee==8.1.0
pylint==2.6.0
pyparsing==2.4.7
pytest==6.2.2
pytest-mock-server==0.2.0
requests==2.25.1
six==1.15.0
toml==0.10.2
urllib3==1.26.3
virtualenv==20.4.7
Werkzeug==1.0.1
wrapt==1.12.1
```

# Run Server (API)
 ```
 python3 manage.py runserver
 ```


# API EndPoints:
In this RESTful API, our endpoints will define the structure of the API and how users access their data from our application using HTTP Methods - GET, POST,PUT DELETE.

In this case we have three resources, brainstorms, inverts, and cubing. and /{resource}/:id


# Use

Example API response for idea:

Only authenticated users can use the API service, for that reason if we try this:
```
http  http://127.0.0.1:8000/api/v1/brainstorms/
```
you would get
```
{
    "detail": "Authentication credentials were not provided."
}

```

Now to access it with credentials:
```
http http://127.0.0.1:8000/api/v1/brainstorms/27 "Authorization: 94301d621abb1ce2feb8b8e8ba2bfc8c9867a673"
```
you would get the brainstorm with the idea of 27
```
{"id":27,"goals":"To be a doctor","agenda":"To not bea dctor","outcomes":"To hate a doctor","decisions":"Don't be a doctor"}
```

Restrictions:
- The Brainstorms, inverisons, and cubing playgrounds are only assoicated with the creator.
- The API doesn't allow unauthenticated results.
- Only Authenticated user can create palygorunds
- The API doesn't allow for unauthenticated results. 
