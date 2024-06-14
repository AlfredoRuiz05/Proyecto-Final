from django.urls import path
from . import views
app_name= "productos"
urlpatterns = [
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('desactivar/<int:producto_id>/', views.desactivar_producto, name='desactivar_producto'),
    path('detalle/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('', views.listar_productos, name='listar_productos'),
    path('lista_favoritos/', views.lista_favoritos, name='lista_favoritos'),
    path('producto/<int:producto_id>/agregar_favorito/', views.agregar_favorito, name='agregar_favorito'),
    path('producto/<int:producto_id>/eliminar_favorito/', views.eliminar_favorito, name='eliminar_favorito'),
    path('marcar_favorito/<int:producto_id>/', views.marcar_favorito, name='marcar_favorito'),
]



