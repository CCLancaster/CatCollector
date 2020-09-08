"""
WSGI config for catcollector project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv

catcollector = os.path.expanduser('/Users/monty/Django-is-a-Thing/catcollector/catcollector')
load_dotenv(os.path.join(catcollector, '.env'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catcollector.settings')

application = get_wsgi_application()
