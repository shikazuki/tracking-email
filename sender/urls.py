from django.urls import path

from . import views

app_name = 'sender'
urlpatterns = [
    path('', views.send_email, name='index'),
    path('image/', views.add_opened_email_history, name='image')
]