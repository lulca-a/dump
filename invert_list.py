def inverter_lista(lista : list) -> list:
    lista_inversa=[]
    for i in lista[-1::-1]:
        lista_inversa.append(i)
    return lista_inversa

#I saw a challenge about inverting lists, so I tried it the second I learned about slicing.
