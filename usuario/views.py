from django.shortcuts import render, redirect
from django.http import HttpResponse
from  usuario.forms import UsuarioForms
# Create your views here.

def index(request):
    return render(request, 'index.html')

def usuario_view(request):
    if request.method == 'POST':
        form = UsuarioForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = UsuarioForms()
    return render(request, 'form_usuario.html', {'form': form})