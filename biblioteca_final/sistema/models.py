from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Libro(models.Model):
    """ Libros  """
    #codlibro = models.CharField(max_length=2, primary_key=True)
    nomlibro = models.CharField(max_length=100)
    editoriales_codeditorial= models.ForeignKey('Editorial', on_delete=models.PROTECT,related_name='get_libros')
    editoriales_codeditorial= models.ForeignKey('Editorial', on_delete=models.PROTECT,related_name='get_libros')
    autores_codautor= models.ManyToManyField('Autor')

    class Meta:
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.nomlibro


class Autor(models.Model):
    """ Autores """
    #codautor= models.CharField(max_length=2 , primary_key=True)
    nomautor= models.CharField(max_length=100) #Varchar
    paises_codpais= models.ForeignKey('Pais',on_delete=models.PROTECT,related_name='get_autores')

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nomautor

class Ejemplar(models.Model):
    """ Ejemplares """
    #codejemplar=models.CharField(max_length=2, primary_key=True)
    estejemplar=models.CharField(max_length=1)
    libros_codlibro = models.ForeignKey('Libro', on_delete=models.PROTECT,related_name='get_ejemplares' )
    libros_codlibro = models.ForeignKey('Libro', on_delete=models.PROTECT,related_name='get_ejemplares' )

    class Meta:
        verbose_name_plural = "Ejemplares"

    def __str__(self):
        return self.estejemplar

class Prestamo(models.Model):
    """ Préstamos """
    fecprestamo=models.DateField(auto_now_add=True)
    usuarios_codusuario = models.ForeignKey('Usuario', on_delete=models.PROTECT,related_name='get_prestamos1')
    usuarios_codusuario = models.ForeignKey('Usuario', on_delete=models.PROTECT,related_name='get_prestamos1')
    ejemplares_codejemplar = models.ForeignKey('Ejemplar', on_delete=models.PROTECT,related_name='get_prestamos2')
    fecdevolucion=models.DateField(auto_now_add=True)
    fecentrega=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Prestamos"


    #def __str__(self):
    #    return self.ejemplares_codejemplar


class Multa(models.Model):

    """ Multas """
    fecha=models.DateField(auto_now_add=True)
    valor= models.DecimalField(max_digits=6, decimal_places=5)
    estado= models.CharField(max_length=2)
    detalle= models.CharField(max_length=100) #Varchar
    prestamos_ejemplares_codejemplar = models.ForeignKey('Prestamo', on_delete=models.PROTECT,related_name='get_multas1' )
    prestamos_usuarios_codusuario = models.ForeignKey('Prestamo', on_delete=models.PROTECT,related_name='get_multas2' )
    valor= models.CharField(max_length=100)
    estado= models.CharField(max_length=2)
    detalle= models.CharField(max_length=100) #Varchar
    prestamos_ejemplares_codejemplar = models.ForeignKey('Prestamo', on_delete=models.PROTECT,related_name='get_multas1' )
    prestamos_usuarios_codusuario = models.ForeignKey('Prestamo', on_delete=models.PROTECT,related_name='get_multas2' )
    prestamos_fecprestamo = models.ForeignKey('Prestamo', on_delete=models.PROTECT,related_name='get_multas3' )

    class Meta:
        verbose_name_plural = "Multas"

    def __str__(self):
        return ("El valor de la multa es: "+self.valor+" por concepto de "+self.detalle)

class Usuario(models.Model):
    """ Usuarios """
    #codusuario= models.CharField(max_length=2 , primary_key=True)
    nomusuario= models.CharField(max_length=100) #Varchar
    tipousuario= models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.nomusuario

class Editorial(models.Model):
    """ Editoriales """
    #codeditorial= models.CharField(max_length=2 , primary_key=True)
    paises_codpais=models.ForeignKey('Pais',on_delete=models.PROTECT,related_name='get_editoriales')
    nomeditorial= models.CharField(max_length=100) #Varchar
    ciueditorial= models.CharField(max_length=100) #Varchar




    class Meta:
        verbose_name_plural = "Editoriales"

    def __str__(self):
        return self.nomeditorial

class Pais(models.Model):
    """ Paises """
    #codpais= models.CharField(max_length=2 , primary_key=True)
    nompais=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Paises"

    def __str__(self):
        return self.nompais
