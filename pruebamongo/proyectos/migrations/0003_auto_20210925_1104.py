# Generated by Django 3.2.7 on 2021-09-25 16:04

from django.conf import settings
from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectos', '0002_proyectoempleados'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyectoempleados',
            name='empleados',
        ),
        migrations.AddField(
            model_name='proyectoempleados',
            name='empleados',
            field=djongo.models.fields.ArrayReferenceField(blank=True, null=True, on_delete=djongo.models.fields.ArrayReferenceField._on_delete, related_name='empleados', to=settings.AUTH_USER_MODEL),
        ),
    ]
