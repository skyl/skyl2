"""
WSGI config for skyl2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

sys.path.insert(0, "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skyl2.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
