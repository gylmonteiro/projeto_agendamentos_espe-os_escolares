from django.contrib import admin

# Register your models here.
from . models import Tipo, Usuario

admin.site.register(Tipo)

admin.site.register(Usuario)