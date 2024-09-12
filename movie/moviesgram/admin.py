from django.contrib import admin

from moviesgram.models import Category, Language, Movie


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Language, LanguageAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'actor', 'release_date', 'language', 'added_by', 'category', 'youtube', 'img']
    list_editable = ['youtube', 'img']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 30


admin.site.register(Movie, MovieAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'movie', 'rate', 'created_at']
    readonly_fields = ['created_at']
