from django.urls import path
from apps.clientes.views import index, plantilla, especial, viewCliente, nuevoRegistro, editarRegistro, eliminarRegistro

app_name = "clientes"
urlpatterns = [
	path('', index),
    path('index', index),
    path('plantilla', plantilla, name="plantilla"),
    path('especial', viewCliente.as_view(), name="vistaClientes"),
    path('nuevoRegistro',nuevoRegistro, name="nuevoRegistro"),
    path('editarRegistro/<idCliente>',editarRegistro, name="editarRegistro"),
    path('eliminarRegistro/<idCliente>',eliminarRegistro, name="eliminarRegistro")
]