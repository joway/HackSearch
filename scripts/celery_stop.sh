celery multi stopwait scheduler --pidfile="$HOME/spider/celery/%n.pid"
celery multi stopwait fetcher --pidfile="$HOME/spider/celery/%n.pid"
celery multi stopwait processor --pidfile="$HOME/spider/celery/%n.pid"
celery multi stopwait pipeline --pidfile="$HOME/spider/celery/%n.pid"