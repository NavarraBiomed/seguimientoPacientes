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

_NO_SI = (
        ("00", "No"),
        ("01", "Sí"),
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
    grupo_etnico = models.CharField(verbose_name = "Grupo étnico", choices = _ETNIA, max_length = 2, blank=True, null=True)

    def is_complete(self):
        incomplete_cases = len(self.episodio_set.filter(completo=False))
        return incomplete_cases == 0


    def __str__(self):
        return str(self.NHC)

class Episodio(models.Model):
        paciente = models.ForeignKey('Paciente')
        completo = models.BooleanField( verbose_name = "Completo", default = False, blank=True)
        lesion = models.BooleanField( verbose_name = "Lesión", default = False, blank=True)

        fecha_inicio = models.DateField(verbose_name = "Fecha ictus",default = timezone.now, blank=True, null=True)
        h_inicio = models.TimeField(verbose_name = "Hora de inicio", default = timezone.now, blank=True, null=True)
        hora_inicio_indet = models.BooleanField( verbose_name = "Hora indeterminada", default = False, blank=True)
        tipo_ictus = models.CharField( verbose_name = "Tipo de ictus", choices = _TIPO_ICTUS, max_length = 2)
        nihss_ingreso = models.IntegerField( verbose_name = "NIHSS Ingreso", choices = _NIHSS, blank=True, null=True)
        nihss_alta = models.IntegerField( verbose_name = "NIHSS Alta", choices = _NIHSS_ALTA, blank=True, null=True)
        mrs_alta = models.IntegerField( verbose_name = "mRS alta", choices = _MRS, blank=True, null=True)
        toast = models.CharField( verbose_name = "TOAST", choices = _TOAST, max_length = 2, blank=True, null=True)
        oxfordshire = models.CharField(verbose_name ="OXFORDSHIRE", choices = _OXFORDSHIRE, max_length = 4, blank=True, null=True)
        ait = models.CharField(verbose_name = "AIT", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
        ait_previo = models.CharField(verbose_name = "AIT", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
        ait_duracion = models.TimeField(verbose_name = "Duración AIT", default = timezone.now, blank=True, null=True)
        ait_neuroimagen = models.CharField(verbose_name = "Neuroimagen AIT", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
        ait_bcd2 = models.IntegerField(verbose_name = "ABCD2", choices = _ESCALA_AIT, blank=True, null=True)
        ait_bcd3 = models.IntegerField(verbose_name = "ABCD3", choices = _ESCALA_AIT, blank=True, null=True)
        hemo_localizacion = models.CharField(verbose_name ="HEMO localización", choices = _HEMO_TIPO, max_length = 2, blank=True, null=True)
        hemo_etiologia = models.CharField(verbose_name = "HEMO etiología", choices = _HEMO_ETIOLOGIA, max_length = 2, blank=True, null=True)
        ev = models.CharField(verbose_name = "EV", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
        recanalizacion_dtc = models.CharField(verbose_name = "Recanalización doble transcraneal", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
        oclusion = models.CharField(verbose_name = "Oclusión", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
        oclusion_lugar = models.CharField( verbose_name = "Lugar de oclusión", choices = _OCLUSION, max_length = 2, blank=True, null=True)
        tibidtc = models.IntegerField(verbose_name = "TIBI/DTC", choices = _TIBIDTC, blank=True, null=True)
        tratamiento_interarterial = models.CharField(verbose_name = "Tratamiento Interarterial", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)

        aspect_basal = models.FloatField(verbose_name="Puntuacion ASPECTS BASAL", blank=True, null=True)
        acm_hiperdensa = models.CharField(verbose_name = "ACM hiperdensa", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
        esus = models.CharField(verbose_name = "ESUS", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
        clasif_sen = models.CharField( verbose_name = "SEN", choices = _TOAST, max_length = 2, blank=True, null=True)

        comentarios = models.TextField(verbose_name="Comentarios", max_length=1024, blank=True, null=True)

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
    ictus_previo = models.CharField(verbose_name ="Ictus previo", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    chadsvasc = models.FloatField(verbose_name="CHADSVASC", blank=True, null=True)
    HTA = models.CharField(verbose_name = "Hipertensión", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    HTA_tiempo = models.IntegerField(verbose_name = "Tiempo evolucón HTA", blank=True, null=True)
    diabetes = models.CharField(verbose_name = "Diabetes mellitus", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    tipo_diabetes = models.CharField (verbose_name = "Tipo de DM", choices = _DIABETES, max_length = 2, blank=True, null=True)
    tiempo_diabetes = models.IntegerField(verbose_name = "Tiempo DM", blank=True, null=True)
    dislipemia = models.CharField(verbose_name = "Displipemia", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    tabaco = models.CharField(verbose_name = "Tabaco", choices = _TABACO, max_length = 2, blank=True, null=True)
    tabaco_paquetes_acumulados = models.IntegerField(verbose_name = "Paquetes/año acumulados", blank=True, null=True)
    alcohol = models.CharField(verbose_name = "Alcohol", choices = _ALCOHOL, max_length = 2, blank=True, null=True)
    ejercicio = models.CharField(verbose_name = "Ejercico físico", choices = _EJERCICIO, max_length = 2, blank=True, null=True)
    cardiopatia_isquemica = models.CharField(verbose_name = "Cardiopatía isquémica crónica", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    IAM = models.CharField(verbose_name = "Infarto agudo de miocardio", choices = _SI_NO_INDET, max_length  = 2, blank=True, null=True)
    otras_cardiopatias = models.CharField(verbose_name = "Otras cardiopatías", choices = _CARDIOPATIA, max_length = 2, blank=True, null=True)
    arritmia_previa  = models.CharField(verbose_name="Arritmia previa", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    fap_previa = models.CharField(verbose_name="FAP previa", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    ACFA_previa  = models.CharField(verbose_name="ACFA previa", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    arteriopatia_perif_previa = models.CharField(verbose_name="Arteriopatía periférica previa", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    TVP  = models.CharField(verbose_name="Trombosis venosa profunda", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    migrana = models.CharField(verbose_name="Migraña", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    SAOS = models.CharField(verbose_name="Síndrome apnea obstructiva sueño", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    deterioro_cognitivo = models.CharField(verbose_name="Deterioro cognitivo", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    cancer = models.CharField(verbose_name="Cancer activo", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    cancer_tipo = models.TextField(verbose_name = "Tipo de cancer", max_length = 500, blank=True, null=True)
    anticoagulacion_previa  = models.CharField(verbose_name="Anticoagulación previa", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    antiagregacion_previa = models.CharField(verbose_name="Antiagregación previa", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    estatina_previas = models.CharField(verbose_name="Estatina previa", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    otras_patologias = models.TextField(verbose_name = "Otras patologías", max_length = 500, blank=True, null=True)
    antecedentes_familiares = models.BooleanField(verbose_name = "Antecedentes familiares", blank=True, default=False)
    rankin = models.CharField(verbose_name="Escala de Rankin", choices= _RANKIN, max_length = 2, blank=True, null=True)
    toast_ictus_previo = models.CharField( verbose_name = "TOAST ictus previo", choices = _TOAST, max_length = 2, blank=True, null=True)



_ECOTSA = (
    (0,'Normal'),
    (1,'Ateromatosis carotidea sin estenosis'),
    (2,'estenosis < 50%'),
    (3,'estenosis  moderada 51 - 69 %'),
    (4,'estenosis severa o critica (70-90 %)'),
    (5,'estenosis critica (>90 %)'),
    (6,'oclusion o estenosis suboclusiva'),
)

class Intervencion(models.Model):
    class Meta:
        verbose_name_plural = "Intervenciones"

    episodio = models.ForeignKey('Episodio')
    anticoag_nombre = models.CharField(max_length=300, blank=True, null=True)
    reacanalizacdtc = models.IntegerField(verbose_name="Recanalizacion durante rtpa",choices=_NO_SI, blank=True, null=True)
    iniciovena = models.FloatField(verbose_name="Tiempo inicio vena", blank=True, null=True)
    mejoriaNIHSS4ev = models.IntegerField(verbose_name="ev -Mejoria de 4 puntos o mas en la escala nihss", choices=_NO_SI, blank=True, null=True)
    iniciomicro = models.FloatField(verbose_name="Tiempo inicio micro", blank=True, null=True)
    mejoriaNIHSS4ia = models.IntegerField(verbose_name="ia - Mejoria de 4 puntos o mas en la escala nihss", choices=_NO_SI, blank=True, null=True)

    deterioro = models.IntegerField(verbose_name="Deterioro", choices=_NO_SI, blank=True, null=True)
    fluctuacion = models.IntegerField(verbose_name="Fluctuación", choices=_NO_SI, blank=True, null=True)
    transf_hemor = models.IntegerField(verbose_name="Transformación hemorrágica", choices=_NO_SI, blank=True, null=True)
    dimerod = models.FloatField(verbose_name="Dimero D", blank=True, null=True)
    monit_ui = models.CharField(verbose_name="Hallazgos monitorización UI", max_length=3000, blank=True, null=True)
    monituifa = models.IntegerField(verbose_name="DETECCION FA O FAP EN MONITORIZACION UI", choices=_NO_SI, blank=True, null=True)
    holter = models.IntegerField(verbose_name="Holter", choices=_NO_SI, blank=True, null=True)
    holter_fecha = models.DateField(verbose_name = "Fecha de Holter", blank=True, null=True)
    holter_hallazgos = models.CharField(verbose_name="Hallazgos monitorización FA", max_length=3000, blank=True, null=True)
    holter_fa = models.IntegerField(verbose_name="Rachas de FA o FAP  en Holter", choices=_NO_SI, blank=True, null=True)
    ecocardio_hecho = models.IntegerField(verbose_name="Ecocardio realizado", choices=_NO_SI, blank=True, null=True)
    ecocardio_fecha = models.DateField(verbose_name = "Fecha de ecocardio", blank=True, null=True)
    ecocardio_hallazgos = models.CharField(verbose_name="Hallazgos ecocardio", max_length=3000, blank=True, null=True)
    ecocardio_cardioembolico = models.IntegerField(verbose_name="Ecocardio cardioembólico", choices=_NO_SI, blank=True, null=True)
    ecodilatacion_ai = models.IntegerField(verbose_name="Dilatación auricular izquierda", choices=_NO_SI, blank=True, null=True)
    ecotsa_ipsi = models.IntegerField(verbose_name="Hallazgos ECOTSA ipsilateral", choices=_ECOTSA, blank=True, null=True)
    ecotsa_contra = models.IntegerField(verbose_name="Hallazgos ECOTSA contralateral", choices=_ECOTSA, blank=True, null=True)
    ecosta_50_ipsi = models.IntegerField(verbose_name="ECOTSA>50% ipsilatearl", choices=_NO_SI, blank=True, null=True)
    duplex_dtc_ipsilateral = models.IntegerField(verbose_name="ESTENOSIS SIGNFICATIVAipsilateral (Vps >155 cm/s)", choices=_NO_SI, blank=True, null=True)
    duplex_dtc_otro = models.IntegerField(verbose_name="ESTENOSIS significativa a cualquier otro nivel (vPS >155 CM/S)", choices=_NO_SI, blank=True, null=True)
    aterovb = models.IntegerField(verbose_name="Esteniosis VB significativa sintomática (ipsilateral al lado sintomático)", choices=_NO_SI, blank=True, null=True)

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
    puncion = models.DateTimeField(verbose_name = "Punción arterial", default = timezone.now, blank=True, null=True)
    micro = models.DateTimeField(verbose_name = "Introcucción de microcateter", default = timezone.now, blank=True, null=True)
    rescate = models.DateTimeField(verbose_name = "Hora del rescate", default = timezone.now, blank=True, null=True)
    urokinasa = models.CharField(verbose_name = "Urokinasa", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    recanaliza_ia = models.BooleanField(verbose_name = "Recanalización después de IA", default = False, blank=True)
    tici = models.CharField(verbose_name = "TICI", choices = _TICI, max_length = 2, blank=True, null=True)
    oktici = models.CharField(verbose_name = "OKTICI", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    trombo = models.CharField( verbose_name = "Extracción de trombo", choices = _SI_NO_INDET, max_length = 2, blank=True, null=True)
    hora_ext = models.DateTimeField( verbose_name = "Hora de extracción", default = timezone.now, blank=True, null=True)
    peso_trombo = models.PositiveIntegerField (verbose_name="Peso (mg)", blank=True, null=True)
    aspecto_trombo =models.TextField( verbose_name = "Aspecto del trombo", max_length = 500, blank = True, null=True)
    anatomia_patologica = models.TextField (verbose_name = "Anatomía patológica", max_length = 500, blank = True, null=True)
    incidencias = models.TextField (verbose_name = "Incidencias", max_length = 500, blank = True, null=True)
    otras  =models.TextField( verbose_name = "Otras", max_length = 500, blank=True, null=True)


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

_NIHSS_3M = zip (list(range(0,31)), list(range(0,31)))

class Seguimiento(models.Model):
        episodio = models.ForeignKey('Episodio')
        nihss_3meses =  models.IntegerField( verbose_name = "NIHSS 3 meses", choices = _NIHSS_3M, blank=True, null=True)
        toast_3meses = models.CharField( verbose_name = "TOAST 3 meses", choices = _TOAST, max_length = 2, blank=True, null=True)
        rankin_3meses = models.CharField(verbose_name="Escala de Rankin 3 meses", choices= _RANKIN, max_length = 2, blank=True, null=True)
        causa_muerte  = models.TextField( verbose_name = "Causa de la muerte", max_length = 3000, blank=True, null=True)
        muertevascular = models.CharField( verbose_name = "Muerte de causa vascular", choices = _NO_SI, max_length = 2, blank=True, null=True)
        fecha_muerte = models.DateField(verbose_name = "Fecha de la muerte", blank=True, null=True)
        fop = models.CharField( verbose_name = "Presencia de foramen oval permeable", choices = _NO_SI, max_length = 2, blank=True, null=True)
        rope = models.FloatField( verbose_name="Escala RoPE para pacientes con FOP", blank=True, null=True)
