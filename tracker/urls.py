from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.public_profile, name='profile'),
    path('u/<str:nickname>/', views.public_profile, name='public_profile'),
    path('add/', views.add_to_list, name='add_to_list'),
    path('get_status/', views.get_status, name='get_status'),
    path('upload_picture/', views.upload_picture, name='upload_picture'),
    path('follow/', views.follow_user, name='follow_user'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
