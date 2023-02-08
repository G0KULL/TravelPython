from . import views
from django.urls import path

urlpatterns = [
    # path('operations/', views.operations, name= 'operations'),
    path('', views.demo, name='demo'),


]