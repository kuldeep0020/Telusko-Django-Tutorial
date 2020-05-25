from django.urls import path

from travello import views

urlpatterns = [
    path('', views.index),
    path('index.html/', views.index),
]
