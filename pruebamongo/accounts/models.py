from djongo import models
from django.contrib.auth.models import Group, AbstractUser

class User(AbstractUser):
    identificacion = models.CharField(unique=True, verbose_name='Identificacion', max_length=250)
    direccion = models.CharField(max_length=250, verbose_name='Direccion')
    telefono = models.CharField(max_length=250, verbose_name='Telefono')
    fechacontrato = models.DateField(verbose_name='Fecha de Contatacion', auto_now_add=True)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)