from django.contrib import admin
from .models import CPU, MemoryType, Motherboard, Socket, GPUInterface,RAM
# Register your models here.

admin.site.register(Motherboard)
admin.site.register(CPU)
admin.site.register(RAM)
admin.site.register(Socket)
admin.site.register(MemoryType)
admin.site.register(GPUInterface)
