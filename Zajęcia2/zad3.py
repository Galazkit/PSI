#------------------------------------------------
#zad3 Przejdź na stronę https://pyformat.info/ a następnie zapisz w oddzielnym pliku .py
# i wykonaj 5 wybranych przykładów formatowania ciągów oznaczonego jako „New”, których nie było w
# przykładach z tego podrozdziału (np. z wyrównaniem, ilością pozycji liczby, znakiem itp.).
#------------------------------------------------
# -1-
a='{} {}'.format('Testowy','tekst')
print(a)
# -2-
b='{:>5}'.format('tekst po prawej')
print(b)
# - 3 -
c='{first} {last}'.format(first='przykladowy',last='tekst')
print(c)
# - 4 -
d='{:=+5d}'.format(31)
print(d)
# - 5 -
dane = [12, 23, 34, 45, 56]
e='{d[2]} {d[3]}'.format(d=dane)
print(e)