'''
Exemplo 05 - Tratamento de erro com try except
'''

# Solicita ao usuário que digite sua idade e tenta converter para numero inteiro
while True:
    try:
        idade = int(input('Digite sua idade: '))

        if idade < 0:
            print('Digite uma idade válida')
            continue

        print(f'Sua idade é {idade} anos')
        break

    except ValueError:
        print('Erro!!! Digite um número inteiro válido.')
