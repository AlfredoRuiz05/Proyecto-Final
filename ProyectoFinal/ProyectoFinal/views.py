from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import logout
#from apps.usuarios.models import Usuario
from apps.productos.models import Producto
from apps.categorias.models import Categoria
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('pagina_principal')
        else:
            messages.error(request, 'Usuario y/o contraseña incorrecta.')
    return render(request, 'login.html')




def home(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    buscador = request.GET.get('buscador', '')
    if buscador:
        productos = productos.filter(nombre__icontains=buscador)
    return render(request, 'home.html', {'productos': productos, 'categorias': categorias, 'buscador': buscador})
@login_required
def logout(request):
    logout(request)
    return redirect('pagina_principal')
#def registrarme(request):
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('pagina_principal')  # Redirigir a la página principal después del registro exitoso
#    else:
#        form = UserCreationForm()
#    return render(request, 'usuarios/registrarme.html', {'form': form})