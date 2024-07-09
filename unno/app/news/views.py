from django.views.generic import TemplateView
from rest_framework.pagination import CursorPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from .models import News
from .serializers import NewsListSerializer, NewsSerializer


class NewsListView(TemplateView):
    template_name = "news-list.html"


class NewsDetailView(TemplateView):
    template_name = "news-detail.html"


# Create your views here.
class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    http_method_names = ["get"]
    ordering = "-post_time"
    pagination_class = CursorPagination
    filter_backends = [
        OrderingFilter,
    ]

    def get_serializer_class(self):
        if self.action == "list":
            return NewsListSerializer
        else:
            return NewsSerializer
