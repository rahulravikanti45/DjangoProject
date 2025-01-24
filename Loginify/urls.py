from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name = 'login'),
    path('create_user/', views.create_user_view, name='create_user'),
    path('get_all_users/', views.getAllUsers_view, name='get_all_users'),
    path('get_user/<str:username>/', views.getSingleUser_view, name='get_user'),
    path('update_user/<str:username>/', views.updateUser_view, name='update_user'),
    path('delete_user/<str:username>/', views.deleteUser_view, name='delete_user')
]