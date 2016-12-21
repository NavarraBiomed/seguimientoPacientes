from django.db import models
from django.utils import timezone
import locale

_SEXO = (
	(0, "Hombre"),
	(1, "Mujer")
	)

_TIPO = (
	("00", "Tipo 1"),
	("01", "Tipo 2")
	)

_NO_SI = (
        (0, "No"),
        (1, "Sí"),
        )


_ETNIA = (
        ("0", "Caucásico mediterráneo"),
        ("1", "Otro caucásico"),
        ("2", "Latinoamericano-caribeño"),
        ("3", "Asiático"),
        ("4", "Negro o afro-americano"),
        ("5", "Otra raza"),
        ("6", "No determinado")
        )

_DIABETES = (
        ("01", "Tipo 1"),
        ("02", "Tipo 2"),
        ("03", "Desconocido")
        )

_TABACO = (
        (0, "No fumador"),
        (1, "Exfumador"),
        (2, "Fumador pasivo"),
        (3, "Fumador actual"),
        (4, "Desconocido")
        )

_ALCOHOL = (
        (0, "No"),
        (1, "A diario"),
        (2, "Ocasionalmente"),
        (3, "Exhabito enólico")
        )


_RANKIN = (
        (0, "0-Sin síntomas"),
        (1, "1-Sin incapacidad importante"),
        (2, "2-Incapacidad leve"),
        (3, "3-Incapacidad moderada"),
        (4, "4-Incapacidad moderadamente grave"),
        (5, "5-Incapacidad grave"),
        (6, "6-Muerte")
        )


_TOAST = (
        (0, "Aterotrombótico"),
        (1, "Cardioembólico"),
        (2, "Lacunar"),
        (3, "De otra etiología determinada/causa infrecuente"),
        (4, "Indeterminado, >2 causas"),
        (5, "Indeterminado, tras estudio completo"),
        (6, "Indeterminado, estudio incompleto")
        )

_OXFORDSHIRE = (
        (0, "Infartos completos de la circulación anterior"),
        (1, "Infartos parciales de la circulación anterior"),
        (2, "Infartos lacunares"),
        (3, "infartos de la circulación posterior")
        )

_ESCALA_AIT = tuple(zip (range(0,8), range(0,8)))

_TOAST_INDET =(
        (0, 'Criptogenico'),
        (1, 'Incompleto'),
        (2, 'Coexistencia')

    )



_NIHSS = tuple(zip (list(range(0,31)), list(range(0,31))))
_NIHSS_ALTA = tuple(zip(list(range(0,31)), list(range(0,31)) ))
_MRS = tuple(zip (list(range(0,7)), list( range(0,7))))

class Paciente(models.Model):
    nhc = models.IntegerField(verbose_name="NHC")
    iniciales = models.CharField(verbose_name = "Iniciales del paciente", max_length = 6)
    fechanacim = models.DateField(verbose_name = "Fecha de nacimiento", blank=True, null=True)
    sexo = models.IntegerField(verbose_name = "Sexo", choices = _SEXO)
    grupoetnico = models.IntegerField(verbose_name = "Grupo étnico", choices = _ETNIA, blank=True, null=True)

    def is_complete(self):
        incomplete_cases = len(self.episodios.filter(completo=False))
        return incomplete_cases == 0


    def __str__(self):
        return str(self.nhc)


class Episodio(models.Model):
        paciente = models.ForeignKey('Paciente', related_name="episodios")
        idmuestra = models.CharField(verbose_name="ID Muestra", max_length=16)
        idtrombo = models.CharField(verbose_name="ID Trombo", max_length=16, blank=True, null=True)

        completo = models.BooleanField( verbose_name = "Completo", default = False, blank=True)
        lesion = models.BooleanField( verbose_name = "Lesión", default = False, blank=True)

        fechaictus = models.DateField(verbose_name = "Fecha ictus",default = timezone.now, blank=True, null=True)
        h_inicio = models.TimeField(verbose_name = "Hora de inicio", default = timezone.now, blank=True, null=True)
        h_inicioindet = models.BooleanField( verbose_name = "Hora indeterminada", default = False, blank=True)
        nihssb = models.IntegerField( verbose_name = "NIHSS Ingreso", choices = _NIHSS, blank=True, null=True)
        nihssalta = models.IntegerField( verbose_name = "NIHSS Alta", choices = _NIHSS_ALTA, blank=True, null=True)
        rankinalta = models.IntegerField( verbose_name = "mRS alta", choices = _MRS, blank=True, null=True)
        toast = models.IntegerField( verbose_name = "TOAST", choices = _TOAST, blank=True, null=True)
        toastindet = models.IntegerField( verbose_name="TOAST Indeterminado", choices=_TOAST_INDET, blank=True, null=True)
        mimic = models.IntegerField(verbose_name = "AIT o Ictus Mimic", choices = _NO_SI, blank=True, null=True)
        oxfordshire = models.IntegerField(verbose_name ="OXFORDSHIRE", choices = _OXFORDSHIRE, blank=True, null=True)
        ait = models.IntegerField(verbose_name = "AIT", choices = _NO_SI, blank=True, null=True)
        aitprevio = models.IntegerField(verbose_name = "AIT previo", choices = _NO_SI, blank=True, null=True)
        aitdurac = models.IntegerField(verbose_name = "Duración AIT (min)", blank=True, null=True)
        aitneuroimagen = models.IntegerField(verbose_name = "Neuroimagen AIT", choices = _NO_SI, blank=True, null=True)
        abcd2 = models.IntegerField(verbose_name = "ABCD2", choices = _ESCALA_AIT, blank=True, null=True)
        abcd3 = models.IntegerField(verbose_name = "ABCD3", choices = _ESCALA_AIT, blank=True, null=True)
        ev = models.IntegerField(verbose_name = "EV", choices = _NO_SI, blank=True, null=True)
        recanalizacdtc = models.IntegerField(verbose_name = "Recanalización doppler transcraneal", choices = _NO_SI, blank=True, null=True)
        ia = models.IntegerField(verbose_name = "Tratamiento intraarterial", choices = _NO_SI, blank=True, null=True)
        aspect_basal = models.FloatField(verbose_name="Puntuacion ASPECTS BASAL", blank=True, null=True)
        acm_hiperdensa = models.IntegerField(verbose_name = "ACM hiperdensa", choices = _NO_SI, blank=True, null=True)
        esus = models.IntegerField(verbose_name = "ESUS", choices = _NO_SI, blank=True, null=True)
        clasifsen = models.IntegerField( verbose_name = "SEN", choices = _TOAST, blank=True, null=True)

        comentarios = models.TextField(verbose_name="Comentarios", max_length=1024, blank=True, null=True)

        def __str__(self):
            locale.setlocale(locale.LC_TIME, '')
            if self.idmuestra == self.idtrombo or self.idtrombo=="" or self.idtrombo==None:
                return self.idmuestra
            else:
                return self.idmuestra + " ("+ self.idtrombo +" )"
        ###elf.paciente.nombre + " - "+self.tipo_ictus+" ("+str(self.h_default = timezone.nowinicio)+")"

        def description(self):
            locale.setlocale(locale.LC_TIME, '')
            return str(self)+ " - " + self.fechaictus.strftime("%d de %B, %Y")


_TIPO_CARDIOPATIA = (
    (0, "Cardiopatía isquémica"),
    (1, "Cardiopatía valvular"),
    (2, "Otras"),
    (3, "Mixta")

)


class Basal(models.Model):
    class Meta:
        verbose_name_plural = "Basales"

    episodio = models.ForeignKey('Episodio')

    edad = models.IntegerField(verbose_name="Edad", blank=True, null=True)
    ictusaitprevio = models.IntegerField(verbose_name ="Ictus previo", choices = _NO_SI, blank=True, null=True)
    chadsvasc = models.FloatField(verbose_name="CHADSVASC", blank=True, null=True)
    hta = models.IntegerField(verbose_name = "Hipertensión", choices = _NO_SI, blank=True, null=True)
    dm = models.IntegerField(verbose_name = "Diabetes mellitus", choices = _NO_SI, blank=True, null=True)
    dl = models.IntegerField(verbose_name = "Displipemia", choices = _NO_SI, blank=True, null=True)
    tabaquismo = models.IntegerField(verbose_name = "Tabaco", choices = _TABACO, blank=True, null=True)
    alcohol = models.IntegerField(verbose_name = "Alcohol", choices = _ALCOHOL, blank=True, null=True)
    fa = models.IntegerField(verbose_name="FAP previa", choices = _NO_SI, blank=True, null=True)
    cardiopatia = models.IntegerField( verbose_name = "Cardiopatía", choices = _NO_SI, blank=True, null=True)
    tipo_cardiopatia = models.IntegerField(verbose_name="Tipo de cardiopatía", choices=_TIPO_CARDIOPATIA, blank=True, null=True)
    arteriopatia_perif = models.IntegerField(verbose_name="Arteriopatía periférica previa", choices = _NO_SI, blank=True, null=True)
    cancer = models.IntegerField(verbose_name="Cancer activo", choices = _NO_SI, blank=True, null=True)
    anticoagulante  = models.IntegerField(verbose_name="Anticoagulación previa", choices = _NO_SI, blank=True, null=True)
    anticoagnombre = models.CharField(max_length=300, blank=True, null=True)
    antiagregante = models.IntegerField(verbose_name="Antiagregación previa", choices = _NO_SI, blank=True, null=True)
    estatinas = models.IntegerField(verbose_name="Estatina previa", choices = _NO_SI, blank=True, null=True)
    rankinbasal = models.IntegerField(verbose_name="Escala de Rankin", choices= _RANKIN, blank=True, null=True)
    toast_ictusprev = models.IntegerField( verbose_name = "TOAST ictus previo", choices = _TOAST, blank=True, null=True)
    cancerdxposterior = models.IntegerField( verbose_name = "Cancer diagnosticado tras el ictus", choices = _NO_SI, null=True)


_ECOTSA = (
    (0,'Normal'),
    (1,'Ateromatosis carotidea sin estenosis'),
    (2,'estenosis < 50%'),
    (3,'estenosis  moderada 51 - 69 %'),
    (4,'estenosis severa o critica (70-90 %)'),
    (5,'estenosis critica (>90 %)'),
    (6,'oclusion o estenosis suboclusiva'),
)

_TICI = (
        ("0", "No perfusión"),
        ("1", "Penetración con mínima perfusión"),
        ("2", "Perfusión parcial"),
        ("2A", "Relleno parcial"),
        ("2B", "Relleno completo"),
        ("3", "Perfusión completa")
        )

class Intervencion(models.Model):
    class Meta:
        verbose_name_plural = "Intervenciones"

    episodio = models.ForeignKey('Episodio')

    recanalizacdtc =models.IntegerField(verbose_name="Recanalizacion durante rtpa", choices=_NO_SI, blank=True, null=True)
    iniciovena = models.FloatField(verbose_name="Tiempo inicio vena", blank=True, null=True)
    mejoriaNIHSS4ev = models.IntegerField(verbose_name="EV -Mejoria de 4 puntos o mas en la escala nihss", choices=_NO_SI, blank=True, null=True)
    mejoriaNIHSS4ia = models.IntegerField(verbose_name="IA - Mejoria de 4 puntos o mas en la escala nihss", choices=_NO_SI, blank=True, null=True)
    deterioro = models.IntegerField(verbose_name="Deterioro", choices=_NO_SI, blank=True, null=True)
    fluctuacion = models.IntegerField(verbose_name="Fluctuación", choices=_NO_SI, blank=True, null=True)
    transf_hemor = models.IntegerField(verbose_name="Transformación hemorrágica", choices=_NO_SI, blank=True, null=True)
    dimerod = models.FloatField(verbose_name="Dimero D", blank=True, null=True)
    monit_ui = models.CharField(verbose_name="Hallazgos monitorización UI", max_length=3000, blank=True, null=True)
    monituifa = models.IntegerField(verbose_name="DETECCION FA O FAP EN MONITORIZACION UI", choices=_NO_SI, blank=True, null=True)
    holter = models.IntegerField(verbose_name="Holter", choices=_NO_SI, blank=True, null=True)
    holterfecha = models.DateField(verbose_name = "Fecha de Holter", blank=True, null=True)
    holterhallazgos = models.CharField(verbose_name="Hallazgos monitorización FA", max_length=3000, blank=True, null=True)
    holter_fa = models.IntegerField(verbose_name="Rachas de FA o FAP  en Holter", choices=_NO_SI, blank=True, null=True)
    ecocardiohecho = models.IntegerField(verbose_name="Ecocardio realizado", choices=_NO_SI, blank=True, null=True)
    ecocardiofecha = models.DateField(verbose_name = "Fecha de ecocardio", blank=True, null=True)
    ecocardiohallazgos = models.CharField(verbose_name="Hallazgos ecocardio", max_length=3000, blank=True, null=True)
    ecocardiocardieombolico = models.IntegerField(verbose_name="Ecocardio cardioembólico", choices=_NO_SI, blank=True, null=True)
    ecodilatacionai = models.IntegerField(verbose_name="Dilatación auricular izquierda", choices=_NO_SI, blank=True, null=True)
    ecotsaipsi = models.IntegerField(verbose_name="Hallazgos ECOTSA ipsilateral", choices=_ECOTSA, blank=True, null=True)
    ecotsacontra = models.IntegerField(verbose_name="Hallazgos ECOTSA contralateral", choices=_ECOTSA, blank=True, null=True)
    ecotsa50ipsi = models.IntegerField(verbose_name="ECOTSA>50% ipsilatearl", choices=_NO_SI, blank=True, null=True)
    duplex_dtcipsilateral = models.IntegerField(verbose_name="ESTENOSIS SIGNFICATIVAipsilateral (Vps >155 cm/s)", choices=_NO_SI, blank=True, null=True)
    duplex_dtcotro = models.IntegerField(verbose_name="ESTENOSIS significativa a cualquier otro nivel (vPS >155 CM/S)", choices=_NO_SI, blank=True, null=True)
    aterovb = models.IntegerField(verbose_name="Esteniosis VB significativa sintomática (ipsilateral al lado sintomático)", choices=_NO_SI, blank=True, null=True)



class Intraarterial(models.Model):

    class Meta:
        verbose_name_plural = "Intraarterial"

    episodio = models.ForeignKey('Episodio', null = True)

    #CAMBIAR VALORES
    tici = models.CharField(verbose_name = "TICI", choices = _TICI, max_length = 2, blank=True, null=True)
    iniciomicro = models.FloatField(verbose_name="Tiempo inicio micro", blank=True, null=True)


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


_NIHSS_3M = tuple(zip (range(0,31), range(0,31)))

class Seguimiento(models.Model):
        episodio = models.ForeignKey('Episodio')
        nihss3m =  models.IntegerField( verbose_name = "NIHSS 3 meses", choices = _NIHSS_3M, blank=True, null=True)
        toast3m = models.IntegerField( verbose_name = "TOAST 3 meses", choices = _TOAST, blank=True, null=True)
        rankin3m = models.IntegerField(verbose_name="Escala de Rankin 3 meses", choices= _RANKIN, blank=True, null=True)
        causamuerte  = models.TextField( verbose_name = "Causa de la muerte", max_length = 3000, blank=True, null=True)
        muertevascular = models.IntegerField( verbose_name = "Muerte de causa vascular", choices = _NO_SI, blank=True, null=True)
        fechamuerte = models.DateField(verbose_name = "Fecha de la muerte", blank=True, null=True)
        fop = models.IntegerField( verbose_name = "Presencia de foramen oval permeable", choices = _NO_SI, blank=True, null=True)
        rope = models.FloatField( verbose_name="Escala RoPE para pacientes con FOP", blank=True, null=True)
        recurrencia =  models.IntegerField( verbose_name = "Recurrencia", choices = _NO_SI, blank=True, null=True)
        recurrenciafecha = models.DateField(verbose_name = "Fecha de la recurrencia", blank=True, null=True)
        recurrenciatoast = models.IntegerField( verbose_name = "TOAST recurrencia", choices = _TOAST, blank=True, null=True)
        recurrenciavasc = models.IntegerField( verbose_name = "Recurrencia vascular", choices = _NO_SI, blank=True, null=True)
        recurrenciavascfecha = models.DateField(verbose_name = "Fecha de la recurrencia vascular", blank=True, null=True)
