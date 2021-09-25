# Generated by Django 3.2.7 on 2021-09-23 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreclave', models.CharField(max_length=150, unique=True, verbose_name='Nombre clave del proyecto')),
                ('denominacioncomercial', models.CharField(choices=[('ventas', 'ventas'), ('tecnologia', 'tecnologia')], max_length=150, verbose_name='Denominacion Comercial')),
                ('fechainicio', models.DateField(verbose_name='Fecha de inicio')),
                ('fechafinalizacion', models.DateField(verbose_name='Fecha de final')),
                ('estadoactual', models.CharField(choices=[('NoIniciado', 'NoIniciado'), ('Comenzo', 'Comenzo'), ('Finalizado', 'Finalizado')], default='NoIniciado', max_length=150)),
                ('promotor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
