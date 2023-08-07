def separar (*lista):
    lista_pares = []
    lista_impares = []
    for i in lista:
        if i%2 ==0:
            lista_pares.append (i)
            lista_pares.sort()
        else:
            lista_impares.append (i)
            lista_impares.sort()

    return lista_pares, lista_impares

print (separar (13,12,5,8))