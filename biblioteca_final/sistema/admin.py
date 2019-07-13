from django.contrib import admin
from sistema.models import Libro,Ejemplar,Prestamo,Multa,Usuario,Editorial,Pais,Autor
# Register your models here.
admin.site.register(Libro)
admin.site.register(Ejemplar)
admin.site.register(Prestamo)
admin.site.register(Multa)
admin.site.register(Usuario)
admin.site.register(Editorial)
admin.site.register(Pais)
admin.site.register(Autor)
