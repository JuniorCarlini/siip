from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('inicio.urls')),
    path('proprietarios/', include('propriedades.urls')),
    path('armadilhas/', include('armadilhas.urls')),
    # outras URLs do seu projeto
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)