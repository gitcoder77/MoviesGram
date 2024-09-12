from . import views
from django.urls import path


from .views import PasswordChangeView

app_name='users'

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register,name='register'),
    path('',views.logout_view,name='logout'),
    path('dashboard/',views.DashBoard,name='dashboard'),
    path('<int:pk>/password/', PasswordChangeView.as_view()),
]