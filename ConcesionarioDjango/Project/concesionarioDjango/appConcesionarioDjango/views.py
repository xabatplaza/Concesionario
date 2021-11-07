from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Marca, Categoria, Coche

#devuelve el listado de empresas
def index(request):
	marcas = Marca.objects.order_by('nombre')
	output = ', '.join([m.nombre for m in marcas])
	return HttpResponse(output)

#devuelve los datos de una marca
def marca(request, marca_id):
	marca = Marca.objects.get(pk=marca_id)
	output = ', '.join([str(marca.id), marca.nombre, str(marca.anyoDeCreacion), marca.fundador])
	return HttpResponse(output)

#devuelve los coches de una marca
def coches(request, marca_id):
	marca = Marca.objects.get(pk=marca_id)
	output = ', '.join([c.nombre for c in marca.coche_set.all()])
	return HttpResponse(output)

#devuelve los detalles de un coche
def coche(request, coche_id):
	coche = Coche.objects.get(pk=coche_id)
	output = ', '.join([str(coche.id), coche.nombre, str(coche.fecha_creacion), str(coche.caballosPotencia), str(coche.marca), str(coche.categoria)])
	return HttpResponse(output)

#devuelve los detalles de una categoria
def categoria(request, categoria_id):
	categoria = Categoria.objects.get(pk=categoria_id)
	output = ', '.join([str(categoria.id), categoria.nombre, str([c.nombre for c in categoria.coche.all()])])
	return HttpResponse(output)

