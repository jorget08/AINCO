# Generated by Django 3.2 on 2022-07-11 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deudor', '0011_auto_20220405_1804'),
        ('empresaSocia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresasocia',
            name='deudores',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empresaSocia_deudor', to='deudor.deudor'),
        ),
    ]
