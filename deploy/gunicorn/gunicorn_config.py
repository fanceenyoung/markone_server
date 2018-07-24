import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count()
worker_class = 'gevent'

BASE_PATH = '/home/ubuntu/markone_server'
pythonpath = '/home/ubuntu/markone_server'
django_settings = 'markone_server.settings'

max_requests = 5000

timeout = 300

user = 'root'
group = 'root'

pidfile = '/run/markone_server-gunicorn.pid'
errorlog = '/var/log/markone_server/gunicorn/stderr.log'

