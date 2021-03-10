from django.db import models


# Create your models here.
class CommonInfo(models.Model):
    title = models.CharField(verbose_name="Title/name", max_length=200)
    manufacturer = models.CharField(verbose_name="Manufacturer", max_length=50, null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Motherboard(CommonInfo):
    form_factor = models.CharField(verbose_name="Form Factor", max_length=20, null=True, blank=True)
    cpu_socket = models.ForeignKey("Socket", verbose_name="CPU Socket", on_delete=models.SET_NULL, null=True,
                                   blank=True)
    chipset = models.CharField(verbose_name="Chipset", max_length=20, null=True, blank=True)
    memory_type = models.ForeignKey("MemoryType", verbose_name="Memory type", on_delete=models.SET_NULL, null=True,
                                    blank=True)
    memory_chanel = models.CharField(verbose_name="Memory Channel", max_length=20, null=True, blank=True)
    audio = models.CharField(verbose_name="Audio", max_length=100, null=True, blank=True)
    primary_gpu_interface = models.ForeignKey("GPUInterface", verbose_name="Primary GPU interface",
                                              on_delete=models.SET_NULL, null=True, blank=True)
    internal_slots = models.TextField(verbose_name="Internal Connectivity")
    external_slots = models.TextField(verbose_name="External Connectivity")


class CPU(CommonInfo):
    cpu_socket = models.ForeignKey("Socket", verbose_name="CPU Socket", on_delete=models.SET_NULL, null=True,
                                   blank=True)
    architecture = models.CharField(verbose_name="Architecture", max_length=50, null=True, blank=True)
    cores = models.CharField(verbose_name="Cores", max_length=4, null=True, blank=True)
    threads = models.CharField(verbose_name="Threads", max_length=4, null=True, blank=True)
    clock_speed = models.CharField(verbose_name="Clock Speed", max_length=10, null=True, blank=True)
    turbo_speed = models.CharField(verbose_name="Turbo Speed", max_length=10, null=True, blank=True)
    max_memory_size = models.CharField(verbose_name="Max. Memory Size", max_length=10, null=True, blank=True)
    max_memory_speed = models.CharField(verbose_name="Max. Memory Speed", max_length=15, null=True, blank=True)
    integrated_graphics = models.CharField(verbose_name="Integrated Graphics", max_length=100, null=True, blank=True)


class RAM(CommonInfo):
    memory_type = models.ForeignKey("MemoryType", verbose_name="Memory type", on_delete=models.SET_NULL, null=True,
                                    blank=True)
    capacity = models.CharField(verbose_name="Size/Capacity", max_length=15, null=True, blank=True)
    memory_speed = models.CharField(verbose_name="Memory Speed", max_length=15, null=True, blank=True)


class Socket(models.Model):
    socket_title = models.CharField(verbose_name="Socket title", max_length=15)

    def __str__(self):
        return self.socket_title


class MemoryType(models.Model):
    memory_type = models.CharField(verbose_name="Memory type", max_length=15)

    def __str__(self):
        return self.memory_type


class GPUInterface(models.Model):
    gpu_interface = models.CharField(verbose_name="GPU interface", max_length=15)

    def __str__(self):
        return self.gpu_interface
