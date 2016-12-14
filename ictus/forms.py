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
            Row('nhc', 'iniciales'),
            Row('fechanacim', 'sexo', 'grupoetnico'),

            )


class EpisodeForm(forms.ModelForm):

    class Meta:
        model = Episodio
        exclude = ('paciente',)

    layout = Layout(
        Row('idmuestra', 'idtrombo'),
        Row("completo", "lesion"),
        Row("fechaictus", "h_inicio", "h_inicioindet"),
        Row("nihssb", "nihssalta", "rankinalta"),
        Row("toast", "toastindet"),
        Row("mimic", "oxfordshire"),
        Row("ait", "aitprevio", "aitdurac", "aitneuroimagen"),
        Row("abcd2", "abcd3"),
        Row("ev", "recanalizacdtc"),
        Row("ia", "aspect_basal"),
        Row("acm_hiperdensa", "esus", "clasifsen"),
        Row("comentarios")

    )
