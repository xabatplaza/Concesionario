from django.contrib import admin
from .models import Marca, Categoria, Coche, Combustible, Contact
from django.contrib import messages
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Coche)
admin.site.register(Combustible)
admin.site.register(Contact)
# Register your models here.




