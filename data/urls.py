from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('update', views.update),
    path('updesh', views.upload_countries),
    path('<slug:slug>/', views.detail_view, name='country'),
]
