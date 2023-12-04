from django.urls import path
from .views import propriedades

urlpatterns = [
    path('propriedades/<int:proprietario_id>/', propriedades, name='propriedades'),
]
