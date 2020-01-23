from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class pojazdSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = pojazd
        fields = ['id','marka','model','numer_rejestracyjny','owner']

class diagnostaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = diagnosta
        fields = ['imie','nazwisko','pojazd','owner']

class klientSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = klient
        fields = ['imie','nazwisko','telefon','pojazd','owner']

class badanieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = badanie
        fields = ['pojazd', 'data_badania', 'status', 'ważnosc_badania','owner']
