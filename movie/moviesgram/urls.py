from . import views
from django.urls import path

from .views import AddMovie, AddCategoryView, index, CategoryView, LanguageView, MovieEditview, AddLanguageView, \
    DeleteMovieView

app_name='moviesgram'

urlpatterns = [
    path('index/',index.as_view(),name='index'),
    path('add_category/',AddCategoryView.as_view(),name='AddCategory'),
    path('add_language/',AddLanguageView.as_view(),name='AddLanguage'),
    path('movie/<int:movie_id>/',views.MovieDetail,name='MovieDetail'),
    path('Add_Movie/',AddMovie.as_view(),name='AddMovie'),
    path('category/<slug:cats>/',CategoryView,name='category'),
    path('language/<slug:langs>/',LanguageView,name='language'),
    path('movie/edit/<int:movie_id>',MovieEditview.as_view(),name='update_movie'),
    path('movie/delete/<int:movie_id>',DeleteMovieView.as_view(),name='delete_movie'),
    path('',views.user_movies,name='user_movies')

]