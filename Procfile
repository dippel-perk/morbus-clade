release: export DJANGO_PROD=true && python manage.py migrate && python manage.py loaddata health_system
web: python manage.py runserver 0.0.0.0:$PORT