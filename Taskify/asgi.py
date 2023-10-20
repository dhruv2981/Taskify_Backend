"""
ASGI config for Taskify project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Taskify.settings')

application = get_asgi_application()
ws_patterns = [

]

application = ProtocolTypeRouter(
    {
        'webocket': URLRouter(ws_patterns)
    }
)
