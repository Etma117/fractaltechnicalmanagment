# Generated by Django 4.2.6 on 2023-11-23 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0014_alter_categoria_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='accesorio',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.marca'),
        ),
    ]
