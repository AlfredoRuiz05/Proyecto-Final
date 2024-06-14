from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .models import Categoria
from .forms import CategoriaForm

def es_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(es_admin)
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('pagina_principal')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/crear_categoria.html', {'form': form})

@user_passes_test(es_admin)
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente.')
            return redirect('pagina_principal')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/editar_categoria.html', {'form': form})

@user_passes_test(es_admin)
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada exitosamente.')
        return redirect('pagina_principal')
    return render(request, 'categorias/eliminar_categoria.html', {'categoria': categoria})

@user_passes_test(es_admin)
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar_categorias.html', {'categorias': categorias})