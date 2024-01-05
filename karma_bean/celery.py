from __future__ import absolute_import, unicode_literals
import os
from dotenv import load_dotenv
# import sys

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "karma_bean.settings")
load_dotenv('.env')

app = Celery("karma")
app.conf.timezone = 'Asia/Bangkok' 
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
