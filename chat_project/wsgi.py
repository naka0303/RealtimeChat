"""
WSGI config for chat_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat_app.routing

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')

#application = ProtocolTypeRouter({
#  "http": get_asgi_application(),#http://ならこっち
#  "websocket": AuthMiddlewareStack(#ws:// wss://ならこっち
#        URLRouter(
#            chat_app.routing.websocket_urlpatterns#chat_app/routing.py
#        )
#    ),
#})
