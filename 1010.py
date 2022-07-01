'''BeeCrowd 1010'''
# Manipulação de strings para a entrada das variavéis dos produtos. 
produto1 = input('Dê entrada nos valores (1 produto): ').split(' ')
a1 = int(produto1[0]) #* Valor do código de série do produto.
a2 = int(produto1[1]) #* Unidades do produto. 
a3 = float(produto1[2]) #* Preço do produto. 

# A mesma estrutura anterior se repete para o produto 2.
produto2 = input('Dê entrada dos valores (2 produto): ').split(' ')
b1 = int(produto2[0]) 
b2 = int(produto2[1])
b3 = float(produto2[2])

# Cálculo dos preços de cada compra, e posteriormente o valor total. 
valor_total1 = float(a2 * a3) 
valor_total2 = float(b2 * b3) 
total = valor_total1 + valor_total2


print(f'Valor a pagar: R${total:.2f}')
