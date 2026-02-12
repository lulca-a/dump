palavra_secreta = 'palavra'
palavra_oculta = list('*'*len(palavra_secreta))
tentativas = 1

while True:
    posicao=0
    letra = input('Digite uma letra') 
    
    if not letra.isalpha():
        print('Deve ser uma letra do alfabeto!')
        continue
    if len(letra)>1:
        print('Digite apenas uma letra!')
        continue
    
    for i in palavra_secreta:
        if i == letra.lower():
            palavra_oculta[palavra_secreta.index(i,posicao)] = i
        posicao+=1
    
    print(''.join(palavra_oculta))
    print(f'tentativas: {tentativas}')
    tentativas +=1
    
    if ''.join(palavra_oculta) == palavra_secreta:
        
        print(f'Parabéns, a palavra era: {"".join(palavra_oculta)}')
        break
