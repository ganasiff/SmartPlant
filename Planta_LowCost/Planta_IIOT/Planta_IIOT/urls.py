"""Planta_IIOT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Adds site header, site title, index title to the admin side. 
admin.site.site_header = 'Smart Hydrophonics'
admin.site.site_title = 'Hydrophonic System'
admin.site.index_title = 'Bienvenido a la Configuracion del Sistema'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SCADA.urls')),
    path("", include("authentication.urls")), 
    path('SCADA/', include('SCADA.urls')),
]
