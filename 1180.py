'''BeeCrowd 1180'''
# Criação da lista N dos números digitados.
N = int(input())
numeros = (input()).split(' ')
x = 0 #* Posição inicial 
lista = [] #* Nova lista que irá guardar os valores inteiros.
for i in range(N):
    lista.append(int(numeros[x])) 
    x += 1
    i += 1
menor_valor = sorted(lista) #* Organizando, em ordem crescente, os inteiros. 
index = (menor_valor[0]) #* O menor valor fica alocado na posição [0].
posiçao = lista.index(index) #* Posição do menor valor.

print(f'O menor valor é: {menor_valor[0]}')
print(f'A posição do menor valor é: {posiçao}')


