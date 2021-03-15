from rest_framework import serializers
from .models import Socket, CPU


class SocketSerializer(serializers.Serializer):
    socket_title = serializers.CharField(verbose_name="Socket title", max_length=15)

    def create(self, validated_data):
        return Socket.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.socket_title = validated_data.get("socket_title", instance.socket_title)


class CPUSerializer(serializers.Serializer):
    cpu_socket = serializers.ForeignKey("Socket", verbose_name="CPU Socket", on_delete=serializers.SET_NULL, null=True,
                                        blank=True)
    architecture = serializers.CharField(verbose_name="Architecture", max_length=50, null=True, blank=True)
    cores = serializers.CharField(verbose_name="Cores", max_length=4, null=True, blank=True)
    threads = serializers.CharField(verbose_name="Threads", max_length=4, null=True, blank=True)
    clock_speed = serializers.CharField(verbose_name="Clock Speed", max_length=10, null=True, blank=True)
    turbo_speed = serializers.CharField(verbose_name="Turbo Speed", max_length=10, null=True, blank=True)
    max_memory_size = serializers.CharField(verbose_name="Max. Memory Size", max_length=10, null=True, blank=True)
    max_memory_speed = serializers.CharField(verbose_name="Max. Memory Speed", max_length=15, null=True, blank=True)
    integrated_graphics = serializers.CharField(verbose_name="Integrated Graphics", max_length=100, null=True,
                                                blank=True)

    def create(self, validated_data):
        return CPU.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.cpu_socket = validated_data.get("cpu_socket", instance.cpu_socket)
        instance.architecture = validated_data.get("architecture", instance.architecture)
        instance.cores = validated_data.get("cores", instance.cores)
        instance.threads = validated_data.get("threads", instance.threads)
        instance.clock_speed = validated_data.get("clock_speed", instance.clock_speed)
        instance.turbo_speed = validated_data.get("turbo_speed", instance.turbo_speed)
        instance.max_memory_size = validated_data.get("max_memory_size", instance.max_memory_size)
        instance.max_memory_speed = validated_data.get("max_memory_speed", instance.max_memory_speed)
        instance.integrated_graphics = validated_data.get("integrated_graphics", instance.integrated_graphics)

