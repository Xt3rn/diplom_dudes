from django.urls import path
from . import views

app_name = 'diplom_spo'

urlpatterns = [
    path('', views.index, name='index'),
    path('diplom/<int:pk>/edit/', views.diplom_edit, name='edit'),
    path('create/', views.diplom_create, name='create'),
]
