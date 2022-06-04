import random, time
import os

matriz = list()
matriz2 = list()
escolhidos = []
cont = False
os.system('cls') or None
while True:
    try:
        tamanho = int(input('Quantos linhas/colunas você quer seu tabuleiro? '))
    except:
        print('Valor inválido')
        time.sleep(2)
        os.system('cls') or None
    else:  
        break
    

for l in range(0, tamanho):
    linha = []
    linha2 = []
    for c in range(0, tamanho):
        num = random.randint(0, 1)
        linha.append(num)
        linha2.append('X')
    matriz.append(linha)
    matriz2.append(linha2)

while True:
    time.sleep(2)
    os.system('cls') or None
    for l in range(0, tamanho):
        for c in range(0, tamanho):
            if (c == tamanho-1):
                print(f'{matriz2[l][c]}')
            else:
                print(f'{matriz2[l][c]}', end=' ')
    
    posLinha = int(input('Linha: '))
    posColuna = int(input('Coluna: '))
    for pos in escolhidos:
        if(pos[0] == posLinha and pos[1] == posColuna):
            print('Posição já escolhida')
            cont = True
            #print(f'Linha escolhida: {posLinha}')
            #print(f'Coluna escolhida {posColuna}')
            break
        else:
            cont = False
            
    if not(cont):
        matriz2[posLinha][posColuna] = matriz[posLinha][posColuna]
        escolhidos.append([posLinha,posColuna])
