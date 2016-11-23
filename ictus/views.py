from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from django import template
from django.template.loader import get_template, TemplateDoesNotExist
from django.forms import inlineformset_factory

from .models import *
from .forms import *
import sys

def generate_breadcrumbs(**kwargs):
    #Home > Study > Case / Info / New
    patient = kwargs.get('patient', None)
    episode = kwargs.get('episode', None)
    new_patient = kwargs.get('new_patient', None)
    new_episode = kwargs.get('new_episode', None)

    breadcrumbs = [{'name':'Home','link':'/'},]

    if patient:
        breadcrumbs.append({'name':str(patient), 'link':'/patient/'+str(patient.pk)})

        if episode:
            breadcrumbs.append({'name':episode, 'link':'/patient/'+str(patient.pk)+"/"+str(episode.pk)})

    if new_patient:
        breadcrumbs.append({'name':'Nuevo Paciente', 'link':'./'})

    if new_episode:
        breadcrumbs.append({'name':'Nuevo Episodio', 'link':'./'})

    return breadcrumbs


@login_required
def patient_list(request):
    patients = Paciente.objects.all()

    return render(request,'ictus/patient_list.html',{
        'patients': patients,
    })


# Create your views here.
@login_required
def view_patient(request, patient_pk=None):

    try:
        patient = Paciente.objects.get(pk = patient_pk)
        episodes = patient.episodio_set.all()
    except:
        patient = None
        episodes = None

    is_new = patient is None

    breadcrumbs = generate_breadcrumbs(patient=patient, new_patient=is_new)

    if request.method == "POST":
        if not is_new:
            form = PacienteForm(request.POST, instance=patient)
        else:
            form = PacienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'ictus/paciente_edit.html', {
                'form': form,
                'patient': patient,
                'episodes': episodes,
                'new': is_new,
                'breadcrumbs':breadcrumbs,
                })

            #raise Exception("Form isn't valid. Form type: {}".format( type(form) ))
    else:
        if not is_new:
            form = PacienteForm(instance = patient)
            episodes = patient.episodio_set.all()
        else:
            form = PacienteForm()
            episodes = None

        return render(request, 'ictus/paciente_edit.html', {
            'form': form,
            'patient': patient,
            'episodes': episodes,
            'new': is_new,
            'breadcrumbs':breadcrumbs,
            })

@login_required
def new_episode(request,patient_pk):
    patient = Paciente.objects.get(pk=patient_pk)
    breadcrumbs = generate_breadcrumbs(patient=patient, new_episode=True)

    if request.method == "POST":
        episode = Episodio()
        episode.paciente_id = patient_pk
        episode_form = EpisodeForm(request.POST, instance=episode)

        if episode_form.is_valid():
            episode_form.save()
            return HttpResponseRedirect("/episode/"+str(episode.pk)+"/")

    else:
        episode_form = EpisodeForm()

    return render(request, "ictus/episodio_edit.html", {
        "form":episode_form,
        "patient":patient,
        'new': True,
        'breadcrumbs':breadcrumbs,
    })

@login_required
def view_episode(request, episode_pk):

    episode = Episodio.objects.get(pk=episode_pk)

    breadcrumbs = generate_breadcrumbs(patient=episode.paciente, episode=episode)

    BasalInLineFormSet = inlineformset_factory(Episodio, Basal, extra=0, exclude=() )
    ExtractionInLineFormSet = inlineformset_factory(Episodio, Extraccion, extra=0, exclude=() )
    TreatmentInlineFormSet = inlineformset_factory(Episodio, Tratamiento , extra=0, exclude=() )
    InterventionInlineFormSet = inlineformset_factory(Episodio, Intervencion , extra=0, exclude=() )
    SeguimientoInLineFormSet = inlineformset_factory(Episodio, Seguimiento, extra=0, exclude=() )


    #Save the POST first (if it's valid). Otherwise return and render the errors
    if request.method == "POST":
        episode_form = EpisodeForm(request.POST, instance=episode)

        basal_formset = BasalInLineFormSet(request.POST, request.FILES, instance=episode)
        extraction_formset = ExtractionInLineFormSet(request.POST, request.FILES, instance=episode)
        intervention_formset = InterventionInlineFormSet(request.POST, request.FILES, instance=episode)
        treatment_formset = TreatmentInlineFormSet(request.POST, request.FILES, instance=episode)
        seguimiento_formset = SeguimientoInLineFormSet(request.POST, request.FILES, instance=episode)

        all_valid = True
        forms = [episode_form, basal_formset, extraction_formset, intervention_formset, treatment_formset, seguimiento_formset]
        for f in forms:
            if f.is_valid():
                f.save()
            else:
                all_valid = False

        if not all_valid:
            return render(request, "ictus/episodio_edit.html", {
                "form":episode_form,
                "basal_formset": basal_formset,
                "extraction_formset": extraction_formset,
                "treatment_formset": treatment_formset,
                "intervention_formset": intervention_formset,
                "seguimiento_formset": seguimiento_formset,
                "patient":episode.paciente,
                'breadcrumbs': breadcrumbs,
            })
        """"
        If everything is OK, check if we should add fields.
            If so, render the edit again (with extras)
            Else, everything is done: exit editing
        """
        add_fields = ["add_basal", "add_extraction", "add_treatment", "add_intervention", "add_seguimiento"]
        adding = any( field in request.POST for field in add_fields)
        if adding:
            #If the request is adding fields, add the extras and render the edit template
            if "add_basal" in request.POST:
                BasalInLineFormSet = inlineformset_factory(Episodio, Basal , extra=1, exclude=() )
            if "add_extraction" in request.POST:
                ExtractionInLineFormSet = inlineformset_factory(Episodio, Extraccion , extra=1, exclude=() )
            if "add_treatment" in request.POST:
                TreatmentInlineFormSet = inlineformset_factory(Episodio, Tratamiento , extra=1, exclude=() )
            if "add_intervention" in request.POST:
                InterventionInlineFormSet = inlineformset_factory(Episodio, Intervencion , extra=1, exclude=() )
            if "add_seguimiento" in request.POST:
                SeguimientoInLineFormSet = inlineformset_factory(Episodio, Seguimiento , extra=1, exclude=() )

            basal_formset = BasalInLineFormSet(instance=episode)
            extraction_formset = ExtractionInLineFormSet(instance=episode)
            treatment_formset = TreatmentInlineFormSet(instance=episode)
            intervention_formset = InterventionInlineFormSet(instance=episode)
            seguimiento_formset = SeguimientoInLineFormSet(instance=episode)

            return render(request, "ictus/episodio_edit.html", {
                "form":episode_form,
                "basal_formset": basal_formset,
                "extraction_formset": extraction_formset,
                "treatment_formset": treatment_formset,
                "intervention_formset":intervention_formset,
                "seguimiento_formset": seguimiento_formset,
                "patient":episode.paciente,
                'breadcrumbs': breadcrumbs,
            })

        else:
            #if not adding, everything is done, exit editing
            return redirect("/patient/"+ str(episode.paciente.pk) +"/")
    else:
        #If the request is NOT a POST, render the edit normaly
        episode_form = EpisodeForm(instance = episode)
        basal_formset = BasalInLineFormSet(instance=episode)
        extraction_formset = ExtractionInLineFormSet(instance=episode)
        treatment_formset = TreatmentInlineFormSet(instance=episode)
        intervention_formset = InterventionInlineFormSet(instance=episode)
        seguimiento_formset = SeguimientoInLineFormSet(instance=episode)

        return render(request, "ictus/episodio_edit.html", {
            "form":episode_form,
            "basal_formset": basal_formset,
            "extraction_formset": extraction_formset,
            "treatment_formset": treatment_formset,
            "intervention_formset":intervention_formset,
            "seguimiento_formset": seguimiento_formset,
            "patient":episode.paciente,
            'breadcrumbs': breadcrumbs,
        })
