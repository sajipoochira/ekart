python manage.py makemigrations 

python manage.py migrate --no-input

echo "from django.contrib.auth.models import User; User.objects.create_superuser('Admin', 'admin@example.com', 'pass')" | python manage.py shell

python manage.py collectstatic

gunicorn ekart.wsgi:application --bind 0.0.0.0:8000