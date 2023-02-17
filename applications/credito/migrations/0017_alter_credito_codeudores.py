# Generated by Django 3.2 on 2021-11-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeudor', '0007_auto_20210910_1027'),
        ('credito', '0016_remove_credito_aportes_sociales_vencidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='codeudores',
            field=models.ManyToManyField(blank=True, null=True, related_name='credito_codeudor', to='codeudor.Codeudor'),
        ),
    ]
