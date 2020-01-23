from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from django.http import JsonResponse
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from django.http import Http404

# Create your views here.

@api_view(['GET','POST'])
def pojazd_list(request):
    if request.method == 'GET':
        pojazd1 = pojazd.objects.all()
        serializer = pojazdSerializer(pojazd1, many=True)
        #return Response(serializer.data)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = pojazdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer.save()
            #return Response(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.data, status.HTTP_201_CREATED)
        #return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pojazd_detail(request, pk):
    try:
        pojazd1 = pojazd.objects.get(pk=pk)
    except pojazd1.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = pojazdSerializer(pojazd1)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = klientSerializer(pojazd1, request.data)
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        pojazd1.delete()
        return Response(status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def diagnosta_list(request):
    if request.method == 'GET':
        diagnosta1 = diagnosta.objects.all()
        serializer = diagnostaSerializer(diagnosta1, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = diagnostaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.data, status.HTTP_201_CREATED)
        #return JsonResponse(serializer.data, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def diagnosta_detail(request, pk):
        try:
            diagnosta1 = diagnosta.objects.get(pk=pk)
        except diagnosta.DoesNotExist:
            return HttpResponse(status=404)
        if request.method == 'GET':
            serializer = diagnostaSerializer(diagnosta1)
            return Response(serializer.data)
        if request.method == 'PUT':
            serializer = diagnostaSerializer(diagnosta1, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            diagnosta.delete()
            return Response(status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def klient_list(request):
    if request.method == 'GET':
        klient1 = klient.objects.all()
        serializer = klientSerializer(klient1, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = klientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse (serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.data, status.HTTP_201_CREATED)
        #return JsonResponse(serializer.data, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def klient_detail(request, pk):
    try:
        klient1 = klient.objects.get(pk=pk)
    except klient.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = klientSerializer(klient1)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = klientSerializer(klient1, request.data)
        if serializer.is_valid():
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        klient.delete()
        return Response(status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def badanie_list(request):
    if request.method == 'GET':
        badanie1 = badanie.objects.all()
        serializer = badanieSerializer(badanie1, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = badanieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.data, status.HTTP_201_CREATED)
        #return JsonResponse(serializer.data, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def badanie_detail(request, pk):
    try :
        badanie1 = badanie.objects.get(pk=pk)
    except badanie1.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = badanieSerializer(badanie1)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = badanieSerializer(badanie1, request.data)
        if serializer.is_valid():
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        badanie1.delete()
        return Response(status.HTTP_204_NO_CONTENT)

