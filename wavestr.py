import os
import time

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

texto = input()
texto = texto.lower()
lista_texto=[]

for i in texto:
    lista_texto.append(i)
velocidade = 0.2

while True:
    for o in range(len(lista_texto)):
        if o == 0:
            inicio = ''.join(lista_texto)
            print(inicio.capitalize())
            time.sleep(velocidade)
            limpar_terminal()
        else:
            antes =''.join(lista_texto[:o])
            durante = lista_texto[o].upper()
            depois = ''.join(lista_texto[o+1:])
            print(f'{antes}{durante}{depois}')
            time.sleep(velocidade)
            limpar_terminal()
#coloca maiusculo o primeiro - printa
#limpa - minusculuo o primeiro - maiusculo o segundo - printa
#
#receber frase
#contar quantos str tem exceto espaços
#criar lista com cada caractere
#loop: capitaliza o primeiro d alista, limpa, capitaliza o segundo, limpa... e volta!

