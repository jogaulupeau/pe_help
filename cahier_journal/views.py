from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from cahier_journal.models import *

def show(request, object, id):
    if object == 'activite':
        try:
            o = Activite.objects.get(pk=id)
        except Activite.DoesNotExist:
            o = Activite()
        if request.POST:
            form = ActiviteForm(request.POST, instance = o)
        else:
            form = ActiviteForm(instance = o)
    elif object == 'creneau':
        try:
            o = Creneau.objects.get(pk=id)
        except Creneau.DoesNotExist:
            o = Creneau()
        if request.POST:
            form = CreneauForm(request.POST, instance = o)
        else:
            form = CreneauForm(instance = o)
    elif object == 'competence':
        try:
            o = Competence.objects.get(pk=id)
        except Competence.DoesNotExist:
            o = Competence()
        if request.POST:
            form = CompetenceForm(request.POST, instance = o)
        else:
            form = CompetenceForm(instance = o)
    elif object == 'domaine':
        try:
            o = Domaine.objects.get(pk=id)
        except Domaine.DoesNotExist:
            o = Domaine()
        if request.POST:
            form = DomaineForm(request.POST, instance = o)
        else:
            form = DomaineForm(instance = o)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            o = form.instance
        return HttpResponseRedirect(reverse('cahier_journal.views.show', args=(object, o.id)))
    return render(request, 'base_show.html', {
            'form': form,
            'o': o,
            'object': object,
    })


def journee(request, annee, mois, jour):
    creneaux = Creneau.objects.filter(date_debut__startswith='%s-%s-%s' %(annee, mois, jour))
    return render(request, 'base_journee.html', {
            'creneaux': creneaux,
            'annee': annee,
            'mois': mois,
            'jour': jour,
    })
