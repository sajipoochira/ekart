python manage.py migrate --no-input

python manage.py collectstatic

gunicorn ekart.wsgi:application --bind 0.0.0.0:8000