uwsgi -s /tmp/uwsgi.sock --chmod-socket=666 --wsgi-file runserver.py --callable app
