python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input --clear
gunicorn --bind 0.0.0.0:8000 DRF_bookstore.wsgi