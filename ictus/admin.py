from django.contrib import admin
from .models import Paciente, Episodio, Basal

from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

class BasalInLine(admin.TabularInline):
	model = Basal

class EpisodioInLine(admin.TabularInline):
    model = Episodio
    """
    def link(self, instance):
        url =reverse('admin:%s_%s_change' % (instance._meta.app_label,  
                                              instance._meta.module_name),
                      args=(instance.id,))
        return mark_safe("<a href='%s'>Editar</a>" % url)
    """
    extra = 0
    show_change_link = True

    #fields = ("h_inicio", 'tipo')
    readonly_fields = ('tipo',)

class PacienteAdmin(admin.ModelAdmin):
    inlines = [EpisodioInLine,]

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Episodio)