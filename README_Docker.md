# Docker Documenation
This file contains documenation on docker configuration.

## Build Project
First build will be slow, subsequient build will be faster 

docker build [OPTIONS] PATH | URL | -

``docker build -f ./Dockerfile ``

or (when in directorty ~/)

``docker build .``

## Run Project
To run the project:

``docker run -it python_api:latest``

or with docker-compose

``docker-compose -f "docker-compose.yaml" up -d --build ``
