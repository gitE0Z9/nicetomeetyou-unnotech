from rest_framework.routers import SimpleRouter

from .views import NewsViewSet

router = SimpleRouter()

router.register("", NewsViewSet, basename="news")

urlpatterns = router.urls
