from django.contrib import admin
from .models import DeviceModel

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'stock')  # Muestra el campo dinámico en la lista
    search_fields = ('nombre', 'precio')  # Agrega opciones de búsqueda
    list_filter = ('stock',)  # Permite filtrar por valoración
        

admin.site.register(DeviceModel)