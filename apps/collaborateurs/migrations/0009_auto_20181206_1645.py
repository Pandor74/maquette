# Generated by Django 2.1.2 on 2018-12-06 16:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('collaborateurs', '0008_auto_20181206_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppelOffre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projet', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='collaborateurs.Projet')),
            ],
        ),
        migrations.CreateModel(
            name='AppelOffreGlobal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projet', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='collaborateurs.Projet')),
            ],
        ),
        migrations.CreateModel(
            name='AppelOffreLot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_lancement', models.DateField(default=datetime.date.today, verbose_name='Date de démarrage de la consultation')),
                ('relance', models.IntegerField(blank=True, max_length=2)),
                ('AO', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='collaborateurs.AppelOffre')),
                ('AO_agences', models.ManyToManyField(blank=True, to='collaborateurs.Agence')),
            ],
        ),
        migrations.CreateModel(
            name='Echeance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date de fin de la consultation')),
                ('appel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='collaborateurs.AppelOffre')),
                ('appelGlobal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='collaborateurs.AppelOffreGlobal')),
                ('appelLot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='collaborateurs.AppelOffreLot')),
                ('projet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='collaborateurs.Projet')),
            ],
        ),
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AO', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='collaborateurs.AppelOffre')),
                ('agence', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='collaborateurs.Agence')),
            ],
        ),
        migrations.AlterField(
            model_name='personne',
            name='date_inscription_personne',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 6, 16, 45, 4, 606697, tzinfo=utc), verbose_name="Date d'inscription "),
        ),
        migrations.AddField(
            model_name='offre',
            name='personne',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='collaborateurs.Personne'),
        ),
        migrations.AddField(
            model_name='appeloffrelot',
            name='AO_personnes',
            field=models.ManyToManyField(blank=True, to='collaborateurs.Personne'),
        ),
        migrations.AddField(
            model_name='appeloffrelot',
            name='lot',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='collaborateurs.Lot'),
        ),
        migrations.AddField(
            model_name='appeloffrelot',
            name='projet',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='collaborateurs.Projet'),
        ),
    ]