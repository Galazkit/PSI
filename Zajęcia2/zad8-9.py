#zad 8
a=(('123','Marcin','Gałązka','23','margal23@gm.com','1996','Piecki'),
   ('312','Albert','Godlewski','22','godlewski18@wp.pl','1997','Jeziorko'),
   ('456','Artur','Dymkowski','22','Dymkowski2@wp.pl','1997','Klewki'))

#zad 9
dict  = {}
for val in a:
   dict[val[0]] = val[1],val[2],val[3],val[4],val[5],val[6]
print(dict)