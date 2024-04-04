from django.contrib import admin
from new_app.models import News, OlxHome
# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'palace', 'name', 'game_count', 'score')

@admin.register(OlxHome)
class OlxHomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')