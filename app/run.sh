#!/bin/bash
python -m pip install --upgrade pip

pip install -r requirements.txt

pip freeze > requirements.txt

python manage.py makemigrations

python manage.py collectstatic

python manage.py migrate

python manage.py collectstatic

python manage.py spectacular --file schema.yml



