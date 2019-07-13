from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from .models import Libro, Ejemplar, Prestamo, Multa, Usuario, Editorial, Pais, Autor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView


class LibroView(LoginRequiredMixin,ListView):
	model = Libro
	template_name="sistema/libro.html"

class EjemplarView(LoginRequiredMixin,ListView):
	model = Ejemplar
	template_name="sistema/ejemplar.html"

class PrestamoView(LoginRequiredMixin,ListView):
	model = Prestamo
	template_name="sistema/prestamo.html"

class MultaView(LoginRequiredMixin,ListView):
	model = Multa
	template_name="sistema/multa.html"

class UsuarioView(LoginRequiredMixin,ListView):
	model = Usuario
	template_name="sistema/usuario.html"

class EditorialView(LoginRequiredMixin,ListView):
	model = Editorial
	template_name="sistema/editorial.html"

class PaisView(LoginRequiredMixin,ListView):
	model = Pais
	template_name="sistema/pais.html"

class AutorView(LoginRequiredMixin,ListView):
	model = Autor
	template_name="sistema/autor.html"

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password = form.cleaned_data ['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render (request,'registration/register.html',context)
		
@login_required
def origen(request):
    return render(request, 'sistema/origen.html')

def logout(request):
	return render (request,'registration/logout.html')
