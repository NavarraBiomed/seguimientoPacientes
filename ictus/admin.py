from django.contrib import admin
from .models import *

from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

class BasalInLine(admin.StackedInline):
    model = Basal
    extra = 0

class EpisodioInLine(admin.StackedInline):
    model = Episodio
    extra = 0
    show_change_link = True

    #fields = ("h_inicio", 'tipo')
    #readonly_fields = ('tipo_ictus',)

class IntervencionInLine(admin.StackedInline):
    model = Intervencion
    extra = 0
    show_change_link = True

class IntraarterialInLine(admin.StackedInline):
    model = Intraarterial
    extra = 0


class SeguimientoInLine(admin.StackedInline):
    model = Seguimiento
    extra = 0

class EpisodioAdmin(admin.ModelAdmin):
    inlines = [BasalInLine, IntervencionInLine, IntraarterialInLine, SeguimientoInLine]

class PacienteAdmin(admin.ModelAdmin):
    inlines = [EpisodioInLine,]

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Episodio, EpisodioAdmin)
admin.site.register(Basal)
admin.site.register(Intraarterial)
