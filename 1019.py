'''BeeCrowd 1019'''
# Entrada do tempo em segundos.
t = int(input('Tempo em segundos: '))

segundos = minutos = t%60 #* Resto dos segundos e declaração dos minutos.
horas = minutos = (t - segundos)/60 #* Transformação da unidade para minutos e retirada do resto.
minutos = minutos%60 #* Resto dos minutos e declaração das horas.
horas = horas/60 #* Transformação da unidade para horas e retirada do resto.

print(f'{int(horas)}:{int(minutos)}:{int(segundos)}')
