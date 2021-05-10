from os import getenv


wsgi_app = "src.app:create_app()"
reload = getenv("FLASK_ENV", "development") == "development"
accesslog = "-"
access_log_format = (
    "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sµs"
)
loglevel = getenv("GUNICORN_LOG_LEVEL")
capture_output = True
bind = f"0.0.0.0:{getenv('PORT', '8000')}"
workers = 2
worker_class = "eventlet"
