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


# Tratamento de Exceções em Python

## Exercício 1 - Divisão com tratamento de erros


try:
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))

    resultado = numero_1 / numero_2
    print(f"Resultado: {resultado}")

except Exception as e:
    print(type(e), f"Erro: {e}")



## Exercício 2 - Busca em dicionário

idades = {
    'Júlia': 16,
    'Carol': 23,
    'Alberto': 19,
    'Roberta': 17
}

try:
    nome = input("Digite um nome: ")
    idade = idades[nome]

except KeyError:
    print("Nome não encontrado")

else:
    print(f"Idade: {idade}")


## Exercício 3 - Conversão de lista para float

def converte_lista(lista):
    try:
        nova_lista = [float(item) for item in lista]

    except Exception as e:
        print(type(e), f"Erro: {e}")

    else:
        return nova_lista

    finally:
        print("Fim da execução da função")


## Exercício 4 - Agrupamento e soma de listas


def soma_listas(lista1, lista2):
    try:
        if len(lista1) != len(lista2):
            raise IndexError(
                "A quantidade de elementos em cada lista é diferente."
            )

        resultado = [
            (lista1[i], lista2[i], lista1[i] + lista2[i])
            for i in range(len(lista1))
        ]

    except Exception as e:
        print(type(e), f"Erro: {e}")

    else:
        return resultado


## Exercício 5 - Correção automática de provas


gabarito = ['D', 'A', 'B', 'C', 'A']

def corretor(testes):
    notas = []

    try:
        for teste in testes:
            nota = 0

            for i in range(len(teste)):

                if teste[i] not in ['A', 'B', 'C', 'D']:
                    raise ValueError(
                        f"A alternativa {teste[i]} não é válida."
                    )

                if teste[i] == gabarito[i]:
                    nota += 1

            notas.append(nota)

    except Exception as e:
        print(e)

    else:
        return notas



## Exercício 6 - Validação de texto

def avalia_texto(texto):

    for palavra in texto:

        if (
            ',' in palavra or
            '.' in palavra or
            '!' in palavra or
            '?' in palavra
        ):
            raise ValueError(
                f'O texto apresenta pontuação na palavra "{palavra}".'
            )

    return "Texto já tratado!"


## Exercício 7 - Divisão entre colunas


def divide_colunas(lista_1, lista_2):

    try:

        if len(lista_1) != len(lista_2):
            raise ValueError(
                "As listas precisam ter o mesmo tamanho."
            )

        resultado = [
            round(a / b, 2)
            for a, b in zip(lista_1, lista_2)
        ]

    except ValueError as e:
        print(e)

    except ZeroDivisionError as e:
        print(
            f"{e}: A segunda lista não pode conter zero."
        )

    else:
        return resultado



'''
Aprendizados

- Uso de `try`, `except`, `else` e `finally`
- Criação de exceções personalizadas com `raise`
- Validação de entradas
- Tratamento de erros comuns em aplicações Python
- Desenvolvimento de código mais seguro e robusto
'''