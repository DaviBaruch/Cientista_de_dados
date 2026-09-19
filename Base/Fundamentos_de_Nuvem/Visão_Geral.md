---
tipo: curso
titulo: Fundamentos de Nuvem — Construindo a Base
plataforma: Alura
instrutora: Letícia Pires
repositorio: https://github.com/alura-cursos/FundamentosNuvem
tags: [alura, cloud, gcp, bigquery, cloud-storage, curso]
---

# ☁️ Fundamentos de Nuvem — Construindo a Base

> **Plataforma:** Alura · **Instrutora:** Letícia Pires
> **Repositório do curso:** https://github.com/alura-cursos/FundamentosNuvem
> **Carga horária:** ~8h · **Categoria:** Data Science / Cloud

---

## 🎯 O que o curso ensina

- O que é computação em nuvem e por que usá-la
- Diferenciar **IaaS, PaaS e SaaS** com exemplos reais
- Avaliar plataformas: **AWS, Google Cloud, Azure**
- Acessar e armazenar dados com **Google Cloud Storage** (buckets)
- Analisar dados na nuvem com **BigQuery** e **Google Colab**
- Modelos de custo e segurança na nuvem (camada gratuita)

---

## 📖 Ementa (ordem das aulas)

1. Apresentação
2. Preparando o ambiente
3. **Entendendo o dataset** ← usa um dataset de e-commerce/agendamentos parecido com o padrão Olist
4. O que é computação em nuvem?
5. Modelos de serviço (IaaS/PaaS/SaaS)
6. Vantagens da nuvem
7. Pipeline do projeto
8. Compactação de dados e extração
9. Escalabilidade de dados na gestão de agendamentos
10. Projeto prático: pipeline de dados
11. Revisão do que foi aprendido

---

## 🧠 Conceitos-chave

| Conceito | Resumo |
|---|---|
| **Computação em nuvem** | Uso sob demanda de servidores, armazenamento e serviços via internet, sem gerenciar infraestrutura física própria |
| **IaaS** | Infraestrutura como serviço — você gerencia SO e aplicações (ex.: máquinas virtuais) |
| **PaaS** | Plataforma como serviço — você só cuida do código/dados, a infra é gerenciada |
| **SaaS** | Software como serviço — aplicação pronta para uso (ex.: Gmail, BigQuery em modo consulta) |
| **Bucket (Cloud Storage)** | "Pasta" na nuvem para guardar arquivos (CSV, JSON, imagens) de forma durável e escalável |
| **BigQuery** | Data warehouse serverless do Google Cloud — permite rodar SQL sobre grandes volumes de dados sem gerenciar servidor |
| **Pipeline de dados** | Sequência automatizada: ingestão → armazenamento → transformação → análise |
| **Camada gratuita (free tier)** | Limite de uso mensal sem custo, usado no curso para praticar sem gastar |

---

## 🔗 Conexão prática com os datasets Olist

O curso usa um projeto de **pipeline de dados com um dataset de pedidos/agendamentos**. A estrutura é equivalente à do dataset público da **Olist** (pedidos, clientes, produtos, pagamentos) que estou usando para estudo — ver [[Olist_Visao_Geral]].

**Como aplicaria o fluxo do curso nos dados da Olist:**

1. **Ingestão** — subir os 9 CSVs da Olist para um bucket no Google Cloud Storage
2. **Compactação** — zipar os arquivos grandes (ex.: `olist_geolocation_dataset.csv`, com ~1 milhão de linhas) antes do upload, como ensinado em "compactação de dados e extração"
3. **Carga no BigQuery** — criar uma tabela por CSV, ou um dataset único `olist` com 9 tabelas relacionadas por `order_id`, `customer_id`, `product_id`, `seller_id`
4. **Consulta com SQL** — usar BigQuery para responder perguntas como "qual estado mais compra" ou "qual categoria mais vendida" (ver [[Olist_Insights]])
5. **Escalabilidade** — o volume da Olist (~100 mil pedidos, ~1 milhão de geolocalizações) é um bom exemplo prático de "por que não abrir isso tudo em Excel", que é exatamente o argumento central do curso a favor da nuvem

---

## ✅ Status

> 📌 Curso identificado e mapeado. Ainda não iniciado no Drive/Obsidian — próximo passo: assistir e ir preenchendo os conceitos com anotações próprias.

---

← [[02_Cursos]] | [[Alura_Cursos]] | [[Cloud_Computing]] | [[Hub_Central]]
