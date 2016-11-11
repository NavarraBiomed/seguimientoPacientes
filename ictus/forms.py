from django import forms
from material import *
from .models import *
import ictus
from django.views.generic import *
from django.views.generic.edit import FormView


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        exclude = ()

    layout = Layout(
            Row('NHC', 'nombre', 'iniciales'),
            Row('fecha_nacimiento', 'genero', 'grupo_etnico'),

            )


class EpisodeForm(forms.ModelForm):

    class Meta:
        model = Episodio
        exclude = ('paciente',)

    layout = Layout(
        Row("fecha_inicio", "h_inicio", "hora_inicio_indet"),
        Row("tipo_ictus"),
        Row("nihss_ingreso", "nihss_alta", "mrs_alta"),
        Row("toast", "oxfordshire"),
        Row("ait", "ait_duracion", "ait_neuroimagen", "ait_bcd2"),
        Row("hemo_localizacion", "hemo_etiologia"),
        Row("ev", "recanalizacion_dtc"),
        Row("oclusion", "oclusion_lugar"),
        Row("tibidtc", "tratamiento_interarterial")

    )
