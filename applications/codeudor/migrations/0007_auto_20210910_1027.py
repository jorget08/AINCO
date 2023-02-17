# Generated by Django 3.2 on 2021-09-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeudor', '0006_remove_codeudor_credito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeudor',
            name='celular2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='codeudor',
            name='tel_fijo',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='codeudor',
            name='tel_fijo2',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
