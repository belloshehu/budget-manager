"""
WSGI config for errand project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'errand.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Prod')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
