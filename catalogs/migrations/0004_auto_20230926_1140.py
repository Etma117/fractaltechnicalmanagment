# Generated by Django 3.2.20 on 2023-09-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0003_auto_20230926_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reparacion',
            name='marca',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='modelo',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
