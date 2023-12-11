# armadilhas/urls.py
from django.urls import path
from .views import armadilhas

urlpatterns = [
    path('<int:propriedade_id>/', armadilhas, name='armadilhas'),
]