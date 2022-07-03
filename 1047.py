'''BeeCrowd 1047'''
# Entrada dos valores dos horários.
N = input().split(' ')
horas1 = N[0]
minutos1 = N[1]
horas2 = N[2]
minutos2 = N[3]

# Calculando quantas horas durou a partida.
horas_total = int(horas2) - int(horas1)
if horas_total < 0:
    horas_total += 24

# Calculado quantos minutos durou a partida.
minutos_total = int(minutos2) - int(minutos1)
if minutos_total <= 0:
    minutos_total += 60 #* Caso a diferença de horário seja alguns minutos
    horas_total -= 1    #* será corrigida com a soma de 60 min e -1hora

# Printando o valores.
if minutos_total >= 1 and horas_total < 24:
    print(f'O JOGO DUROU {horas_total} HORA(S) E {minutos_total} MINUTO(S).')
elif minutos_total == 0 and horas_total == 0:
    print('O jogo durou 24 Horas.')
else:
    print('valores inadequados.')