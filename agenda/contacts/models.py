# -*- coding: utf-8 -*-
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100 , verbose_name='Nombre')
    first_name = models.CharField(max_length=100 , verbose_name='Apellido')
    email = models.CharField(max_length=100 , verbose_name='Email')
    phone = models.CharField(max_length=9 , verbose_name='Telefono')
    # photo = models.ImageField(upload_to='Imagenes' , null=True, blank=True,verbose_name='Imágen')

    def __unicode__(self):
        return self.name

