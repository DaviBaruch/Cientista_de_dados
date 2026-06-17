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

nomes = ["João", "Maria", "José", "Pedro", "Clara", "Ana", "Lucas"]

medias = [7.5, 8.0, 9.0, 7.0, 8.5, 9.5, 8.0]

estudantes = list(zip(nomes, medias))
print(estudantes)

candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 8.0]

#A zip() é uma função embutida do Python que recebe um ou mais iteráveis (lista, string, dict, etc.) e retorna-os como um iterador de tuplas onde cada elemento dos iteráveis são pareados. Ela é útil para fazer iterações simultâneas em várias listas.

id = [1, 2, 3, 4, 5]
regiao = ["Norte", "Nordeste", "Sudeste", "Centro-Oeste", "Sul"]

mapa = list(zip(id, regiao))
print(mapa)


#Para uma pessoa cientista de dados, essa função pode auxiliar a parear 2 listas distintas em um único objeto zip, podendo este ser transformado em uma lista de tuplas (formato ideal para gerar um índice de mais de um nível que será explorado em alguns dos cursos da formação) ou em um dicionário passando o objeto zip para a função dict().

#Agora, se as listas de entrada têm comprimentos diferentes, a saída contém o mesmo número de tuplas que a lista de menor comprimento e os elementos restantes dos outros iteráveis serão ignorados. Por exemplo:

codigos = ["1000", "1001", "1002", "1003", "1004", "1005"]
frutas = ["maçã", "uva", "banana", "laranja"]

mercadorias = list(zip(codigos, frutas))
print(mercadorias)

#Criar uma lista da situação dos estudantes em que caso sua média seja maior ou igual a 6 receberá o valor "Aprovado" e caso contrário receberá o valor "Reprovado"

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

situacao = ["Aprovado(a)" if notas >= 6.0 else "Reprovado(a)" for notas in medias]
print(situacao)

#para gerar listas de listas:

#[expressão for item in lista de listas]

cadastro = [x for x in [nomes, notas, medias, situacao]]
print(cadastro)

#Dict comprehension

lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')], [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]], [9.0, 7.3, 5.8, 6.7, 8.5], ['Aprovado(a)', 'Aprovado(a)', 'Reprovado(a)', 'Aprovado(a)', 'Aprovado(a)']]

coluna = [ "Notas", "Média Final", "Situação"]
cadastro_dict = {coluna[i]: lista_completa[1+i] for i in range(len(coluna))}
print(cadastro_dict)
#Saída:

#{'Notas': [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]], 'Média Final': [9.0, 7.3, 5.8, 6.7, 8.5], 'Situação': ['Aprovado(a)', 'Aprovado(a)', 'Reprovado(a)', 'Aprovado(a)', 'Aprovado(a)']}

cadastro_dict["Estudantes"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]
print(cadastro)

#saída:
#[[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
#[[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]], [9.0, 7.3, 5.8, 6.7, 8.5], ['Aprovado(a)', 'Aprovado(a)', 'Reprovado(a)', 'Aprovado(a)', 'Aprovado(a)']]


#Try Expect: Key Error

nota = {'João': 8.5, 'Maria': 7.0, 'José': 5.5, 'Cláudia': 6.7, 'Ana': 8.5, 'Pedro': 7.0, 'Lucas': 8.0, 'Carla': 9.0}

nome = input("Digite o nome do aluno(a): ")

#Simulando error de chave
resultado = notas[nome]
print(resultado)

#Tratando o erro de chave
try:
    resultado = nota[nome]
    print(resultado)
except KeyError:
    print("Aluno(a) não encontrado.")
    