# Generated by Django 4.2.6 on 2023-11-27 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0018_alter_accesorio_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesorio',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.marca'),
        ),
    ]
