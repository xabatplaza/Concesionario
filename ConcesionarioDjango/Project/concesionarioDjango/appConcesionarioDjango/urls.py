from django.urls import path
from . import views
from django.conf import settings

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.indexcar, name='indexcar'),
    path('contact', views.contact, name='contact'),
    
    path('marcas', views.marcas, name='marcas'),
    path('blog', views.blog, name='blog'),
    
    path('marca/<int:marca_id>/', views.marca, name='marca'),
    
    #path('marca/<int:marca_id>/coches', views.coches, name='coches'),
    
    path('coche/<int:coche_id>', views.coche, name='coche'),
    path('categoria/<int:categoria_id>', views.categoria, name='categoria'),

    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='templates/logout.html'), name='logout'),
]
