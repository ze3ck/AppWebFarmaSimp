from argparse import Namespace
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home,panelAdmin,panelMedico,panelBodeguero,panelFarmaceutico,caducarMedicamentos,eliminarCuentas,generarInformes,modificarCuentas,ConsultarMedicamentos,registrarConsulta,registrarCuentas,registrarMedicamentos, reservarMedicamentos,retiroMedicamentos,verCuentas,carrito,caducar

from django.conf import settings
from django.conf.urls.static import static
from .views import  Agregar_productos, Eliminar_productos, Restar_productos,Limpiar


urlpatterns = [

    path('',home,name='home'),
    path('panel_medico/',panelMedico,name='panelMedico'),
    path('panel_bodeguero/',panelBodeguero,name='panelBodeguero'),
    path('panel_farmaceutico/',panelFarmaceutico,name='panelFarmaceutico'),
    path('panel_admin/',panelAdmin,name='panelAdmin'),
    path('registrar_medicamentos/',registrarMedicamentos,name='registrarMedicamentos'),
    path('registrar_consulta/',registrarConsulta,name='registrarConsulta'),
    path('ver_medicamentos/',ConsultarMedicamentos,name='ConsultarMedicamentos'),
    path('caducar_medicamentos/',caducarMedicamentos,name='caducarMedicamentos'),
    path('eliminar_cuentas/<id>',eliminarCuentas,name='eliminarCuentas'),
    path('generar_informes/',generarInformes,name='generarInformes'),
    path('modificar_cuentas/<id>',modificarCuentas,name='modificarCuentas'),
    path('ver_cuentas/',verCuentas,name='verCuentas'),
    path('registrar_cuentas/',registrarCuentas,name='registrarCuentas'),
    path('retirar_medicamentos/',retiroMedicamentos,name='retiroMedicamentos'),
    path('reservar_medicamentos/',reservarMedicamentos,name='reservarMedicamentos'),
    path('carrito/',carrito,name='carrito'),
    path('caducar/<id>',caducar,name='caducar'),
    
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
