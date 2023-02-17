# Generated by Django 3.2 on 2021-05-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeudor', '0006_remove_codeudor_credito'),
        ('credito', '0014_alter_credito_codeudores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='codeudores',
            field=models.ManyToManyField(related_name='credito_codeudor', to='codeudor.Codeudor'),
        ),
    ]
