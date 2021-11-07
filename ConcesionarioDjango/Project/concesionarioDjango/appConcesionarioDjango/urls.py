from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('marca/<int:marca_id>/', views.marca, name='marca'),
    path('marca/<int:marca_id>/coches', views.coches, name='coches'),
    path('coche/<int:coche_id>', views.coche, name='coche'),
    path('categoria/<int:categoria_id>', views.categoria, name='categoria')
]
