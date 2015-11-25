from django.contrib import admin
from .models import Paciente, Episodio, Basal, Intervencion, Extraccion, Tratamiento, Seguimiento

from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

class BasalInLine(admin.TabularInline):
    model = Basal
    extra = 0

class EpisodioInLine(admin.TabularInline):
    model = Episodio
    extra = 0
    show_change_link = True

    #fields = ("h_inicio", 'tipo')
    readonly_fields = ('tipo',)

class IntervencionInLine(admin.TabularInline):
    model = Intervencion
    extra = 0
    show_change_link = True

class ExtraccionInLine(admin.TabularInline):
    model = Extraccion
    extra = 0
    
class TratamientoInLine(admin.TabularInline):
    model = Tratamiento
    extra = 0

class SeguimientoInLine(admin.TabularInline):
    model = Seguimiento
    extra = 0

class IntervencionAdmin(admin.ModelAdmin):
    inlines = [ExtraccionInLine,]

class EpisodioAdmin(admin.ModelAdmin):
    inlines = [BasalInLine, IntervencionInLine, TratamientoInLine, SeguimientoInLine]

class PacienteAdmin(admin.ModelAdmin):
    inlines = [EpisodioInLine,]

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Episodio, EpisodioAdmin)
admin.site.register(Basal)
admin.site.register(Intervencion, IntervencionAdmin)
admin.site.register(Extraccion)
