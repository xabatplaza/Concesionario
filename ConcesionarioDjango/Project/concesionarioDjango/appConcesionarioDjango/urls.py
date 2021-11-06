from django.urls import path
from . import views

urlpatterns = [
    path('indexcar', views.indexcar, name='indexcar'),
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('fullwidth', views.fullwidth, name='fullwidth'),
    path('', views.index, name='index'),
    path('singlepost', views.singlepost, name='singlepost'),
    path('', views.index, name='index'),

    path('departamento/<int:departamento_id>/', views.detail, name='detail'),
    path('departamento/<int:departamento_id>/empleados', views.empleados, name='empleados'),
    path('empleado/<int:empleado_id>', views.empleado, name='empleado'),
    path('habilidad/<int:habilidad_id>', views.habilidad, name='habilidad')
]
