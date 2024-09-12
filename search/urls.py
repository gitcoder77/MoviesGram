from . import views
from django.urls import path


app_name='search'

urlpatterns = [
    path('',views.SearchResult,name='SearchResult'),
]