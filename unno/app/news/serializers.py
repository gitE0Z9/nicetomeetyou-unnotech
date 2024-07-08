from .models import News
from rest_framework.serializers import ModelSerializer


class NewsListSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "img",
        )


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
