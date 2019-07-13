from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
	path('libro/',views.LibroView.as_view(), name='libro'), #href="{% url 'libro' %}" --> en el template
	path('ejemplar/',views.EjemplarView.as_view(), name='ejemplar'),
	path('prestamo/',views.PrestamoView.as_view(), name='prestamo'),
	path('multa/',views.MultaView.as_view(), name='multa'), 
	path('usuario/',views.UsuarioView.as_view(), name='usuario'), 
	path('editorial/',views.EditorialView.as_view(), name='editorial'), 
	path('pais/',views.PaisView.as_view(), name='pais'), 
	path('autor/',views.AutorView.as_view(), name='autor'), 

]