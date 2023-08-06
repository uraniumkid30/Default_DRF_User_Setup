# base image  
FROM debian:bookworm
FROM python:3.8 
SHELL ["/bin/bash", "-c"]
# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DockerHOME 
# run this command to install all dependencies  
RUN pip install -r requirements/development.txt 

# port where the Django app runs 
CMD chmod a+rwx ./conf/scripts/local/provide_env.sh

EXPOSE 8000  
# start server  
# ENTRYPOINT ["./conf/scripts/local/provide_env.sh"]
