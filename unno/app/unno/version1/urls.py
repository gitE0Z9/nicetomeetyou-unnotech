from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

BASE_API_PREFIX = "api/v1/"


# swagger api
swagger_info = openapi.Info(
    title="UNNO Tech API",
    default_version="v1",
    description="UNNO Tech API",
    contact=openapi.Contact(email="acrocanthosaurus627@gmail.com"),
)

SchemaView = get_schema_view(
    swagger_info,
    public=True,
    permission_classes=[permissions.AllowAny],
)

swagger_urlpatterns = [
    path(
        "swagger-json",
        SchemaView.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        SchemaView.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        SchemaView.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]


urlpatterns = [
    path(
        BASE_API_PREFIX + "news/",
        include("news.urls"),
    ),
    *swagger_urlpatterns,  # docs
]
