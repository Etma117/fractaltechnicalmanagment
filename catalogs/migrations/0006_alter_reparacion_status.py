# Generated by Django 3.2.20 on 2023-10-08 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0005_auto_20231008_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reparacion',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalogs.status'),
        ),
    ]
