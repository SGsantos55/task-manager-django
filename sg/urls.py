from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
path('',views.home,name='home'),
path('sign',views.sign,name='sign'),
path('login_user',views.login_user,name='login_user'),
path('santos',views.santos,name='santos'),
path('logout_user',views.logout_user,name='logout_user'),
path('Todo_list',views.Todo_list,name='Todo_list'),
path('create_todo',views.create_todo,name='create_todo'),
path('update_todo/<int:pk>',views.update_todo,name='update_todo'),
path('delete_todo/<int:pk>',views.delete_todo,name='delete_todo'),

]