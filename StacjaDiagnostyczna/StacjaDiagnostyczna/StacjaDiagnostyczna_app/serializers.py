from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class pojazdSerializer(serializers.ModelSerializer):
    class Meta:
        model = pojazd
        fields = ['marka','model','numer_rejestracyjny']

class diagnostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = diagnosta
        fields = ['imie','nazwisko','pojazd']

class klientSerializer(serializers.ModelSerializer):
    class Meta:
        model = klient
        fields = ['imie','nazwisko','telefon','pojazd']

class badanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = badanie
        fields = ['pojazd', 'data_badania', 'status', 'ważnosc_badania']
