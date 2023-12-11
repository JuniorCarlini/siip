from django.urls import path
from .views import armadilhas

urlpatterns = [
    # suas outras URLs
    path('propriedade/<int:propriedade_id>/armadilhas/', armadilhas, name='armadilhas'),
]
