from djongo import models
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

class ProyectoEmpleados(models.Model):
    proyecto = models.OneToOneField(Proyectos, on_delete=models.DO_NOTHING, verbose_name='Proyecto')
    empleados = models.ArrayReferenceField(to = User, null=True, blank=True, related_name="empleados")



class HistoriasUsuario(models.Model):
    identificacionhistoriausuario = models.CharField(verbose_name="Identificacion de Historia de usuario", max_length=150, unique=True)
    descripcionhistoriausuario = models.CharField(verbose_name="Historia de usuario", max_length=500)
    documentacion = models.FileField(upload_to = "Uploaded Files/")
    empleados = models.ArrayReferenceField(to = User, null=True, blank=True, related_name="husuario")