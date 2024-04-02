from django.urls import re_path,path
from backend.consumer import ChatData
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
websocket_urlpatterns = [
    # path('ws/chat/', ChatData.as_asgi()),
    path('ws/chat/<str:user_id>/', ChatData.as_asgi())
    # re_path(r'ws/chat/$', ChatData.as_asgi()),
    #  re_path(r'ws/group_name/(?P<extended_group>[^/]+)/$', POSextended.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})