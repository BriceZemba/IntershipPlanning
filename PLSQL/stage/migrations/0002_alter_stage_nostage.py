# Generated by Django 5.0.4 on 2024-05-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='nostage',
            field=models.CharField(max_length=4),
        ),
    ]