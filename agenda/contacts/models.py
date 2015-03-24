# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=100 , verbose_name='Nombre')
    phone = models.CharField(max_length=9 , verbose_name='Telefono')
    imagen =

    sport_activity = models.ForeignKey(SportActivity,verbose_name='Actividad')
    typetrainer = models.ForeignKey(TypeTrainer,verbose_name='Entrenamiento de')
    usergym = models.ForeignKey(User,verbose_name='Usuario')
    totaldays = models.IntegerField(verbose_name='Duración en días')

    def __unicode__(self):
        return self.name # + " -- " + self.sport_activity.description

    class Meta:
        app_label = 'BackEnd'
        verbose_name = 'Entrenamiento'
        verbose_name_plural = 'Definir Entrenamientos'

