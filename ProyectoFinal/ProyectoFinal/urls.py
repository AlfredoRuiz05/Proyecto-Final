from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('', views.home, name='pagina_principal'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('registrarme/',views.registrarme, name= 'registrarme'),
    path('productos/', include('apps.productos.urls')),
    path('categorias/', include('apps.categorias.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






