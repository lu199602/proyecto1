# Generated by Django 5.1.1 on 2024-10-04 06:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto1', '0002_rename_producto_productoo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productoo',
            name='fechaCreacion',
        ),
        migrations.AddField(
            model_name='productoo',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='productoo',
            name='fecha_modificacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
