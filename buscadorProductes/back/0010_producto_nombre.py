# Generated by Django 3.0.3 on 2020-03-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscadorProductes', '0009_remove_producto_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='nombre',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
