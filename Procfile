web: gunicorn RDC.wsgi --log-file -
worker: celery -A RDC worker -l INFO
