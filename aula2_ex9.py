# Exemplo 04

'''
    Exmeplo 4 para receber varios valores na mesma linha
    utilizando o split
'''

nome, idade, cidade = input(
    'Digite o nome, idade e cidade separados por espaço: '
).split() # aremazena os valores digitados pelo usuario nas variaveis acima

idade = int(idade) # converte a idade string para inteiro

# Conversão de valores é chamado de parse
# Exibe o nome, idade e cidade do usuario usando o f-string para a formatação de saida

print(f'{nome} tem {idade} anos e mora em {cidade}')

