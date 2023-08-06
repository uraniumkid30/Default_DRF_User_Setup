#!/bin/bash
echo "Successfully Connected !"
source conf/env_variables/.env
echo "About to run management checks!"
python manage.py check
echo "About to run migrations !"
python manage.py migrate
echo "About to run server !"
python manage.py runserver 0.0.0.0:8000