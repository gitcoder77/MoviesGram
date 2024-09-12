from . import views
from django.urls import path

from .views import AddCategory, index, CategoryView, LanguageView,\
      AddLanguage, updatemovie, delete

app_name='moviesgram'

urlpatterns = [
    path('index/',index.as_view(),name='index'),
    path('add_category/',AddCategory,name='AddCategory'),
    path('add_language/',AddLanguage,name='AddLanguage'),
    path('movie/<int:movie_id>/',views.MovieDetail,name='MovieDetail'),
    path('add_movie/',views.add_movie,name='AddMovie'),
    path('category/<slug:cats>/',CategoryView,name='category'),
    path('language/<slug:langs>/',LanguageView,name='language'),
    path('movie/edit/<int:movie_id>',updatemovie,name='update_movie'),
    path('movie/delete/<int:movie_id>',delete,name='delete_movie'),
    path('',views.user_movies,name='user_movies')

]