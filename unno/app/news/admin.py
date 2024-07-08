from django.contrib import admin

from .models import News

# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "brief",
        "source",
        "source_url",
        "post_time",
        "create_time",
    )
    list_filter = ("source",)

    @admin.display(description="敘述")
    def brief(self, obj):
        return obj.content[:20]
