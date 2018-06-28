import multiprocessing

bind = "0.0.0.0:11112"
workers = multiprocessing.cpu_count()
worker_class = 'gevent'

BASE_PATH = '/root/markone_server'
pythonpath = '/root/bg_recognition'
django_settings = 'bg_recognition.settings'

max_requests = 5000

timeout = 300

user = 'root'
group = 'root'

pidfile = '/run/bg_recognition-gunicorn.pid'
errorlog = '/var/log/bg_recognition/gunicorn/stderr.log'

