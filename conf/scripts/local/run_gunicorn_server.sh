#!/bin/bash

# source ./venv/bin/activate
# sleep 2


# # migrate
# python manage.py makemigrations
# python manage.py migrate

# create superuser
# echo "${green}>>> Creating a 'admin' user ...${reset}"
# echo "${green}>>> The password must contain at least 8 characters.${reset}"
# echo "${green}>>> Password suggestions: djangoadmin${reset}"
# python manage.py createsuperuser --username='admin' --email=''

# run
MANAGER_NAME="pipenv" # update to manager_name options pipenv, python, poetry
if [ ${MANAGER_NAME} == "poetry" ]
then
    poetry shell
    poetry install
    poetry lock --no-update
    source $(poetry env info --path)/bin/activate
    source conf/env_variables/.env
    python manage.py check
    gunicorn -c conf/scripts/local/gunicorn_script.py
elif [ ${MANAGER_NAME} == "pipenv" ]
then
    echo "${blue}>>> Syncing environment with with ${MANAGER_NAME}."
    pipenv shell
    pipenv sync
    source conf/env_variables/.env
    echo "${green}>>> About running development server with ${MANAGER_NAME}."
    pipenv run python manage.py check
    pipenv run gunicorn -c conf/scripts/local/gunicorn_script.py
else
    echo "${blue}>>> Syncing environment with with ${MANAGER_NAME}."
    source conf/env_variables/.env
    echo "${green}>>> About running development server with ${MANAGER_NAME}."
    python manage.py check
    gunicorn -c conf/scripts/local/gunicorn_script.py
fi
