from django.urls import path
from . import views

urlpatterns = [
    path('templates/lista_productos/', views.lista_productos, name='lista_productos'),
    path('templates/crear_productos/', views.crear_producto, name='crear_producto'),
    path('templates/prestar_productos/<int:producto_id>', views.prestar_producto, name='prestar_producto'),
    path('templates/detalle_producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('templates/<int:producto_id>/prestamos_producto/', views.prestamos_producto, name='prestamos_producto'),
     path('templates/<int:producto_id>/agregar_stock/', views.agregar_stock, name='agregar_stock'),
]

