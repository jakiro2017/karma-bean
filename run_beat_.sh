#!/bin/zsh
echo $CELERY_BROKER_URL
celery -A karma_bean beat 
