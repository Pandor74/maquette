# Generated by Django 2.0.6 on 2018-10-18 07:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborateurs', '0011_auto_20181018_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='agence',
            name='num_SIRET',
            field=models.CharField(max_length=13, null=True, validators=[django.core.validators.RegexValidator(message='Le numéro SIRET doit être composé de 13 chiffres exactement', regex='^(?P<siret>\\d{13})$')], verbose_name='N° SIRET'),
        ),
        migrations.AddField(
            model_name='entreprise',
            name='num_SIREN',
            field=models.CharField(max_length=9, null=True, validators=[django.core.validators.RegexValidator(message='Le numéro SIREN doit être composé de 9 chiffres exactement', regex='^(?P<siren>\\d{9})$')], verbose_name='N° SIREN ou les 9 premiers chiffres de N°SIRET'),
        ),
        migrations.AlterField(
            model_name='agence',
            name='fax',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Le numéro de téléphone doit contenir exactement 10 chiffres', regex='^0(?P<num>\\d{9})$')]),
        ),
        migrations.AlterField(
            model_name='agence',
            name='telephone',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Le numéro de téléphone doit contenir exactement 10 chiffres', regex='^0(?P<num>\\d{9})$')]),
        ),
    ]
