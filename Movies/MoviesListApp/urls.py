from django.urls import path
from . import views
urlpatterns = [path('', views.Movies_list, name='Movies_list'),
               path('publisher/<int:pk>/', views.publisher_edit, name='publisher_edit'),
               path('publisher/new/', views.publisher_edit, name='publisher_create')]