from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Prestamo
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Producto, Prestamo
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Producto, Prestamo

# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

@login_required
@permission_required('producto.crear_producto', raise_exception=True)
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        cantidad = request.POST['cantidad']
        precio_unitario = request.POST['precio_unitario']
        descripcion = request.POST['descripcion']
        Producto.objects.create(
            nombre=nombre, cantidad=cantidad, precio_unitario=precio_unitario, descripcion=descripcion
        )
        return redirect('lista_productos')
    return render(request, 'crear_productos.html')

@login_required
def prestar_producto(request, producto_id):
    # Obtener el producto o lanzar error 404 si no se encuentra
    producto = get_object_or_404(Producto, id=producto_id)

    # Obtener todos los usuarios disponibles para seleccionar (puedes filtrarlos si es necesario)
    usuarios = User.objects.all()

    if request.method == 'POST':
        # Intentamos obtener la cantidad desde el formulario y convertirla a entero
        try:
            cantidad = int(request.POST['cantidad'])
            usuario_id = int(request.POST['usuario'])
        except (ValueError, KeyError):
            messages.error(request, "La cantidad ingresada o el usuario seleccionado no son válidos.")
            return redirect('prestar_producto', producto_id=producto.id)

        # Verificar que la cantidad no exceda el stock disponible
        if cantidad > producto.cantidad:
            messages.error(request, "No hay suficiente stock disponible.")
            return redirect('prestar_producto', producto_id=producto.id)

        # Verificar que el usuario seleccionado existe
        try:
            usuario_destino = User.objects.get(id=usuario_id)
        except User.DoesNotExist:
            messages.error(request, "El usuario seleccionado no existe.")
            return redirect('prestar_producto', producto_id=producto.id)

        # Crear el préstamo
        try:
            Prestamo.objects.create(
                usuario=request.user,  # Usuario que hace el préstamo
                producto=producto,
                cantidad=cantidad,
                usuario_destino=usuario_destino  # Usuario que recibe el préstamo
            )
        except Exception as e:
            messages.error(request, f"Hubo un error al procesar el préstamo: {str(e)}")
            return redirect('prestar_producto', producto_id=producto.id)

        # Actualizar el stock del producto
        producto.cantidad -= cantidad
        producto.save()

        # Mensaje de éxito
        messages.success(request, f"Se ha prestado {cantidad} unidad(es) de {producto.nombre} a {usuario_destino.username}.")
        return redirect('detalle_producto', producto_id=producto.id)

    # Renderizamos el formulario si la solicitud es GET
    return render(request, 'prestar_productos.html', {'producto': producto, 'usuarios': usuarios})
@login_required
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

@login_required
def prestamos_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    # Obtener todos los préstamos del producto específico
    prestamos = Prestamo.objects.filter(producto=producto)

    # Pasar los préstamos y el producto a la plantilla
    return render(request, 'prestamos_producto.html', {'producto': producto, 'prestamos': prestamos})

@login_required
def agregar_stock(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        try:
            cantidad_a_agregar = int(request.POST['cantidad'])
            if cantidad_a_agregar <= 0:
                messages.error(request, "La cantidad debe ser un número positivo.")
                return redirect('agregar_stock', producto_id=producto.id)

            # Agregar la cantidad al stock actual
            producto.cantidad += cantidad_a_agregar
            producto.save()

            messages.success(request, f"Se han agregado {cantidad_a_agregar} unidades de {producto.nombre}.")
            return redirect('detalle_producto', producto_id=producto.id)

        except ValueError:
            messages.error(request, "La cantidad ingresada no es válida.")
            return redirect('agregar_stock', producto_id=producto.id)

    return render(request, 'agregar_stock.html', {'producto': producto})