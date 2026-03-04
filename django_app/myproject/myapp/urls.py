from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('greet/<str:name>/', views.greet, name='greet'),
    path('messages/', views.message_list, name='messages'),
]