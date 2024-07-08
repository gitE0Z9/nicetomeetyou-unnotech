from django.urls import path
from news.urls import page_urlpatterns as news_page_urls

urlpatterns = [
    *news_page_urls,
]
