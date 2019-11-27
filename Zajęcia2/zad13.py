#zad13
student1 = (145881,"Marcin","Gałązka")
student2 = (145882,"Albert","Godlewski")
student3 = (145883,"Patryk","Konopko")
student4 = (145884,"Artur","Dymkowski")

lista_studentow = [student1,student2,student3,student4]


slownik = dict([
  (student1[0], {"imie": student1[1],"nazwisko": student1[2],"wiek": 24, "email":"galazka@gmail.com","rok urodzenia":1997,"adres":"Piecki 11"}),
  (student2[0], {"imie": student2[1],"nazwisko": student2[2],"wiek": 19, "email":"heniek@wp.pl","rok urodzenia":1996,"adres":"Olsztyn 12"}),
  (student3[0], {"imie": student3[1],"nazwisko": student3[2],"wiek": 22, "email":"gienek@op.pl","rok urodzenia":1995,"adres":"Oczko 13"}),

])

print(slownik[145881]["wiek"],slownik[145881]["email"])
