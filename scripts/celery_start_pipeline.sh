celery multi start pipeline -A config -Q pipeline --pidfile="$HOME/spider/celery/%n.pid" --logfile="$HOME/spider/celery/%n.log"
celery multi start pipeline2 -A config -Q pipeline --pidfile="$HOME/spider/celery/%n2.pid" --logfile="$HOME/spider/celery/%n2.log"
