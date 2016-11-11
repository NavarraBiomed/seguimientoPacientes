from django.db import models
from django.utils import timezone
import locale

_SEXO = (
	("00", "Hombre"),
	("01", "Mujer")
	)

_TIPO = (
	("00", "Tipo 1"),
	("01", "Tipo 2")
	)

_SI_NO_INDET = (
        ("00", "No"),
        ("01", "Sí"),
        ("02", "Indeterminado")
        )

_ETNIA = (
        ("00", "Caucásico mediterráneo"),
        ("01", "Otro caucásico"),
        ("02", "Latinoamericano-caribeño"),
        ("03", "Asiático"),
        ("04", "Negro o afro-americano"),
        ("05", "Otra raza"),
        ("06", "No determinado")
        )

_DIABETES = (
        ("01", "Tipo 1"),
        ("02", "Tipo 2"),
        ("03", "Desconocido")
        )

_TABACO = (
        ("00", "No fumador"),
        ("01", "Exfumador"),
        ("02", "Fumador pasivo"),
        ("03", "Fumador actual"),
        ("04", "Desconocido")
        )

_ALCOHOL = (
        ("00", "No"),
        ("01", "A diario"),
        ("02", "Ocasionalmente"),
        ("03", "Exhabito enólico")
        )

_EJERCICIO = (
        ("00", "No"),
        ("01", "Menos de 3 días/semana"),
        ("02", "Más de 3 días/semana"),
        ("04", "A diario")
        )

_CARDIOPATIA = (
        ("00", "Ninguna"),
        ("01", "Miocardiopatía dilatada"),
        ("02", "Miocardiopatía hipertrófica"),
        ("03", "Miocardiopatía restrictiva"),
        ("04", "Cardiopatía valvular"),
        ("05", "Cardiopatía isquémica"),
        ("06", "Cardiopatía hipertensiva"),
        ("07", "Dos o más cardiopatías"),
        ("08", "Desconocida"),
        ("09", "Otras cardiopatías"),
        ("10", "Bloqueo AV marcapasos")
        )

_RANKIN = (
        ("0", "Sin síntomas"),
        ("1", "Sin incapacidad importante"),
        ("2", "Incapacidad leve"),
        ("3", "Incapacidad moderada"),
        ("4", "Incapacidad moderadamente grave"),
        ("5", "Incapacidad grave"),
        ("6", "Muerte")
        )

_TIPO_ICTUS = (
        ("00", "Isquémico"),
        ("01", "Hemorrágico"),
        ("02", "Isquemia transitoria"),
        ("03", "Mimic")
        )

_TOAST = (
        ("1", "Aterotrombótico"),
        ("2", "Cardioembólico"),
        ("3", "Lacunar"),
        ("4", "De otra etiología determinada/causa infrecuente"),
        ("5", "Indeterminado, >2 causas"),
        ("6", "Indeterminado, tras estudio completo"),
        ("7", "Indeterminado, estudio incompleto")
        )

_OXFORDSHIRE = (
        ("TACI", "Infartos completos de la circulación anterior"),
        ("PACI", "Infartos parciales de la circulación anterior"),
        ("LACI", "Infartos lacunares"),
        ("POCI", "infartos de la circulación posterior")
        )

_ESCALA_AIT = zip (range(0,8), range(0,8))

_HEMO_TIPO = (
        ("00", "No"),
        ("01", "Hematoma lobar"),
        ("02", "Hematoma subpratentorial profundo"),
        ("03", "Hematoma cerebeloso, profundo"),
        ("04", "Hematoma troncoencefálico, profundo")
        )

_HEMO_ETIOLOGIA = (
        ("1", "Hemorragia primaria-HTA"),
        ("2", "Hemorragia secundaria")
        )

_OCLUSION = (
        ("0", "ACI proximal"),
        ("1", "ACI proximal y tandem"),
        ("2", "ACI distal terminus"),
        ("3", "ACI distal terminus y tandem"),
        ("4", "M1"),
        ("5", "M2"),
        ("6", "BASILAR"),
        ("7", "Otros")
        )

_TIBIDTC = zip (range(0,6), range(0,6))

_NIHSS = zip (list(range(0,31)), list(range(0,31)))
_NIHSS_ALTA = zip(list(range(0,31)), list(range(0,31)) )
_MRS = zip (list(range(0,7)), list( range(0,7)))

class Paciente(models.Model):
    NHC = models.IntegerField(verbose_name="NHC")
    nombre = models.CharField(verbose_name = "Nombre del paciente ", max_length = 30)
    iniciales = models.CharField(verbose_name = "Iniciales del paciente", max_length = 6)
    fecha_nacimiento = models.DateField(verbose_name = "Fecha de nacimiento")
    genero = models.CharField(verbose_name = "Género", choices = _SEXO, max_length = 2)
    grupo_etnico = models.CharField(verbose_name = "Grupo étnico", choices = _ETNIA, max_length = 2)

    def __str__(self):
        return str(self.NHC)

class Episodio(models.Model):
        paciente = models.ForeignKey('Paciente')
        fecha_inicio = models.DateField(verbose_name = "Fecha ictus",default = timezone.now)
        h_inicio = models.TimeField(verbose_name = "Hora de inicio", default = timezone.now)
        hora_inicio_indet = models.BooleanField( verbose_name = "Hora indeterminada", default = False)
        tipo_ictus = models.CharField( verbose_name = "Tipo de ictus", choices = _TIPO_ICTUS, max_length = 2)
        nihss_ingreso = models.IntegerField( verbose_name = "NIHSS Ingreso", choices = _NIHSS)
        nihss_alta = models.IntegerField( verbose_name = "NIHSS Alta", choices = _NIHSS_ALTA)
        mrs_alta = models.IntegerField( verbose_name = "mRS alta", choices = _MRS)
        toast = models.CharField( verbose_name = "TOAST", choices = _TOAST, max_length = 2)
        oxfordshire = models.CharField(verbose_name ="OXFORDSHIRE", choices = _OXFORDSHIRE, max_length = 4)
        ait = models.CharField(verbose_name = "AIT", choices = _SI_NO_INDET, max_length = 2)
        ait_duracion = models.TimeField(verbose_name = "Duración AIT", default = timezone.now)
        ait_neuroimagen = models.CharField(verbose_name = "Neuroimagen AIT", choices = _SI_NO_INDET, max_length = 2)
        ait_bcd2 = models.IntegerField(verbose_name = "ABCD2", choices = _ESCALA_AIT, blank = True, null=True)
        hemo_localizacion = models.CharField(verbose_name ="HEMO localización", choices = _HEMO_TIPO, max_length = 2)
        hemo_etiologia = models.CharField(verbose_name = "HEMO etiología", choices = _HEMO_ETIOLOGIA, max_length = 2)
        ev = models.CharField(verbose_name = "EV", choices = _SI_NO_INDET, max_length = 2)
        recanalizacion_dtc = models.CharField(verbose_name = "Recanalización doble transcraneal", choices = _SI_NO_INDET, max_length = 2)
        oclusion = models.CharField(verbose_name = "Oclusión", choices = _SI_NO_INDET, max_length = 2)
        oclusion_lugar = models.CharField( verbose_name = "Lugar de oclusión", choices = _OCLUSION, max_length = 2)
        tibidtc = models.IntegerField(verbose_name = "TIBI/DTC", choices = _TIBIDTC, blank = True, null=True)
        tratamiento_interarterial = models.CharField(verbose_name = "Tratamiento Interarterial", choices = _SI_NO_INDET, max_length = 2)

        def __str__(self):
            locale.setlocale(locale.LC_TIME, '')
            return self.paciente.nombre + " - " + _TIPO_ICTUS[int(self.tipo_ictus)][1] + " ("+self.fecha_inicio.strftime("%d de %B, %Y")+")"
        ###elf.paciente.nombre + " - "+self.tipo_ictus+" ("+str(self.h_default = timezone.nowinicio)+")"

        def description(self):
            locale.setlocale(locale.LC_TIME, '')
            return self.fecha_inicio.strftime("%d de %B, %Y")+" - " + _TIPO_ICTUS[int(self.tipo_ictus)][1]


class Basal(models.Model):
    class Meta:
        verbose_name_plural = "Basales"

    episodio = models.ForeignKey('Episodio')
    ictus_previo = models.CharField(verbose_name ="Ictus previo", choices = _SI_NO_INDET, max_length = 2)
    HTA = models.CharField(verbose_name = "Hipertensión", choices = _SI_NO_INDET, max_length = 2)
    HTA_tiempo = models.IntegerField(verbose_name = "Tiempo evolucón HTA")
    diabetes = models.CharField(verbose_name = "Diabetes mellitus", choices = _SI_NO_INDET, max_length = 2)
    tipo_diabetes = models.CharField (verbose_name = "Tipo de DM", choices = _DIABETES, max_length = 2)
    tiempo_diabetes = models.IntegerField(verbose_name = "Tiempo DM")
    dislipemia = models.CharField(verbose_name = "Displipemia", choices = _SI_NO_INDET, max_length = 2)
    tabaco = models.CharField(verbose_name = "Tabaco", choices = _TABACO, max_length = 2)
    tabaco_paquetes_acumulados = models.IntegerField(verbose_name = "Paquetes/año acumulados")
    alcohol = models.CharField(verbose_name = "Alcohol", choices = _ALCOHOL, max_length = 2)
    ejercicio = models.CharField(verbose_name = "Ejercico físico", choices = _EJERCICIO, max_length = 2)
    cardiopatia_isquemica = models.CharField(verbose_name = "Cardiopatía isquémica crónica", choices = _SI_NO_INDET, max_length = 2)
    IAM = models.CharField(verbose_name = "Infarto agudo de miocardio", choices = _SI_NO_INDET, max_length  = 2)
    otras_cardiopatias = models.CharField(verbose_name = "Otras cardiopatías", choices = _CARDIOPATIA, max_length = 2)
    arritmia_previa  = models.CharField(verbose_name="Arritmia previa", choices = _SI_NO_INDET, max_length = 2)
    fap_previa = models.CharField(verbose_name="FAP previa", choices = _SI_NO_INDET, max_length = 2)
    ACFA_previa  = models.CharField(verbose_name="ACFA previa", choices = _SI_NO_INDET, max_length = 2)
    arteriopatia_perif_previa = models.CharField(verbose_name="Arteriopatía periférica previa", choices = _SI_NO_INDET, max_length = 2)
    TVP  = models.CharField(verbose_name="Trombosis venosa profunda", choices = _SI_NO_INDET, max_length = 2)
    migrana = models.CharField(verbose_name="Migraña", choices = _SI_NO_INDET, max_length = 2)
    SAOS = models.CharField(verbose_name="Síndrome apnea obstructiva sueño", choices = _SI_NO_INDET, max_length = 2)
    deterioro_cognitivo = models.CharField(verbose_name="Deterioro cognitivo", choices = _SI_NO_INDET, max_length = 2)
    cancer = models.CharField(verbose_name="Cancer activo", choices = _SI_NO_INDET, max_length = 2)
    cancer_tipo = models.TextField(verbose_name = "Tipo de cancer", max_length = 500)
    anticoagulacion_previa  = models.CharField(verbose_name="Anticoagulación previa", choices = _SI_NO_INDET, max_length = 2)
    antiagregacion_previa = models.CharField(verbose_name="Antiagregación previa", choices = _SI_NO_INDET, max_length = 2)
    estatina_previas = models.CharField(verbose_name="Estatina previa", choices = _SI_NO_INDET, max_length = 2)
    otras_patologias = models.TextField(verbose_name = "Otras patologías", max_length = 500, blank = True)
    antecedentes_familiares = models.BooleanField(verbose_name = "Antecedentes familiares")
    rankin = models.CharField(verbose_name="Escala de Rankin", choices= _RANKIN, max_length = 2)


class Intervencion(models.Model):
    class Meta:
        verbose_name_plural = "Intervenciones"

    episodio = models.ForeignKey('Episodio')
    anticoag_nombre = models.CharField(max_length=300)


_TICI = (
        ("0", "No perfusión"),
        ("1", "Penetración con mínima perfusión"),
        ("2", "Perfusión parcial"),
        ("2A", "Relleno parcial"),
        ("2B", "Relleno completo"),
        ("3", "Perfusión completa")
        )

class Extraccion(models.Model):

    class Meta:
        verbose_name_plural = "Extracciones"

    episodio = models.ForeignKey('Episodio', null = True)
    puncion = models.DateTimeField(verbose_name = "Punción arterial", default = timezone.now)
    micro = models.DateTimeField(verbose_name = "Introcucción de microcateter", default = timezone.now)
    rescate = models.DateTimeField(verbose_name = "Hora del rescate", default = timezone.now)
    urokinasa = models.CharField(verbose_name = "Urokinasa", choices = _SI_NO_INDET, max_length = 2)
    recanaliza_ia = models.BooleanField(verbose_name = "Recanalización después de IA", default = False)
    tici = models.CharField(verbose_name = "TICI", choices = _TICI, max_length = 2)
    oktici = models.CharField(verbose_name = "OKTICI", choices = _SI_NO_INDET, max_length = 2)
    trombo = models.CharField( verbose_name = "Extracción de trombo", choices = _SI_NO_INDET, max_length = 2)
    hora_ext = models.DateTimeField( verbose_name = "Hora de extracción", default = timezone.now)
    peso_trombo = models.PositiveIntegerField (verbose_name="Peso (mg)")
    aspecto_trombo =models.TextField( verbose_name = "Aspecto del trombo", max_length = 500, blank = True)
    anatomia_patologica = models.TextField (verbose_name = "Anatomía patológica", max_length = 500, blank = True)
    incidencias = models.TextField (verbose_name = "Incidencias", max_length = 500, blank = True)
    otras  =models.TextField( verbose_name = "Otras", max_length = 500, blank=True)


_TRATAMIENTOS = (
        ("ANTICOAG_sintrom", "ANTICOAG Sintrom"),
        ("ANTICOAG_apixaban", "ANTICOAG Apixaban"),
        ("ANTICOAG_rivaroxaban", "ANTICOAG Rivaroxaban"),
        ("ANTICOAG_dabigatran", "ANTICOAG Dabigatran"),
        ("ANTIAGREG_adiro", "ANTIAGREG Adiro"),
        ("ANTIAGREG_clopidogrel", "ANTIAGREG Clopidogrel"),
        ("ESTATINAS", "ESTATINAS"),
        ("ASPIRINA", "ASPIRINA")
        )

class Tratamiento(models.Model):
        episodio = models.ForeignKey('Episodio')
        medicamento = models.CharField(verbose_name = "Medicamento", choices = _TRATAMIENTOS, max_length = 30)
        dosis = models.PositiveIntegerField(verbose_name = "Dosis (mg)")

class Seguimiento(models.Model):
        episodio = models.ForeignKey('Episodio')
        variable_seguimiento = models.CharField(max_length = 30, verbose_name="Placeholder variable seg")
        ##variables#, blank = True#
