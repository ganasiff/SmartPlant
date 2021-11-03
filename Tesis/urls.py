"""Tesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from SCADA import views as SCADA_views
from cuentas_usuario import views as cuentas_views
#import SCADA

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',SCADA_views.indice, name='home'),
    path('login/',cuentas_views.login_view, name='Iniciar Sesion'),
    path('logout/',cuentas_views.logout_view,name='Cerrar Sesion'),
    path('register/', cuentas_views.register_view, name='Registrar Usuario'),
    path('settings/',SCADA_views.settings_scada,name='settings'),
    path('settings/list',SCADA_views.Settings_list.as_view(),name='settings_list'),
    path('settings/create',SCADA_views.Settings_Create.as_view(),name='settings_create'),
    path('settings/search/',SCADA_views.settings_scada_search,name='search_settings'),
    path('settings/edit/<int:pk>',SCADA_views.Settings_edit.as_view(),name='edit_config'),
    path('settings/<int:pk>/remove',SCADA_views.Settings_delete.as_view(),name='delete_config'),
    path('hello_world',SCADA_views.HelloWorld.as_view()),
]
