from channels.routing import URLRouter
from news.urls import websocket_urlpatterns as news_ws_patterns

websocket_middleware = URLRouter(
    [
        *news_ws_patterns,
    ]
)
