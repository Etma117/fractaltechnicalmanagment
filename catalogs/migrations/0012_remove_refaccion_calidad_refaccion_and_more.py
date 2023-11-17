# Generated by Django 4.2.6 on 2023-11-16 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0011_auto_20231031_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refaccion',
            name='calidad_refaccion',
        ),
        migrations.RemoveField(
            model_name='refaccion',
            name='tipo_de_pieza',
        ),
        migrations.RemoveField(
            model_name='reparacion',
            name='refaccion',
        ),
        migrations.RemoveField(
            model_name='reparacion',
            name='status',
        ),
        migrations.RemoveField(
            model_name='reparacion',
            name='tipo_de_reparacion',
        ),
        migrations.AddField(
            model_name='accesorio',
            name='imagen',
            field=models.ImageField(blank=True, default='accesorios/default.jpg', null=True, upload_to='accesorios/'),
        ),
        migrations.DeleteModel(
            name='CalidadRefaccion',
        ),
        migrations.DeleteModel(
            name='Refaccion',
        ),
        migrations.DeleteModel(
            name='Reparacion',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.DeleteModel(
            name='TipoRefaccion',
        ),
        migrations.DeleteModel(
            name='TipoReparacion',
        ),
    ]