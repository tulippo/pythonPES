'''BeeCrowd 1040'''

N = input().split()
nota1 = float(N[0])
nota2 = float(N[1])
nota3 = float(N[2])
nota4 = float(N[3])
media = (nota1*2 + nota2*3 + nota3*4 + nota4*1)/10
print(media)
if media >= 7:
    print('Aprovado!')
elif media < 5:
    print('Reprovado!')
else:
    print('Aluno em exame')
    exame_final = float(input('Nota do exame: '))
    media_final = (media + exame_final)/2
    if media_final < 5:
        print('Aluno reprovado!')
    else:
        print(f'Aluno aprovado!!! Media final: {media_final}')