from django.contrib import admin
from .models import Paciente, Episodio, Basal

from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

class BasalInLine(admin.TabularInline):
	model = Basal

class EpisodioInLine(admin.TabularInline):
    model = Episodio
    extra = 0
    show_change_link = True

    #fields = ("h_inicio", 'tipo')
    readonly_fields = ('tipo',)

class EpisodioAdmin(admin.ModelAdmin):
    inlines = [BasalInLine,]

class PacienteAdmin(admin.ModelAdmin):
    inlines = [EpisodioInLine,]

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Episodio, EpisodioAdmin)
admin.site.register(Basal)