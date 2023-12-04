from django.urls import path
from inicio.views import index, proprietarios

urlpatterns = [
    path('',index, name= 'index'),
    path('proprietarios/',proprietarios, name = 'proprietarios'),
]