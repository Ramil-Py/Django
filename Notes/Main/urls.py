from django.urls import path
from . import views

urlpatterns = [
    path('notes/<int:id>/', views.note),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('', views.index, name='home'),
]