from django.db import models


# Create your models here.
class Motherboard(models.Model):
    title = models.CharField(verbose_name="Title/name", max_length=200)
    manufacturer = models.CharField(verbose_name="Manufacturer", max_length=50, null=True)
    form_factor = models.CharField(verbose_name="Form Factor", max_length=20, null=True)
    cpu_socket = None
    chipset = models.CharField(verbose_name="Chipset", max_length=20, null=True)
    memory_type = None
    memory_chanel = models.CharField(verbose_name="Memory Channel", max_length=20, null=True)
    audio = models.CharField(verbose_name="Audio", max_length=100, null=True)
    primary_gpu_interface = None
    internal_slots = models.TextField(verbose_name="Internal Connectivity")
    external_slots = models.TextField(verbose_name="External Connectivity")








