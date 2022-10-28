# Generated by Django 4.0.6 on 2022-10-08 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_aux_geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubDivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_aux_geo.country')),
            ],
        ),
    ]