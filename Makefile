migrate:
	rm -f django.db
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver_plus 127.0.0.1:8889

createuser:
	python manage.py createsuperuser --username admin --email test@gmail.com
