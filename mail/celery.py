from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mail.settings')
app = Celery('mail')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task()
def add(email, message):
    send_mail('title',
        strip_tags(message),
        '@example@example.com',
        [email],
        html_message=message,
        fail_silently=False)
#celery -A mail worker -l info