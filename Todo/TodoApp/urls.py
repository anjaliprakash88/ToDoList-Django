from django.urls import path
from .import views

urlpatterns = [
    path('', views.loginpage, name='login'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('logout', views.user_logout, name='logout'),
    path('create', views.create_todo, name='create_todo'),
    path('complete_todo/<int:id>', views.complete_todo, name='complete_todo'),
    path('delete_todo/<int:id>', views.delete_todo, name='delete_todo'),
    

]