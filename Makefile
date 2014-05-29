foreman:
	foreman start
shell:
	python manage.py shell

run:
	python manage.py runserver

sync:
	python manage.py syncdb

collectstatic:
	python manage.py collectstatic

deletedb:
	rm ~/projects/django/notify/db.sqlite3