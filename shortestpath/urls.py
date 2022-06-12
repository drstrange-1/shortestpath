from django.urls import path
from . import views

urlpatterns = [
    path('path/',views.path,name='path')
]