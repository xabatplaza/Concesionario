
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Marca, Categoria, Coche, Combustible
from pprint import pprint


def contact(request):
	return render(request, 'contact.html')

	
#devuelve el listado de marcas
def index(request):
	marcas = get_list_or_404(Marca.objects.order_by('nombre'))
	return render(request, 'index.html', {'lista_marcas': marcas })
	
#devuelve el listado de marcas y coches de cada marca
def marcas(request):
	marcas = get_list_or_404(Marca.objects.order_by('nombre'))
	coches = get_list_or_404(Coche.objects)
	context = {'lista_marcas': marcas, 'coches' : coches}
	return render(request, 'marcas.html', context)

#devuelve el listado de categorias y coches de cada categoria
def blog(request):
	categorias = get_list_or_404(Categoria.objects.order_by('nombre'))
	coches = get_list_or_404(Coche.objects)
	context = {'lista_categorias': categorias, 'coches' : coches }
	return render(request, 'blog.html', context)


#devuelve los coches de una marca
# def coches(request, marca_id):
# 	marca = get_object_or_404(Marca, pk=marca_id)
# 	coches =  marca.coche_set.all()
# 	context = {'marca': marca, 'coches' : coches }
# 	return render(request, 'marcas.html', context)
	

#devuelve los detalles de un coche por categoria
def indexcar(request):
	categorias = get_list_or_404(Categoria.objects.order_by('nombre'))
	coches = get_list_or_404(Coche.objects)
	context = {'lista_categorias': categorias, 'coches' : coches, 'categoria': categoria }
	return render(request, 'indexcar.html', context)


#devuelve los detalles de un coche
def coche(request, coche_id):
	coche = get_object_or_404(Coche, pk=coche_id)
	combustibles= coche.combustibles.all()
	context = {'coche' : coche, 'combustibles' : combustibles }
	return render(request, 'coche.html', context)


#devuelve los detalles de una categoria
def categoria(request, categoria_id):
	categoria = get_object_or_404(Categoria, pk=categoria_id)
	coches =  categoria.coche_set.all()
	context = { 'coches': coches, 'categoria' : categoria }
	return render(request, 'categoria.html', context)

#devuelve los detalles de una marca
def marca(request, marca_id):
	marca = get_object_or_404(Marca, pk=marca_id)
	coches = marca.coche_set.all()
	context = {'coches': coches, 'marca': marca }
	return render(request, 'marca.html', context)

def formulario(request):
	return render(request, 'formulario.html')