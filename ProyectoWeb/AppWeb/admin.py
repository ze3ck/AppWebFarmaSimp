from django.contrib import admin
from .models import Medicamento,Consulta,Retiro
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Register your models here.
admin.site.register(Medicamento)
admin.site.register(Consulta) 
admin.site.register(Retiro) 
admin.site.register(Permission) 
admin.site.register(ContentType) 