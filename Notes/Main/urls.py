from django.urls import path
from . import views

urlpatterns = [
    path('notes/<int:number>/', views.note),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('edit/<int:number>', views.edit, name='edit'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.index, name='home'),
]