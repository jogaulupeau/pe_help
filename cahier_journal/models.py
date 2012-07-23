# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from cahier_journal.widgets import ColorPickerWidget
from datetime import timedelta
from django import forms


class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)


class Domaine(models.Model):
    NIVEAUX = (
                   ('Maternelle', (
                                   ('ps', 'PS'),
                                   ('ms', 'MS'),
                                   ('gs', 'GS'),
                                  )
                   ),
                   ('Cycle 2', (
                                ('cp', 'CP'),
                                ('ce1', 'CE1'),
                                ('ce2', 'CE2'),
                               )
                   ),
                   ('Cycle 3', (
                                ('cm1', 'CM1'),
                                ('cm2', 'CM2'),
                               )
                   )
                  )
    titre = models.CharField(max_length=250)
    niveau = models.CharField(max_length=50, choices=NIVEAUX, blank=True, null=True)
    couleur = ColorField(blank=True, null=True)
    def __unicode__(self):
        return self.titre


class Competence(models.Model):
    titre = models.CharField(max_length=250)
    domaine = models.ForeignKey(Domaine)
    def __unicode__(self):
        return self.titre
    class Meta:
        verbose_name = 'compétence'


class Objectif(models.Model):
    titre = models.CharField(max_length=250)
    competence = models.ForeignKey(Competence)
    def __unicode__(self):
        return self.titre


class Activite(models.Model):
    titre = models.CharField(max_length=200)
    objectif = models.ManyToManyField(Objectif)
    def __unicode__(self):
        return self.titre
    class Meta:
        verbose_name = 'activité'


class Creneau(models.Model):
    date_debut = models.DateTimeField()
    duree = models.TimeField()
    date_fin = models.DateTimeField(blank=True, null=True)
    activite = models.ForeignKey(Activite, related_name='creneaux')
    groupe = models.CharField(max_length=100, blank=True, null=True)
    bilan = models.TextField(blank=True, null=True)
    def save(self):
        self.date_fin = self.date_debut + timedelta(seconds = self.duree.minute * 60 + self.duree.hour * 3600)
        super(Creneau, self).save()
    def __unicode__(self):
        return self.date_debut.strftime('%d/%m/%y %H:%M')
    class Meta:
        verbose_name = 'créneau'
        verbose_name_plural = 'créneaux'


class DomaineForm(ModelForm):
    class Meta:
        model = Domaine


class CompetenceForm(ModelForm):
    class Meta:
        model = Competence


class ObjectifForm(ModelForm):
    class Meta:
        model = Objectif


class ActiviteForm(ModelForm):
    class Meta:
        model = Activite
        #widgets = { 'objectif': forms.HiddenInput(), }


class CreneauForm(ModelForm):
    class Meta:
        model = Creneau
        exclude = ('date_fin')
