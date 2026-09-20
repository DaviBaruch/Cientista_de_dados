# 📊 Capítulo 1 — Introdução ao Pandas

## 🎯 Objetivo

Conhecer a biblioteca **Pandas** e entender como utilizá-la para carregar, visualizar e manipular dados em formato de tabela.

---

## 🐼 O que é Pandas?

**Pandas** é uma biblioteca Python de código aberto voltada para **análise e manipulação de dados**.

Ela permite trabalhar com dados provenientes de diferentes fontes, como:

- CSV
- Excel
- JSON
- HTML
- Bancos de dados SQL

O principal objetivo é facilitar tarefas como:

- Carregar dados
- Visualizar dados
- Selecionar informações
- Filtrar dados
- Ordenar dados
- Agregar dados
- Transformar dados

> **Pandas = ferramenta para trabalhar com dados de forma prática usando Python.**

---

## 🗂️ DataFrame

O **DataFrame** é uma das principais estruturas do Pandas.

Ele representa os dados em formato de **tabela**, sendo semelhante a uma planilha do Excel.

Exemplo:

| Nome | Idade | Cidade |
|---|---:|---|
| João | 20 | São Paulo |
| Maria | 22 | Campinas |
| Pedro | 19 | Santos |

Nesse caso:

- Cada **linha** representa um registro.
- Cada **coluna** representa uma informação.
- O conjunto da tabela pode ser representado por um **DataFrame**.

### 🔑 Ideia principal

```text
Arquivo / Banco de dados
        ↓
      Pandas
        ↓
    DataFrame
        ↓
Análise e manipulação