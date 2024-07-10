from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from . import views
from .consumers import NewsListConsumer

# api
router = SimpleRouter()

router.register("", views.NewsViewSet, basename="news")

# html
page_urlpatterns = [
    path("news/", views.NewsListView.as_view(), name="news-list"),
    path("news/<pk>", views.NewsDetailView.as_view(), name="news-detail"),
]

urlpatterns = router.urls

# ws
websocket_urlpatterns = [
    re_path(r"^ws/news/$", NewsListConsumer.as_asgi()),
]
