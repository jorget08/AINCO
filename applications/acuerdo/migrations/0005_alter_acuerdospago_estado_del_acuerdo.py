# Generated by Django 3.2 on 2021-12-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acuerdo', '0004_auto_20211204_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acuerdospago',
            name='estado_del_acuerdo',
            field=models.CharField(max_length=50),
        ),
    ]
