# Generated by Django 4.0.6 on 2022-09-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alpha2', models.CharField(max_length=2, null=True)),
                ('alpha3', models.CharField(max_length=3, unique=True)),
                ('num', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
