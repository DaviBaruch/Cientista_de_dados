cadastro = ("Júlia", 23, "São Paulo", "SP", "Python para DS 1")


print(cadastro[0]) # imprime Júlia
print(cadastro[-1]) # imprime Python para DS 1

nome, idade, cidade, estado, turma = cadastro

print(f'A estudante {nome} tem {idade} anos e mora em {cidade}-{estado}. Ela está matriculada na turma de {turma}.')

#Listas de tuplas

estudantes = ["João", "Maria", "José", "Pedro", "Clara", "Ana", "Lucas"]

from random import randint

def gera_codigo():
    return randint(0, 9999)

codigo_estudantes = []
for i in range(len(estudantes)):
    codigo_estudantes.append((estudantes[i], estudantes[i][0] + str(gera_codigo())))

print(codigo_estudantes)

#List comprehension

#Formato padrão
# [expressão for item in lista]

#teste