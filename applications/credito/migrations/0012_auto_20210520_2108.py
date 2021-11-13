# Generated by Django 3.2 on 2021-05-21 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeudor', '0006_remove_codeudor_credito'),
        ('credito', '0011_credito_codeudores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credito',
            name='codeudores',
        ),
        migrations.AddField(
            model_name='credito',
            name='codeudores',
            field=models.ManyToManyField(blank=True, null=True, related_name='credito_codeudor', to='codeudor.Codeudor'),
        ),
    ]
