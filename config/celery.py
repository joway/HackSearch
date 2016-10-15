from celery import Celery

app = Celery('spider')
app.config_from_object('config.celeryconfig')
