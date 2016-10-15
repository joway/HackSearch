celery multi start fetcher -A config -Q fetcher --pidfile="$HOME/spider/celery/%n.pid" --logfile="$HOME/spider/celery/%n.log"
celery multi start processor -A config -Q processor --pidfile="$HOME/spider/celery/%n.pid" --logfile="$HOME/spider/celery/%n.log"
