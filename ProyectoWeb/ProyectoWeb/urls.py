"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from AppWeb.views import Eliminar_productos,Agregar_productos,Restar_productos,Limpiar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('AppWeb.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('agregar/<int:producto_id>/',Agregar_productos,name="Agregar_productos"),
    path('eliminar/<int:producto_id>/',Eliminar_productos, name="Eliminar_productos"),
    path('restar/<int:producto_id>/',Restar_productos, name="Restar_productos"),
    path('limpiar/',Limpiar, name="Limpiar"),
    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)