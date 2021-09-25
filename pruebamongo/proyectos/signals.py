from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProyectoEmpleados, Proyectos



@receiver(post_save, sender = Proyectos)
def agregarUsuarios(instance, sender, created, **kwargs):
    if created:
        ProyectoEmpleados.objects.get_or_create(proyecto = instance)

