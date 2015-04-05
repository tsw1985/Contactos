# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(upload_to=b'Imagenes', null=True, verbose_name=b'Im\xc3\xa1gen', blank=True),
            preserve_default=True,
        ),
    ]
