def fun(a_lista, b_lista):
    return a_lista[1::2]+b_lista[0::2]

lista_ab = fun([2, 4, 5, 6, 7], [1, 2, 9, 8, 11])
print(lista_ab)