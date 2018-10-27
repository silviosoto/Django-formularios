from django import forms
from usuario.models import usuario

class UsuarioForms(forms.ModelForm):
    class Meta:
        model = usuario
        fields = [
            'nombre',
            'apellidos',
            'direccion',
            'ciudad',
            'longitud',
            'latitud',
            'estadogeo'
        ]
        labels = { 
            'nombre' : 'Nombre',
            'apellidos' : 'apellidos',
            'direccion' : 'direccion',
            'ciudad' : 'ciudad',
            'longitud' : 'longitud',
            'latitud' : 'latitud',
            'estadogeo' : 'estadogeo',
        }
        widtget ={
            'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
            'apellidos' : forms.TextInput(attrs={'class' : 'form-control'}),
            'direccion' : forms.TextInput(attrs={'class' : 'form-control'}),
            'ciudad' : forms.TextInput(attrs={'class' : 'form-control'}),
            'longitud' : forms.TextInput(attrs={'class' : 'form-control'}),
            'latitud' : forms.TextInput(attrs={'class' : 'form-control'}),
            'estadogeo' : forms.TextInput(attrs={'class' : 'form-control'})
        }