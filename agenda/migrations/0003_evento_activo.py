# Generated by Django 3.2.20 on 2023-11-12 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_alter_evento_estado_reparacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
