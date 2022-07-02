import random

jokenpo = ['pedra','papel','tesoura','spock','lagarto'] 

N = int(input())

for i in range(N):
    i += 1  
    sheldon = random.choice(jokenpo)
    raj = random.choice(jokenpo)
    print(f'sheldou escolheu: {sheldon}')
    print(f'raj escolheu {raj}')
    
    if sheldon == raj:
        print(f'Caso #{i}: De novo!\n')

    elif sheldon == 'pedra': #*pedra
        if raj == 'papel' or raj == 'spock':
            resultado = 'Raj trapaceou!' #!
        elif raj == 'lagarto' or raj == 'tesoura':
            resultado = 'Bazinga!' #*
        print(f'Caso #{i}: {resultado}\n')

    elif sheldon == 'papel': #*papel
        if raj == 'tesoura' or 'lagarto':
            resultado = 'Raj trapaceou!' #!
        elif raj == 'pedra' or raj == 'spock':
            resultado = 'Bazinga!' #*
        print(f'Caso #{i}: {resultado}\n')

    elif sheldon == 'tesoura': #*tesoura
        if raj == 'pedra' or raj == 'spock':
            resultado = 'Raj trapaceou!'#!
        elif raj == 'papel' or raj == 'lagarto':    
            resultado = 'Bazinga!' #*
        print(f'Caso #{i}: {resultado}\n')

    elif sheldon == 'lagarto': #*lagarto
        if raj == 'tesoura' or raj == 'pedra':
            resultado = 'Raj trapaceou!'#!
        elif raj == 'spock' or raj == 'papel':
            resultado = 'Bazinga!' #*
        print(f'Caso #{i}: {resultado}\n')

    elif sheldon == 'spock': #spock
        if raj == 'papel' or raj == 'lagarto':
            resultado = 'Raj trapaceou!'#!
        elif raj == 'pedra' or raj == 'tesoura':
            resultado = 'Bazinga!' #*
        print(f'Caso #{i}: {resultado}\n') 
    
    

'''
pedra > lagarto
pedra > tesoura
papel > pedra
papel > spock
tesoura > papel
tesoura > lagarto
lagarto > spock
lagarto > papel
spock > pedra
spock > tesoura
'''