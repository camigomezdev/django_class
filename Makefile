run-local:
	python manage.py runserver --settings=settings.local

# call with make startapp APP_NAME=<your-app-name>
startapp:
	python manage.py startapp $(APP_NAME) --settings=settings.local

makemigrations:
	python manage.py makemigrations --settings=settings.local

migrate: 
	python manage.py migrate --settings=settings.local

createsuperuser:
	python manage.py createsuperuser --settings=settings.local

run-prod:
	python manage.py runserver --settings=settings.prod

# call with make copy-db -e DB_FILE=<your-file-name>
copy-db:
	mysqldump -u root amigurumis_db > $(DB_FILE)

create-local-db:
	echo "CREATE DATABASE amigurumi_db;" | mysql -u root

clear-local-db:
	echo "DROP DATABASE IF EXISTS amigurumis_db; CREATE DATABASE amigurumis_db;" | mysql -u root

# call with make import-db -e DB_FILE=<your-file-name>
import-db: clear-local-db
	mysql -u root amigurumis_db < $(DB_FILE)