from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from cahier_journal.models import *
from django.core import serializers

def getjson(request, object, id_parent):
    if object == 'competence':
        liste = Competence.objects.filter(domaine__pk__exact=id_parent)
    if object == 'objectif':
        liste = Objectif.objects.filter(competence__pk__exact=id_parent)
    data = {}
    for i in liste:
        data[i.pk] = i
    return HttpResponse(serializers.serialize("json", liste))

def show(request, object, id):
    if object == 'activite':
        try:
            o = Activite.objects.get(pk=id)
        except Activite.DoesNotExist:
            o = Activite()
        if request.POST:
            form = ActiviteForm(request.POST, instance = o)
            if form.is_valid():
                form.save()
                o = form.instance
        else:
            form = ActiviteForm(instance = o)
        return render(request, 'base_activite.html', {
            'form': form,
            'o': o,
            'object': object,
            'domaines': Domaine.objects.all(),
            'competences': Competence.objects.all(),
            'objectifs': Objectif.objects.all(),
        })
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


def objectif(request):
    return render(request, 'base_objectif.html', {
            'objectifs': Objectif.objects.all(),
            'domaines': Domaine.objects.all(),
            'competences': Competence.objects.all(),
    })
