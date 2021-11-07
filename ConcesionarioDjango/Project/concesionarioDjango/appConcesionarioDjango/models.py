from django.db import models

class Marca(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 nombre = models.CharField(max_length=50)
 anyoDeCreacion = models.IntegerField()
 fundador = models.CharField(max_length=50)
 def __str__(self):
        return self.nombre

class Categoria(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 nombre = models.CharField(max_length=50)
 def __str__(self):
        return self.nombre

class Coche(models.Model):
 # Campo para la relación one-to-many
 marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
 categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
 nombre = models.CharField(max_length=40)
 fecha_creacion = models.DateField()
 # Es posible indicar un valor por defecto mediante 'default'
 caballosPotencia = models.IntegerField(default=0)

 def __str__(self):
        return self.nombre


   
