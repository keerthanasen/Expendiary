from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.list, name = 'list'),
    path('add', views.ProjectCreateView.as_view(), name='add'),
    path('<slug:project_slug>', views.description, name = "description"),
]