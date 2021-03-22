from django.shortcuts import render, HttpResponse
from .models import Socket, CPU
from .serializers import SocketSerializer, CPUSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def socket_list(request):
    # get all sockets
    if request.method == 'GET':
        sockets = Socket.objects.all()
        serializer = SocketSerializer(sockets, many=True)
        return JsonResponse(serializer.data, safe=False)
    # add new socket
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SocketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def socket_detail(request, pk):
    try:
        socket = Socket.objects.get(pk=pk)
    except Socket.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = SocketSerializer(socket)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SocketSerializer(socket, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        socket.delete()
        return HttpResponse(status=204)




