# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('rating', models.FloatField()),
                ('length', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('movie_id', models.ForeignKey(to='website.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('row', models.SmallIntegerField()),
                ('col', models.SmallIntegerField()),
                ('projection_id', models.ForeignKey(to='website.Projection')),
            ],
        ),
    ]
