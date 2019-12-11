from django.db import models

# Create your models here.

class pojazd(models.Model):
    marka = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    numer_rejestracyjny = models.CharField(max_length=45)

class diagnosta(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko =  models.CharField(max_length=45)
    pojazd = models.ForeignKey(pojazd, on_delete=models.CASCADE)

class klient(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    telefon = models.CharField(max_length=45)
    pojazd = models.ForeignKey(pojazd, on_delete=models.CASCADE)

class badanie(models.Model):
    pojazd = models.ForeignKey(pojazd, on_delete=models.CASCADE)
    data_badania =  models.DateTimeField('data badania')
    status = models.BooleanField(default=False)
    ważnosc_badania = models.DateTimeField('Data końca ważności')
