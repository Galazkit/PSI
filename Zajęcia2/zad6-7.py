#zad 6 : Wyszukaj w Internecie pojęcie „extended slice” w kontekście Pythona i wyświetl swoje imię i
# nazwisko z odwróconą kolejnością znaków z kapitalikami. Np. Fotzsyzrk Kaipor

lista=list(range(1,11))
print(lista) #oryginalna lista
lista2=lista[5:] #przenosze do drugiej listy liczby po 5
del lista[5:] #usuwam z oryginalnej listy liczby po 5
print(lista)
print(lista2)

#zad 7 : Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak,
# aby pierwsze 5 liczb zostało w oryginalnej liście a pozostałe 5 znalazło się w nowej liście.
lista3 = lista+lista2 #lacze 2 listy
print(lista3)
lista3.insert(0,0) #dodaje 0 na poczatek
print(lista3)
lista3.sort(reverse=True) #sortuje malejaco
print(lista3)