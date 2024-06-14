from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Favorito
from .forms import ProductoForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

def es_admin(user):
    return user.is_authenticated and user.is_staff
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'productos/detalles_producto.html', {'producto': producto})

def listar_productos(request):
    productos = Producto.objects.all()
    buscador = request.GET.get('buscador', '')
    if buscador:
        productos = productos.filter(nombre__icontains=buscador)
    return render(request, 'productos/listar_productos.html', {'productos': productos})

@user_passes_test(es_admin)
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('productos:listar_productos')  # Ajuste aquí
        else:
            messages.error(request, 'Error al crear el producto. Por favor, revisa el formulario.')
    else:
        form = ProductoForm()
    return render(request, 'productos/crear_producto.html', {'form': form})

@user_passes_test(es_admin)
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('productos:listar_productos')
        else:
            messages.error(request, 'Error al actualizar el producto. Por favor, revisa el formulario.')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form, 'producto': producto})

@user_passes_test(es_admin)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        # Eliminar el producto
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('pagina_principal')
    else:
        # Mostrar confirmación de eliminación de producto
        return render(request, 'productos/eliminar_producto.html', {'producto': producto})

@user_passes_test(es_admin)
def desactivar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        producto.activo = False
        producto.save()
        messages.success(request, 'Producto desactivado exitosamente.')
        return redirect('pagina_principal')
    return render(request, 'productos/desactivar_producto.html', {'producto': producto})

@login_required
def agregar_favorito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    Favorito.objects.get_or_create(user=request.user, producto=producto)
    return redirect('productos:detalle_producto', producto_id=producto.id)

@login_required
def eliminar_favorito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    favorito = Favorito.objects.filter(user=request.user, producto=producto)
    if favorito.exists():
        favorito.delete()
    return redirect('productos:detalle_producto', producto_id=producto.id)

@login_required
def lista_favoritos(request):
    favoritos = Favorito.objects.filter(user=request.user).select_related('producto')
    return render(request, 'productos/listar_favoritos.html', {'favoritos': favoritos})


@login_required
def marcar_favorito(request, producto_id):
    # Verificar si el usuario es administrador
    if request.user.is_staff:
        return HttpResponseForbidden("Forbidden: Solo usuarios registrados pueden marcar como favorito.")

    producto = get_object_or_404(Producto, id=producto_id)
    favorito, created = Favorito.objects.get_or_create(user=request.user, producto=producto)
    if created:
        messages.success(request, f'El producto {producto.nombre} ha sido añadido a tus favoritos.')
    else:
        messages.info(request, f'El producto {producto.nombre} ya está en tus favoritos.')
    return redirect('productos:lista_favoritos')



