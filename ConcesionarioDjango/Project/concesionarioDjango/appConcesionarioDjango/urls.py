from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('marca/<int:marca_id>/', views.marca, name='detail'),
    path('departamento/<int:departamento_id>/empleados', views.empleados, name='empleados'),
    path('empleado/<int:empleado_id>', views.empleado, name='empleado'),
    path('habilidad/<int:habilidad_id>', views.habilidad, name='habilidad')
]
