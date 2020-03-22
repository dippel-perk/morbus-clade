release: export DJANGO_PROD=true && python manage.py migrate && python manage.py loaddata health_system && python manage.py loaddata base_data
web: python manage.py runserver 0.0.0.0:$PORT