'''BeeCrowd 1069'''
# Definindo a quantidade de diamantes.
N = int(input())
for i in range(N):
    diamante = str(input('Digite o diamante: ')) #* Digitar o diamante.
    d1 = diamante.count('<') #* Contagem dos pares essenciais para formar 1 diamante.
    d2 = diamante.count('>')
    if d1 < d2:
        diamantes_processados = d1 % d2 #* Cálcula-se sempre o menor valor pelo módulo do maior para definir a qtd. de pares
        print(diamantes_processados)
    elif d2 < d1:
        diamantes_processados = d2 % d1
        print(diamantes_processados)
    i += 1

    
