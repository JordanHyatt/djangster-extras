# Generated by Django 4.0.6 on 2022-10-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_aux_geo', '0002_subdivision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdivision',
            name='iso_code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]