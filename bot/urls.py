from django.urls import path

from . import views

urlpatterns = [
    path('', views.send_message, name='conversation'),
    path('conversation', views.send_message, name='conversation'),
]
