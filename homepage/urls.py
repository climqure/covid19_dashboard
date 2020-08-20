from django.urls import path, include
from . import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.index),
]

handler404 = 'homepage.views.handler404'
handler505 = 'homepage.views.handler500'
