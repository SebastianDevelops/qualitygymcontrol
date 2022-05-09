"""
WSGI config for Gymnasium project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
#import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Gymnasium.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from notifications.config import get_notification_count, run_notifier

'''app_path = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
sys.path.append(os.path.join(app_path, ""))'''

run_notifier()

