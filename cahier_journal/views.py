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
        form = ActiviteForm(instance = o)
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
