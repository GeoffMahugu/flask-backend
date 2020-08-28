# FLASK BACKEND APP 🐍
This is a simple Flask-API boilerplate to help you quickly get started with setting up and deploying your python project.
Here are some of the features of the setup:

1. Docker Ready
2. Kubernetes Ready
3. Deployment Ready

## Prerequisites:

i) Installed [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

i) Installed [Docker](https://docs.docker.com/engine/install/ubuntu/)

ii) Installed [docker-compose](https://docs.docker.com/compose/install/)


## STEP 1: Clone Project
To clone the project, run this command:

``git clone git@github.com:GeoffMahugu/flask-backend.git``

Cd into project directory:

 ``cd flask-backend``

 ## STEP 2: Setup Environment
There are 2 states the app can run: 

i) **DevConfig**: Has debug congigurations set on

ii) **ProdConfig**: This configuration has debug set off

To set the environments run this:
ENV_CONFIG: being either DevConfig or ProdConfig

``export APP_ENV=<ENV_CONFIG>``

 ## STEP 2: Run Project

 To run the project:

### Using Docker

i). Build

 ``docker-compose -f "docker-compose.yaml" up -d --build``
 
ii.) Run app

 ``docker-compose up``

 To read more on docker: (link ☞)[README_Docker.md]

**Note**

During development, remember to build the image before runing the image. (That might just be the reason you are not seeing your upates)


 ### Using PipEnv

i). Install PipEnv

Check version to make sure you are running python3

``python --version``

Proceed to install PipEnv

``pip3 install pipenv``

ii). Activate the Env

To activate the environment, run this command:
**PS:** Will auto pick the configs from the (requirements.txt)[./requirements.txt] file.

``pipenv shell``

iii) Install dependancies

``pipenv install``

iv) Run project

``python3 app.py``


# PROJECT SETUP

✦ [/api](./api) This directory contains configurations for setting up the business logic
Contains configurations for setting up API's

✦ [/config](./config) Contains Global application configurations

✦ [/models](./models) Contains configurations for modeling Database/iGraph. Do all ORM here.

✦ [/static](./static) Contains any sattic files that needs to be served

✦ [/tasks](./tasks) Contains configurations for any messaging process e.g Celery


## API DOCUMENATION

**i) Test Get-Request**

url: ``http://127.0.0.1:5000/api/test-get``

protocal: GET

response:

``
{
  "You are task home": "API 1 Done"
}
``

**ii) Test POST-Request**

url: ``http://127.0.0.1:5000/api/test-igraph``

protocal: POST

request: 

``
{
  "name": "John Doe",
	"uuid": "=_ueyJhbGciOiJSUzI1NiIsImtp="
}
``

response:

``
{
  "name": "John Doe",
  "uuid": "=_ueyJhbGciOiJSUzI1NiIsImtp=",
  "message": "Data has been processed"
}
``

## RESOURCES

 This is alist of usefull resources:
1. (Docker Docs)[https://docs.docker.com/get-started/]
2. (flask_restful)[https://flask-restful.readthedocs.io/en/latest/quickstart.html]
