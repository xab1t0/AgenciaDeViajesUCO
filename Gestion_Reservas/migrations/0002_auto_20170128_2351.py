# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 23:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
        ('Gestion_Agencia', '0002_delete_avion'),
        ('Gestion_Reservas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nombre_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Agencia.Hotel')),
                ('nombre_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuario')),
            ],
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='nombre_hotel',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
    ]