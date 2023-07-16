from django.contrib import admin
from django.urls import path, include

## Aqui são definidas as rotas gerais

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]
