from django.shortcuts import render
from .forms import EpisodioForm
from ictus.models import Episodio
from material import LayoutMixin, Layout, Fieldset, Inline, Row, Span2, Span5, Span7

# Create your views here.

'''
def episodio_nuevo(request):
	form = EpisodioForm()
	return render(request, 'ictus/episodio_edit.html', {'form': form})
'''

class episodio_nuevo(LayoutMixin,
                      extra_views.NamedFormsetsMixin,
                      extra_views.CreateWithInlinesView):
    title = "Nuevo episodio"
    model = Episodio
    layout = Layout(
        Row('fecha_inicio', 'tipo_ictus', 'toast'),
        Fieldset('Address',
                 Row(Span7('address'), Span5('zipcode')),
                 Row(Span5('city'), Span2('state'), Span5('country'))),
    )
