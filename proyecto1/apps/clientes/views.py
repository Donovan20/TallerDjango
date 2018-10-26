from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.clientes.models import Cliente
from django.views.generic import ListView
from apps.clientes.forms import ClienteForm

def index(request):
	return HttpResponse("Esta es la respuesta")

def plantilla(request):
	return render(request, 'clientes/index.html')

def especial(request):
	# contexto = { 
	# 	'clientes': Cliente.objects.all()
	# }
	return render(request, 'clientes/paginaEspecial.html', { clientes : Cliente.objects.all() })

def nuevoRegistro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('clientes:vistaClientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/clienteFormulario.html', {'form' : form})

def editarRegistro(request,idCliente):
    cliente = Cliente.objects.get(id=idCliente)
    if(request.method == 'GET'):
        form = ClienteForm(instance = cliente)
    else:
        form = ClienteForm(request.POST, instance = cliente)
        if form.is_valid():
            form.save()
        return redirect('clientes:vistaClientes')   
    return render(request, 'clientes/clienteFormulario.html', {'form' : form})
    
def eliminarRegistro(request, idCliente):
    cliente = Cliente.objects.get(id=idCliente)
    if(request.method == 'GET'):
        instance = cliente
        instance.delete()
    return redirect('clientes:vistaClientes')   
    

class viewCliente(ListView):
	model = Cliente
	queryset = Cliente.objects.all()
	template_name = 'clientes/paginaEspecial.html'