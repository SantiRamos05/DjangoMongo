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

class Documentacion(models.Model):
    proyecto = models.OneToOneField(Proyectos, on_delete=models.DO_NOTHING, verbose_name='Proyecto', null=True, blank=True)
    codigo = models.CharField(verbose_name="Codigo", max_length=150, unique=True)
    descripcion =  models.TextField(verbose_name="Descripcion", max_length=500)
    fecha = models.DateField(verbose_name="Fecha Creacion Documento")
    tipo = models.CharField(max_length=150, verbose_name="Tipo de Documento")
    version = models.CharField(verbose_name="Version", max_length=150, unique=True)
    


class HistoriasUsuario(models.Model):
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE, verbose_name='Proyecto', null=True, blank=True)
    identificacionhistoriausuario = models.CharField(verbose_name="Codigo", max_length=150, unique=True)
    descripcionhistoriausuario = models.TextField(verbose_name="Descripcion", max_length=500)
    fechainicioesperado = models.DateField(verbose_name="Fecha Inicio Esperado", null=True, blank=True)
    fechainicioreal = models.DateField(verbose_name="Fecha Inicio Real", null=True, blank=True)
    duracionesperada = models.DateField(verbose_name="Duracion Estimada", null=True, blank=True )
    duracionreal = models.DateField(verbose_name="Duracion Real", null=True, blank=True)

    empleados = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    documentacion = models.ArrayReferenceField(to = Documentacion, null=True, blank=True, related_name="documentacion")
    






    
