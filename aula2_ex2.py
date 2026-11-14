# Mensagem de boas-vindas
# Exemplo simples de apresentação e tipo de variável em Python.

print("Aula 2 - Data Science")

num = 10
print(f"Valor de num: {num}")
print(f"Tipo de num: {type(num)}")


nome_aluno = 'Rocky'
idade_aluno = 15
media_aluno = 8.5

print('Nome do aluno %s, ele tem %d anos w sua média é %f.'%(nome_aluno, idade_aluno, media_aluno))
print('Nome do aluno %s, ele tem %d anos e sua média é %.2f.' %(nome_aluno, idade_aluno, media_aluno))
print('Nome do aluno {}, ele tem {} anos e sua média é {}.'.format(nome_aluno, idade_aluno, media_aluno))
print(f'Nome do aluno {nome_aluno}, ele tem {idade_aluno} anos e sua média é {media_aluno:.2f}.')
