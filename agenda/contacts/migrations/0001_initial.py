# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('first_name', models.CharField(max_length=100, verbose_name=b'Apellido')),
                ('email', models.CharField(max_length=100, verbose_name=b'Email')),
                ('phone', models.CharField(max_length=9, verbose_name=b'Telefono')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
