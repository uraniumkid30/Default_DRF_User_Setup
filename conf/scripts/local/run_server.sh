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
poetry shell
poetry install
poetry lock --no-update
source $(poetry env info --path)/bin/activate
python manage.py check
python manage.py runserver