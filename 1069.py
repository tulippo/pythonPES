'''BeeCrowd 1069'''

N = int(input())
for i in range(N):
    diamante = tuple(input('Digite o diamante: '))
    d1 = diamante.count('<')
    d2 = diamante.count('>')
    if d1 < d2:
        diamantes_processados = d1 % d2
        print(diamantes_processados)
    elif d2 < d1:
        diamantes_processados = d2 % d1
        print(diamantes_processados)
    i += 1

    
