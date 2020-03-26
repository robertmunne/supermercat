# Generated by Django 3.0.3 on 2020-03-06 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estanterias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_estanteria', models.IntegerField()),
                ('n_almacen', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='buscadorProductes.Almacen')),
            ],
        ),
        migrations.CreateModel(
            name='Pasillos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_pasillo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EAN', models.CharField(max_length=13)),
                ('cantidad', models.IntegerField()),
                ('nombre', models.CharField(blank=True, max_length=140, null=True)),
                ('descipcion', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='localilizacionActualProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estanteria', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='buscadorProductes.Estanterias')),
                ('producto', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='buscadorProductes.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='estanterias',
            name='n_pasillo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='buscadorProductes.Pasillos'),
        ),
    ]
