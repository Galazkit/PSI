#zad1 Pobierz ze strony https://pl.lipsum.com/
# tekst akapitu o tytule „Czym jest Lorem Ipsum” i przypisz go do zmiennej.
#------------------------------------------------

Txt= "Lorem Ipsum jest tekstem stosowanym jako " \
   "przykładowy wypełniacz w przemyśle poligraficznym. Został " \
   "po raz pierwszy użyty w XV w. przez nieznanego drukarza do " \
   "wypełnienia tekstem próbnej książki. Pięć wieków później zaczął" \
   " być używany przemyśle elektronicznym, pozostając praktycznie " \
   "niezmienionym. Spopularyzował się w latach 60. XX w. wraz z " \
   "publikacją arkuszy Letrasetu, zawierających fragmenty Lorem " \
   "Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem " \
   "przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
#print(Txt)

#------------------------------------------------
#zad2
#------------------------------------------------
imie = "Marcin"
nazwisko = "Gałązka"
litera_1=imie[2]
litera_2=nazwisko[3]

licz1=Txt.count(litera_1)
licz2=Txt.count(litera_2)

ans='w tekscie jest {} liter {} oraz {} liter {} '.format(licz1,litera_1,licz2,litera_2)
print(ans)

