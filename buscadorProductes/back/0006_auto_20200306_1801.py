# Generated by Django 3.0.3 on 2020-03-06 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscadorProductes', '0005_auto_20200306_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(default='.', max_length=140),
        ),
    ]
