'''BeeCrowd 1180'''

N = int(input())
numeros = (input()).split(' ')
x = 0
lista = []
for i in range(N):
    lista.append(int(numeros[x]))
    x += 1
    i += 1
menor_valor = sorted(lista)
index = (menor_valor[0])
posiçao = lista.index(index)

print(f'O menor valor é: {menor_valor[0]}')
print(f'A posição do menor valor é: {posiçao}')


