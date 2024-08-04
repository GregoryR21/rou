from django.urls import path
from .views import *
from .import views 

urlpatterns = [
    path('', views.index),
    path('/', views.index),
    path('add_number', views.add_number),
    path('start', views.start),
    path('restart', views.restart),
]