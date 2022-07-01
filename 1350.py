'''BeeCrowd 1350'''
N = 1 
while N != 0:
    # Entrada da quantidade de sentenças que serão lidas.
    N = int(input(' '))
    verdadeiras = 0 #* Declaração de variavéis.
    falsas = 0

    # Loop para a leitura de sentenças sucessivas.
    for i in range(N): 
        sentença = str(input(' '))
        if sentença.find('true') != -1: #* Verificando a presença de sentenças verdadeiras. 
            verdadeiras += 1            #* O .find() retorna -1 caso não ache a palavra dentro da string.
        else:
            falsas += 1
        i += 1

    # Caso todas as sentenças sejam falsas, deve-se considerar uma incosistência.
    if N == 0:
        print('Código encerrado.')
    elif N == falsas and falsas != 0:
        print('inconsistente')
    else: 
        print(f'{verdadeiras} sentenças são verdadeiras.')
        print(f'{falsas} sentenças são falsas.')
