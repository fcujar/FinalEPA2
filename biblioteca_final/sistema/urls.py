from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
	path('libro/',views.LibroView.as_view(), name='libro'), #href="{% url 'libro' %}" --> en el template
	path('ejemplar/',views.EjemplarView.as_view(), name='ejemplar'),
	path('prestamo/',views.PrestamoView.as_view(), name='prestamo'),
<<<<<<< HEAD
	path('multa/',views.MultaView.as_view(), name='multa'), 
	path('usuario/',views.UsuarioView.as_view(), name='usuario'), 
	path('editorial/',views.EditorialView.as_view(), name='editorial'), 
	path('pais/',views.PaisView.as_view(), name='pais'), 
	path('autor/',views.AutorView.as_view(), name='autor'), 

]
=======
	path('multa/',views.MultaView.as_view(), name='multa'),
	path('usuario/',views.UsuarioView.as_view(), name='usuario'),
	path('editorial/',views.EditorialView.as_view(), name='editorial'),
	path('pais/',views.PaisView.as_view(), name='pais'),
	path('autor/',views.AutorView.as_view(), name='autor'),

	path('libroCreate/',views.LibroCreate.as_view(), name='libroCreate'), #href="{% url 'libro' %}" --> en el template
	path('ejemplarCreate/',views.EjemplarCreate.as_view(), name='ejemplarCreate'),
	path('prestamoCreate/',views.PrestamoCreate.as_view(), name='prestamoCreate'),
	path('multaCreate/',views.MultaCreate.as_view(), name='multaCreate'),
	path('usuarioCreate/',views.UsuarioCreate.as_view(), name='usuarioCreate'),
	path('editorialCreate/',views.EditorialCreate.as_view(), name='editorialCreate'),
	path('paisCreate/',views.PaisCreate.as_view(), name='paisCreate'),
	path('autorCreate/',views.AutorCreate.as_view(), name='autorCreate'),


]
>>>>>>> Comit final
