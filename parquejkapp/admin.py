from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.plazas import Plazas
from .models.vehiculos import Vehiculos
from .models.facturas import Facturas

admin.site.register(User)
admin.site.register(Vehiculos)
admin.site.register(Facturas)
admin.site.register(Plazas)