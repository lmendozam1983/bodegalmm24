from django.contrib import admin
from .models import Producto

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'precio_unitario', 'fecha_ingreso')
    search_fields = ('nombre',)
    list_filter = ('fecha_ingreso',)