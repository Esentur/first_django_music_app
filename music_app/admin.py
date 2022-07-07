from django.contrib import admin
from music_app.models import Category, Music

# Register your models here.
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title','duration','category']
    list_filter =['category']
    search_fields = ['id']
admin.site.register(Category)
admin.site.register(Music,MusicAdmin)