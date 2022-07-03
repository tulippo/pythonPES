'''BeeCrowd 1215'''
# Entrada do texto que será tratado.
texto = input().lower().split(' ') #* Coloca-se tudo em minúsculo e transforma a string em lista.
N = len(texto) 
texto.sort()

x = 0
y = 0
dicionario_filtro = {} #* Dicionario que irá funcionar como filtro para termos repetidos.
lista_confimação = [] #* Lista que irá guardar os termos definitivos.
lista_apresentaçao = [] #* Lista que irá apresentar os termos em ordem alfabética.
dicionario_final = dict() #* Dicionario que irá guardar os termos definitivos.

# Filtrando os termos repetidos
for i in range(N):
    dicionario_filtro[x] = texto[x]
    for x, texto[x] in dicionario_filtro.items():
        if texto[x] not in lista_confimação:
            lista_confimação.append(texto[x])
            dicionario_final[x] = texto[x]
            lista_apresentaçao.append(dicionario_final[x])
    x += 1  
    i += 1
# Apresentando os termos de acordo com a quantidade no dicionario_final.
N = len(dicionario_final)
for j in range(N):
    print(lista_apresentaçao[y])
    y += 1
    j += 1
