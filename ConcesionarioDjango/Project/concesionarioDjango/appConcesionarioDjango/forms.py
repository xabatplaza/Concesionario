from django import forms

class FormularioContacto(forms.Form):
    nombres=forms.charField()
    apellidos=forms.charField()
    correo=forms.emailField()
    #contraseñas=forms.charField()
