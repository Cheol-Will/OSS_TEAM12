from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('create_account/', views.user_create, name='user_create')
]