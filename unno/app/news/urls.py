from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views


# api
router = SimpleRouter()

router.register("", views.NewsViewSet, basename="news")

# html
page_urlpatterns = [
    path("news/", views.NewsListView.as_view(), name="news-list"),
    path("news/<pk>", views.NewsDetailView.as_view(), name="news-detail"),
]

urlpatterns = router.urls
