from django import forms
from sistema.models import Libro, Ejemplar, Prestamo, Multa, Usuario, Editorial, Pais, Autor

class LibroForm(forms.ModelForm):
	class Meta:
		model=Libro
		fields='__all__'
		widgets={
		'nomlibro':forms.TextInput(attrs={'class':'form-control'})		
		}

class EjemplarForm (forms.ModelForm):
	class Meta:
		model=Ejemplar
		fields='__all__'
		widgets={
		'estejemplar':forms.TextInput(attrs={'class':'form-control'})
		}

class PrestamoForm (forms.ModelForm):
	class Meta:
		model=Prestamo
		fields='__all__'
		widgets={
		'fecprestamo':forms.DateInput(attrs={'class':'form-control datepicker'}),
		'fecdevolucion':forms.DateInput(attrs={'class':'form-control datepicker'}),
		'fecentrega':forms.DateInput(attrs={'class':'form-control datepicker'})
		}

class MultaForm (forms.ModelForm):
	class Meta:
		model=Multa
		fields='__all__'
		widgets={
		'fecha':forms.DateInput(attrs={'class':'form-control datepicker'}),
		'valor':forms.TextInput(attrs={'class':'form-control'}),
		'estado':forms.TextInput(attrs={'class':'form-control'}),
		'detalle':forms.Textarea(attrs={'class':'form-control'})
		}

class UsuarioForm (forms.ModelForm):
	class Meta:
		model=Usuario
		fields='__all__'
		widgets={
		'nomusuario':forms.TextInput(attrs={'class':'form-control'}),
		'tipousuario':forms.TextInput(attrs={'class':'form-control'})
		}

class EditorialForm (forms.ModelForm):
	class Meta:
		model=Editorial
		fields='__all__'
		widgets={
		'nomeditorial':forms.TextInput(attrs={'class':'form-control'}),
		'ciueditorial':forms.TextInput(attrs={'class':'form-control'})
		}

class PaisForm (forms.ModelForm):
	class Meta:
		model=Pais
		fields='__all__'
		widgets={
		'nompais':forms.TextInput(attrs={'class':'form-control'})
		}

class AutorForm (forms.ModelForm):
	class Meta:
		model=Autor
		fields='__all__'
		widgets={
		'nomautor':forms.TextInput(attrs={'class':'form-control'})
		}

