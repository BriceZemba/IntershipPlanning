# Generated by Django 5.0.4 on 2024-05-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stagiaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numsta', models.IntegerField()),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('annee', models.IntegerField()),
                ('diplome', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=1)),
                ('stage' ,models.CharField()),
            ],
        ),
    ]
