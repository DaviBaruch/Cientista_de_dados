# ☁️ Capítulo 1 — Fundamentos de Nuvem

> **Curso:** Fundamentos de Nuvem  
> **Capítulo:** 1  
> **Tema principal:** Dados, escalabilidade e computação em nuvem

---

## 🎯 Objetivo do capítulo

Compreender como o crescimento do volume de dados influencia a infraestrutura necessária para armazená-los e processá-los, além de entender como a computação em nuvem oferece recursos para lidar com problemas de **escalabilidade, armazenamento, processamento e análise de dados**.

---

## 1. Dataset e dados interconectados

O capítulo apresenta um cenário baseado em um **dataset de pedidos**, composto por diferentes arquivos/tabelas que possuem relações entre si.

### O que analisar

- Volume de dados
- Quantidade de registros
- Quantidade de tabelas
- Estrutura das tabelas
- Colunas e tipos de dados
- Chaves primárias
- Chaves estrangeiras
- Relacionamentos entre tabelas
- Possíveis inconsistências ou dados faltantes

### Por que os dados são interconectados?

Em um projeto real, os dados normalmente são distribuídos em diferentes tabelas para evitar duplicação e facilitar a organização.

Exemplo:

```text
Clientes
   │
   └── Pedidos
          │
          └── Produtos
                 │
                 └── Categorias
```

Essa estrutura permite combinar diferentes informações para responder perguntas de negócio.

---

## 2. Volume de dados e escalabilidade

À medida que uma empresa cresce, a quantidade de dados também aumenta.

Um sistema que funciona bem com poucos milhares de registros pode apresentar dificuldades quando passa a lidar com milhões ou bilhões.

### Escalabilidade

**Escalabilidade** é a capacidade de uma infraestrutura aumentar ou diminuir seus recursos de acordo com a demanda.

Existem dois conceitos importantes:

### Escalabilidade vertical

Aumentar a capacidade de uma máquina existente.

Exemplo:

```text
Servidor
8 GB RAM
   ↓
32 GB RAM
```

### Escalabilidade horizontal

Adicionar novas máquinas ao sistema.

```text
Servidor
   ↓
Servidor 1 + Servidor 2 + Servidor 3
```

---

## 3. Infraestrutura On-Premise

**On-premise** significa manter a infraestrutura física dentro da própria organização.

A empresa é responsável por:

- Servidores
- Armazenamento
- Rede
- Energia
- Refrigeração
- Manutenção
- Segurança
- Atualizações
- Expansão da infraestrutura

### Principais desafios

- Alto investimento inicial
- Manutenção dos equipamentos
- Limitação física
- Dificuldade para aumentar capacidade rapidamente
- Recursos podem ficar ociosos
- Necessidade de planejamento antecipado

### Problema de escalabilidade

Se a empresa prevê que precisará de mais servidores no futuro, precisa adquirir e instalar essa infraestrutura antes ou durante o crescimento.

Isso pode gerar:

> **Custo + tempo + capacidade ociosa**

---

# ☁️ 4. Computação em Nuvem

A computação em nuvem permite utilizar recursos computacionais através de provedores especializados.

Em vez de a empresa precisar possuir toda a infraestrutura física, ela pode contratar recursos conforme a necessidade.

### Principais vantagens

- Elasticidade
- Escalabilidade
- Pagamento conforme utilização
- Maior agilidade
- Redução da necessidade de infraestrutura física própria
- Possibilidade de aumentar ou diminuir recursos rapidamente

---

# 🧩 5. Modelos de serviço em nuvem

Os principais modelos apresentados são:

- **IaaS**
- **PaaS**
- **SaaS**

Eles representam diferentes níveis de responsabilidade entre o cliente e o provedor de nuvem.

---

## 🏗️ IaaS — Infrastructure as a Service

**Infraestrutura como Serviço**

O provedor oferece recursos básicos de infraestrutura.

Exemplos:

- Máquinas virtuais
- Armazenamento
- Rede
- Servidores

O usuário ainda possui bastante controle sobre o ambiente.

### Analogia

É como **alugar uma casa vazia**.

A estrutura básica existe, mas você ainda precisa cuidar de várias coisas internamente.

---

## ⚙️ PaaS — Platform as a Service

**Plataforma como Serviço**

O provedor fornece uma plataforma pronta para desenvolvimento e execução de aplicações.

O desenvolvedor se preocupa mais com a aplicação e menos com a infraestrutura.

### Analogia

É como **alugar uma cozinha equipada**.

A infraestrutura necessária já está preparada para você trabalhar.

---

## 💻 SaaS — Software as a Service

**Software como Serviço**

É um software pronto utilizado diretamente pelo usuário.

Exemplos:

- E-mail
- Aplicativos online
- Sistemas empresariais
- Ferramentas de colaboração

### Analogia

É como **ir a um restaurante**.

Você utiliza o serviço pronto sem precisar se preocupar com a cozinha ou com a infraestrutura.

---

# 🔄 6. Pipeline de dados

Um **pipeline de dados** representa o fluxo pelo qual os dados passam desde sua origem até serem utilizados para análise ou tomada de decisão.

Uma estrutura simplificada:

```text
Fonte de dados
      ↓
Ingestão
      ↓
Armazenamento
      ↓
Processamento
      ↓
Transformação
      ↓
Análise
      ↓
Visualização
      ↓
Tomada de decisão
```

---

## 📦 7. Pipeline aplicado aos atrasos nas entregas

O pipeline pode ser utilizado para analisar informações relacionadas às entregas.

### Exemplo

```text
Pedidos
   ↓
Coleta dos dados
   ↓
Armazenamento na nuvem
   ↓
Tratamento dos dados
   ↓
Integração das tabelas
   ↓
Cálculo dos atrasos
   ↓
Análise
   ↓
Dashboard
```

A partir disso, podemos identificar:

- Quantidade de pedidos atrasados
- Percentual de atrasos
- Regiões com maior número de atrasos
- Produtos com maior ocorrência de problemas
- Transportadoras com maior índice de atraso
- Tempo médio de entrega
- Padrões de atraso

---

# ☁️ 8. Como a nuvem ajuda o pipeline

A computação em nuvem pode fornecer recursos para diferentes etapas do pipeline.

### Armazenamento

Permite armazenar grandes volumes de dados sem depender exclusivamente de servidores físicos próprios.

### Processamento

Pode fornecer recursos computacionais maiores quando o volume de dados aumenta.

### Escalabilidade

Os recursos podem acompanhar o crescimento da quantidade de dados e da demanda.

### Análise

Os dados processados podem alimentar ferramentas de análise e dashboards.

---

# 🧠 9. Conceitos principais para memorizar

| Conceito | Significado |
|---|---|
| **Cloud Computing** | Uso de recursos computacionais através da nuvem |
| **Escalabilidade** | Capacidade de aumentar ou diminuir recursos |
| **Elasticidade** | Adaptação dos recursos à demanda |
| **On-Premise** | Infraestrutura mantida pela própria organização |
| **IaaS** | Infraestrutura como serviço |
| **PaaS** | Plataforma como serviço |
| **SaaS** | Software como serviço |
| **Pipeline** | Fluxo de processamento dos dados |
| **Ingestão** | Entrada/coleta dos dados |
| **Processamento** | Tratamento e transformação dos dados |
| **Dashboard** | Visualização das informações para análise |

---

# 🧪 10. Exercício prático do capítulo

### Dataset

- [ ] Baixar o dataset de pedidos
- [ ] Extrair os arquivos
- [ ] Identificar todas as tabelas
- [ ] Identificar os relacionamentos
- [ ] Verificar o volume de dados
- [ ] Analisar a estrutura das tabelas
- [ ] Analisar o conteúdo

### Infraestrutura

- [ ] Identificar problemas de uma infraestrutura on-premise
- [ ] Explicar por que a escalabilidade é necessária
- [ ] Comparar escalabilidade vertical e horizontal

### Computação em nuvem

- [ ] Explicar IaaS
- [ ] Explicar PaaS
- [ ] Explicar SaaS
- [ ] Relacionar cada modelo às suas respectivas analogias

### Pipeline

- [ ] Identificar a origem dos dados
- [ ] Definir a etapa de ingestão
- [ ] Definir o armazenamento
- [ ] Definir o processamento
- [ ] Definir a análise
- [ ] Criar uma proposta de análise dos atrasos nas entregas

---

# 🔗 Conexões

**Conceitos relacionados:**

- [[Dados]]
- [[Banco de Dados]]
- [[SQL]]
- [[Engenharia de Dados]]
- [[Pipeline de Dados]]
- [[Big Data]]
- [[Computação em Nuvem]]
- [[Escalabilidade]]
- [[IaaS]]
- [[PaaS]]
- [[SaaS]]
- [[Data Analytics]]
- [[Dashboard]]

---

# 💡 Insight pessoal

> A computação em nuvem não significa apenas "guardar arquivos na internet". Ela fornece infraestrutura, plataformas e softwares que permitem construir sistemas capazes de acompanhar o crescimento da quantidade de dados e da demanda.

---

# 📌 Resumo em uma frase

**A nuvem permite construir uma infraestrutura mais escalável e flexível para armazenar, processar e analisar grandes volumes de dados por meio de diferentes modelos de serviço, como IaaS, PaaS e SaaS.**
