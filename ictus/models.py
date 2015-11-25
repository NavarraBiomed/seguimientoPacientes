from django.db import models
from django.utils import timezone

_SEXO = (
	("00", "Hombre"),
	("01", "Mujer")
	)

_TIPO = (
	("00", "Tipo 1"),
	("01", "Tipo 2")
	)


class Paciente(models.Model):
    NHC = models.IntegerField()
    nombre = models.CharField(max_length = 30)
    sexo = models.CharField(choices = _SEXO, max_length = 2)
    fecha = models.DateField(default = timezone.now)

    def __str__(self):
        return str(self.NHC)

class Episodio(models.Model):
	paciente = models.ForeignKey('Paciente')
	h_inicio = models.DateTimeField();
	tipo = models.CharField(choices = _TIPO, max_length = 2)

	def __str__(self):
		return self.tipo+" 	("+str(self.h_inicio)+")"

class Basal(models.Model):
	episodio = models.ForeignKey('Episodio')
	rank_basal = models.IntegerField(verbose_name = "Ranking Basal")
	deterioro_fluct = models.IntegerField(verbose_name = "Deteriorio")
	transf_hemor = models.IntegerField(verbose_name = "Transformación hemorrágica")
	hta = models.IntegerField(verbose_name = "HTA") 
	dm = models.IntegerField(verbose_name = "Diabetes mellitus") 
	dl = models.IntegerField(verbose_name = "Dislipemia")
	fa = models.IntegerField(verbose_name = "Fibrilación auricular")
	cardiopatia = models.IntegerField(verbose_name = "Cardiopatia")

class Intervencion(models.Model):
	episodio = models.ForeignKey('Episodio')
	anticoag_nombre = models.CharField(max_length=300)

class Extraccion(models.Model):
        Intervencion = models.ForeignKey('Intervencion')
        variable_extraccion = models.IntegerField(verbose_name="Placeholder variable")

class Tratamiento(models.Model):
        episodio = models.ForeignKey('Episodio')
        ecocardio_cardiembolico = models.IntegerField(verbose_name="Cardioembolicas")
        ecotsa = models.CharField(max_length = 3000)
        ###Más variables aquí##)

class Seguimiento(models.Model):
        episodio = models.ForeignKey('Episodio')
        variable_seguimiento = models.CharField(max_length = 30, verbose_name="Placeholder variable seg")
        ##variables##
