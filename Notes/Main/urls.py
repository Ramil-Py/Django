from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.note),
    path('about/', views.about),
    path('', views.index),
]