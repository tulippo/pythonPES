'''BeeCrowd 1215'''
texto = input().lower().split(' ')
N = len(texto)
texto.sort()

x = 0
y = 0
dicionario_filtro = {}
temp = []
ultima_lista = []
res = dict()

for i in range(N):
    dicionario_filtro[x] = texto[x]
    for x, texto[x] in dicionario_filtro.items():
        if texto[x] not in temp:
            temp.append(texto[x])
            res[x] = texto[x]
            ultima_lista.append(res[x])
    x += 1  
    i += 1
    
N = len(res)
for j in range(N):
    print(ultima_lista[y])
    y += 1
    j += 1
