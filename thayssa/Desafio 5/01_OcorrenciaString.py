#   Faça um programa que leia uma frase pelo teclado e mostre:
#       - Quantas vezes aparece a letra 'A'
#       - Em que posição ela aparece a primeira vez
#       - Em que posição ela aparece a última vez

frase = input('digite uma frase: ')

t = len(frase)
conta = 0
for j in range(t):
    if frase[j] == 'a' or frase[j] == 'A':
        conta += 1 
                  

print('quantidades de A:', conta)
#print('posição do último A:', ultimo)
#print('posicao do primeiro A:', primeiro)