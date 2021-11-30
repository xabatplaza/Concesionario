from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexcar, name='indexcar'),
    path('contact', views.contact, name='contact'),
    
    path('marcas', views.marcas, name='marcas'),
    path('blog', views.blog, name='blog'),
    
    path('marca/<int:marca_id>/', views.marca, name='marca'),
    
    #path('marca/<int:marca_id>/coches', views.coches, name='coches'),
    
    path('coche/<int:coche_id>', views.coche, name='coche'),
    path('categoria/<int:categoria_id>', views.categoria, name='categoria'),

    path('formulario/', views.formulario, name='formulario'),
    path('usuariocreado/', views.usuariocreado, name='usuariocreado')
]
