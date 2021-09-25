from django.db import models
from django.db.models.base import Model
from accounts.models import User
# Create your models here.

DENOMINACION_COMERCIAL =(
    ('ventas', 'ventas'),
    ('tecnologia', 'tecnologia')
)
ESTADO =(
    ('NoIniciado', 'NoIniciado'),
    ('Comenzo', 'Comenzo'),
    ('Finalizado', 'Finalizado')
)


class Proyectos(models.Model):
    nombreclave = models.CharField(verbose_name="Nombre clave del proyecto", max_length=150, unique=True)
    promotor = models.OneToOneField(User, on_delete=models.DO_NOTHING, null= True, blank=True)
    denominacioncomercial = models.CharField(verbose_name="Denominacion Comercial", choices=DENOMINACION_COMERCIAL, max_length=150)
    fechainicio = models.DateField(verbose_name="Fecha de inicio")
    fechafinalizacion = models.DateField(verbose_name="Fecha de final")
    estadoactual = models.CharField(max_length=150, choices=ESTADO, default="NoIniciado")

    def __str__(self):
        return self.nombreclave
    