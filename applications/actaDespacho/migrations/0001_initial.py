# Generated by Django 3.2 on 2022-03-07 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deudor', '0010_alter_deudor_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActaDespacho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_subida_acto', models.DateTimeField(auto_now_add=True)),
                ('fecha_acta', models.DateField()),
                ('num_radicacion', models.CharField(max_length=200)),
                ('clase_proceso', models.CharField(max_length=250)),
                ('num_despacho', models.CharField(max_length=200)),
                ('nombre_despacho', models.CharField(max_length=200)),
                ('juez_o_magistrado', models.CharField(max_length=250)),
                ('direccions_despacho', models.CharField(max_length=250)),
                ('ciudad_despacho', models.CharField(max_length=150)),
                ('tel_fijo', models.CharField(blank=True, max_length=7)),
                ('tel_fijo2', models.CharField(blank=True, max_length=7)),
                ('cel', models.CharField(blank=True, max_length=10)),
                ('cel2', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=250)),
                ('email2', models.EmailField(blank=True, max_length=250)),
                ('observaciones', models.TextField(blank=True)),
                ('comentarios', models.TextField(blank=True)),
                ('acta', models.FileField(upload_to='gestionActas')),
                ('deudor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actaDespacho_deudor', to='deudor.deudor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actaDespacho_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
