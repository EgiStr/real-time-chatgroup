"""
ASGI config for realtimeChat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os


from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import Websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtimeChat.settings')


os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            Websocket_urlpatterns
        )
    ),
})
