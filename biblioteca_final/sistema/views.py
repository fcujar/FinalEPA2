from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from .models import Libro, Ejemplar, Prestamo, Multa, Usuario, Editorial, Pais, Autor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView

from django.views.generic import ListView, DetailView, CreateView
from sistema.forms import *


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


###################################LO NUEVO

class LibroCreate(LoginRequiredMixin,CreateView):
	model=Libro
	form_class=LibroForm
	template_name='sistema/libroCreate.html'
	succes_url=reverse_lazy('libroCreate')
	#success_url="/success/"

class EjemplarCreate(LoginRequiredMixin,CreateView):
	model=Ejemplar
	form_class=EjemplarForm
	template_name='sistema/ejemplarCreate.html'
	succes_url=reverse_lazy('ejemplarCreate')

class PrestamoCreate(LoginRequiredMixin,CreateView):
	model=Prestamo
	form_class=PrestamoForm
	template_name='sistema/prestamoCreate.html'
	succes_url=reverse_lazy('prestamoCreate')

class MultaCreate(LoginRequiredMixin,CreateView):
	model=Multa
	form_class=MultaForm
	template_name='sistema/multaCreate.html'
	succes_url=reverse_lazy('multaCreate')

class UsuarioCreate(LoginRequiredMixin,CreateView):
	model=Usuario
	form_class=UsuarioForm
	template_name='sistema/usuarioCreate.html'
	succes_url=reverse_lazy('usuarioCreate')

class EditorialCreate(LoginRequiredMixin,CreateView):
	model=Editorial
	form_class=EditorialForm
	template_name='sistema/editorialCreate.html'
	succes_url=reverse_lazy('editorialCreate')

class PaisCreate(LoginRequiredMixin,CreateView):
	model=Pais
	form_class=PaisForm
	template_name='sistema/paisCreate.html'
	succes_url=reverse_lazy('paisCreate')

class AutorCreate(LoginRequiredMixin,CreateView):
	model=Autor
	form_class=AutorForm
	template_name='sistema/autorCreate.html'
	succes_url=reverse_lazy('autorCreate')
