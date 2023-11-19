from django.urls import path
from inicio.views import index, proprietarios
 
urlpatterns = [
    path('',index),
    path('proprietarios/',proprietarios, name = 'proprietarios'),
]