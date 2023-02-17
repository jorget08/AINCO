# Generated by Django 3.2 on 2021-05-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('tel_fijo', models.CharField(max_length=7)),
                ('celular', models.CharField(max_length=10)),
                ('responsable', models.CharField(max_length=100)),
                ('num_trabajadores', models.PositiveSmallIntegerField()),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
