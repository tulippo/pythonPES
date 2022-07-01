vet1 = input('Dê entrada nos valores: ').split(' ')
a1 = int(vet1[0])
a2 = int(vet1[1])
a3 = float(vet1[2])

vet2 = (input('Dê entrada nos valores: ')).split(' ')
b1 = int(vet2[0])
b2 = int(vet2[1])
b3 = float(vet2[2])

valor_total1 = float(a2 * a3) 
valor_total2 = float(b2 * b3) 
total = valor_total1 + valor_total2

print('Valor a pagar: {.2f}'.format(total))