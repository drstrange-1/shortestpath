from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('path/',views.path,name='path')
    
]