# Generated by Django 3.2.20 on 2023-10-31 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_evento_estado_reparacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='estado_reparacion',
        ),
    ]
