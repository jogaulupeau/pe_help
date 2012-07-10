# -*- coding: utf-8 -*-
from django.db import models


class Competence(models.Model):
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
    parent = models.ForeignKey('self', blank=True, null=True)
    niveau = models.CharField(max_length=50, choices=NIVEAUX)
    def __unicode__(self):
        return self.titre
    class Meta:
        verbose_name = 'compétence'


class Activite(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    competence = models.ManyToManyField(Competence)
    def __unicode__(self):
        return self.titre
    class Meta:
        verbose_name = 'activité'


class Creneau(models.Model):
    date_debut = models.DateTimeField()
    duree = models.TimeField()
    activite = models.ForeignKey(Activite, related_name='creneaux')
    def __unicode__(self):
        return self.date_debut.strftime('%d/%m/%y %H:%M')
    class Meta:
        verbose_name = 'créneau'
        verbose_name_plural = 'créneaux'
