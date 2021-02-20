from django.urls import path

from . import views

app_name = 'sender'
urlpatterns = [
    path('', views.send_email, name='index'),
]