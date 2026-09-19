---
tipo: curso
titulo: Pandas — Conhecendo a Biblioteca
plataforma: Alura
nivel: 1
iniciado: 2026-09-15
status: 🔄 Em andamento
tags:
  - pandas
  - python
  - data-analysis
  - alura
  - nivel-1
  - exploracao-dados
---

# 🐼 Pandas — Conhecendo a Biblioteca

> **Plataforma:** Alura
> **Nível:** 1 — Base concluída, iniciando exploração de dados
> **Status:** 🔄 Em andamento

---

## 🎯 O que este curso ensina

| Tópico | Status |
|---|---|
| Utilizar os principais recursos do Pandas em um projeto | ⬜ |
| Realizar análises exploratórias de dados (EDA) | ⬜ |
| Construir diferentes tipos de gráficos | ⬜ |
| Selecionar dados específicos (filtros e indexação) | ⬜ |
| Lidar com dados nulos | ⬜ |
| Remover linhas e colunas | ⬜ |
| Criar diversos tipos de colunas | ⬜ |

---

## 📚 Conceitos-chave aprendidos

> Preencha aqui conforme for avançando no curso.

### Estruturas de dados
- `DataFrame` — tabela bidimensional com rótulos
- `Series` — coluna única com índice

### Leitura de dados
```python
import pandas as pd

df = pd.read_csv('arquivo.csv')
df = pd.read_excel('arquivo.xlsx')
df.head()       # primeiras 5 linhas
df.tail()       # últimas 5 linhas
df.shape        # (linhas, colunas)
df.info()       # tipos e nulos
df.describe()   # estatísticas descritivas
```

### Seleção de dados
```python
df['coluna']                    # selecionar coluna
df[['col1', 'col2']]           # múltiplas colunas
df.loc[linha, 'coluna']        # por rótulo
df.iloc[0, 1]                  # por posição
df[df['col'] > 10]             # filtro condicional
```

### Dados nulos
```python
df.isnull().sum()              # contar nulos por coluna
df.dropna()                    # remover linhas com nulo
df.fillna(0)                   # preencher nulos com valor
df['col'].fillna(df['col'].mean())  # preencher com média
```

### Remover linhas e colunas
```python
df.drop('coluna', axis=1)      # remover coluna
df.drop(0, axis=0)             # remover linha pelo índice
df.drop_duplicates()           # remover duplicatas
```

### Criar colunas
```python
df['nova_col'] = df['col1'] + df['col2']          # operação
df['categoria'] = df['valor'].apply(lambda x: 'alto' if x > 100 else 'baixo')
df['col_str'] = df['col'].astype(str)             # mudar tipo
```

### Gráficos com Pandas
```python
df['coluna'].plot(kind='bar')      # gráfico de barras
df['coluna'].plot(kind='hist')     # histograma
df.plot(kind='scatter', x='a', y='b')  # scatter
df['coluna'].plot(kind='pie')      # pizza
```

---

## 💡 Aprendizados e insights

> Adicione aqui o que foi mais relevante ou surpreendente durante o curso.

---

## 🔗 Conexões com o vault

- Base de dados → [[Machine_Learning]] — Pandas é pré-requisito para ML
- Visualização → [[Visualizacao_de_Dados]] — gráficos com Pandas e Matplotlib
- Aplicado em → [[Analise_Desempenho_Alunos]] — projeto que já usa Pandas
- Aplicado em → [[Analise_Livros]] — web scraping + Pandas
- Próximo passo → [[Python_Projetos]] — criar novo projeto com Pandas
- Plataforma → [[Alura_Cursos]]

---

## ✅ Próximos passos após concluir

- [ ] Criar projeto prático usando Pandas com dataset real
- [ ] Registrar certificado em [[Certificados_Alura]]
- [ ] Atualizar [[Curriculo]] com a habilidade
- [ ] Atualizar [[LinkedIn_Estrategia]] — adicionar Pandas nas skills

---

← [[Alura_Cursos]] | [[04_Dados_IA]] | [[Hub_Central]]
