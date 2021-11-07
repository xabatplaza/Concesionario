
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Marca, Categoria, Coche

#devuelve el listado de empresas
def index(request):
	marcas = get_list_or_404(Marca.objects.order_by('nombre'))
	context = {'lista_marcas': marcas }
	return render(request, 'index.html', context)

#devuelve los datos de una marca
def marca(request, marca_id):
	marca = get_object_or_404(Marca, pk=marca_id)
	#output = ', '.join([str(marca.id), marca.nombre, str(marca.anyoDeCreacion), marca.fundador])
	context = {'marca': marca }
	return render(request, 'marca.html', context)

#devuelve los coches de una marca
def coches(request, marca_id):
	marca = get_object_or_404(Marca, pk=marca_id)
	coches =  marca.coche_set.all()
	context = {'marca': marca, 'coches' : coches }
	return render(request, 'coches.html', context)
	

#devuelve los detalles de un coche
def coche(request, coche_id):
	coche = get_object_or_404(Coche, pk=coche_id)
	context = { 'coche': coche }
    return render(request, 'coche.html', context)
	

	#output = ', '.join([str(coche.id), coche.nombre, str(coche.fecha_creacion), str(coche.caballosPotencia), str(coche.marca), str(coche.categoria)])
	#categorias = ', '.join([c.nombre for c in coche.categorias.all()])
	#output = f"{datos_coche} // Categoria: {categorias}"
	

#devuelve los detalles de una categoria
def categoria(request, categoria_id):
	categoria = get_object_or_404(Categoria, pk=categoria_id)
	coches =  categoria.coche_set.all()
	context = { 'coches': coches, 'categoria' : categoria }
    return render(request, 'categoria.html', context)

