'''
Estrutura Condicionais - If, if e Else
'''

n1 = input('Digite o numero n1: ')
n2 = input('Digite o numero n2: ')


if n1>n2:
    print(f'O número {n1} é maior que o {n2}')

elif n2>n1:
    print(f'O número {n2} é maior que o {n1}')
else:
    print(f'O número {n1} e {n2} são iguais')