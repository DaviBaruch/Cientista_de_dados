# ☁️ Capítulo 2 — Google Cloud Storage e BigQuery

> **Curso:** Fundamentos de Nuvem  
> **Capítulo:** 2  
> **Tema principal:** Armazenamento em nuvem, Cloud Storage e integração com BigQuery

---

## 🎯 Objetivo do capítulo

Compreender como utilizar o **Google Cloud Storage** para armazenar arquivos na nuvem e como integrar esses dados ao **BigQuery** para transformá-los em dados estruturados e realizar consultas utilizando **SQL**.

---

# 🧩 1. Visão geral do fluxo

O capítulo apresenta um fluxo de trabalho para armazenar, processar e analisar dados na nuvem:

```text
Definição do problema
        ↓
Coleta e ingestão de dados na nuvem
        ↓
Análise e exploração de dados
        ↓
Processamento e transformação
        ↓
Modelagem
        ↓
Visualização
        ↓
Monitoramento
```

Durante as primeiras etapas, os dados podem estar em formatos estruturados ou não estruturados.

Exemplos de arquivos utilizados:

- CSV
- JSON

---

# ☁️ 2. Google Cloud Storage

O **Google Cloud Storage (GCS)** é um serviço de armazenamento de objetos na nuvem.

Ele permite armazenar arquivos e dados de diferentes formatos sem depender de um armazenamento físico local.

### Conceitos importantes

| Conceito | Significado |
| --- | --- |
| **Bucket** | Contêiner utilizado para armazenar objetos |
| **Objeto** | Arquivo armazenado dentro de um bucket |
| **Classe de armazenamento** | Define características de armazenamento e acesso |
| **Localização** | Região ou conjunto de regiões onde os dados são armazenados |

---

# 🪣 3. Bucket

O **bucket** funciona como um contêiner para os arquivos armazenados no Cloud Storage.

Exemplo:

```text
Bucket
│
├── pedidos.csv
├── clientes.csv
├── produtos.json
└── dados/
    ├── pedidos_2026.csv
    └── clientes_2026.json
```

### Regras de nomenclatura

O nome do bucket precisa seguir as regras definidas pelo Google Cloud.

Por isso, ao criar um bucket, é necessário escolher um nome válido e adequado para identificar o projeto ou conjunto de dados armazenado.

---

# 📍 4. Localização do armazenamento

Ao criar um bucket, é necessário escolher sua localização.

A localização influencia aspectos como:

- Latência
- Custos
- Disponibilidade
- Proximidade dos usuários ou sistemas

> **Ideia principal:** a localização dos dados é uma decisão técnica que pode afetar desempenho e custos.

---

# 💾 5. Classe de armazenamento

O Google Cloud Storage possui diferentes classes de armazenamento.

Neste capítulo, é utilizada a classe:

**Standard**

A classe Standard é adequada para dados que precisam ser acessados com frequência.

```text
Acesso frequente
      ↓
   Standard
```

A escolha da classe deve considerar a frequência de acesso aos dados e os custos envolvidos.

---

# 🔐 6. Segurança e prevenção de acesso público

Ao configurar um bucket, é importante impedir que os arquivos sejam disponibilizados publicamente sem necessidade.

Uma das configurações abordadas é a:

**Prevenção do acesso público**

### Objetivo

Evitar que objetos armazenados no bucket possam ser acessados publicamente de forma indevida.

> **Princípio importante:** os dados devem ser acessíveis somente por usuários ou serviços que realmente possuem permissão.

---

# 📤 7. Upload de arquivos

Depois da criação e configuração do bucket, é possível fazer upload dos arquivos.

Neste capítulo são utilizados principalmente:

- `.csv`
- `.json`

Os arquivos podem ser organizados utilizando pastas.

Exemplo:

```text
bucket-pedidos/
│
├── csv/
│   ├── pedidos.csv
│   └── clientes.csv
│
└── json/
    └── produtos.json
```

Essa organização facilita o gerenciamento dos dados.

---

# 🧱 8. BigQuery

O **BigQuery** é uma plataforma de análise de dados que permite executar consultas SQL sobre grandes volumes de dados.

Neste capítulo, ele é utilizado em conjunto com o Cloud Storage.

```text
Arquivos CSV / JSON
        ↓
Google Cloud Storage
        ↓
BigQuery
        ↓
Dataset
        ↓
Tabelas
        ↓
SQL
        ↓
Análise dos dados
```

---

# 🗂️ 9. Dataset no BigQuery

Antes de criar as tabelas, é necessário criar um **dataset**.

O dataset funciona como um agrupador lógico das tabelas dentro de um projeto do BigQuery.

```text
Projeto
│
└── Dataset
    │
    ├── pedidos
    ├── clientes
    └── produtos
```

---

# 📊 10. Tabelas no BigQuery

Depois de criar o dataset, os dados podem ser carregados ou conectados para serem utilizados como tabelas.

Uma das opções abordadas é utilizar arquivos armazenados no Cloud Storage como fonte dos dados.

### Detecção automática de esquema

O BigQuery pode utilizar a **detecção automática de esquema** para identificar:

- Nome das colunas
- Tipos de dados
- Estrutura dos registros

```text
Arquivo CSV
    ↓
Detecção automática de esquema
    ↓
Colunas + tipos de dados
    ↓
Tabela no BigQuery
```

---

# 🔄 11. Dados não estruturados → dados estruturados

Uma das ideias centrais do capítulo é transformar arquivos armazenados na nuvem em estruturas que podem ser analisadas.

Exemplo:

```text
pedidos.csv
    ↓
Cloud Storage
    ↓
BigQuery
    ↓
Tabela estruturada
    ↓
Consulta SQL
```

Isso facilita a exploração e análise dos dados.

---

# 🧮 12. Importação de dados CSV

Ao importar um arquivo CSV para o BigQuery, é importante verificar as configurações de mapeamento dos campos.

Alguns pontos que precisam ser observados:

- Nome das colunas
- Tipo dos dados
- Separador utilizado no arquivo
- Cabeçalho
- Correspondência entre campos e colunas

Uma configuração incorreta pode fazer com que os dados sejam interpretados de maneira errada.

---

# 🐍 13. SQL no BigQuery

Depois que os dados estão disponíveis no BigQuery, podemos utilizar **SQL** para consultar as tabelas.

Exemplo:

```sql
SELECT *
FROM `projeto.dataset.pedidos`;
```

Essa estrutura mostra três elementos importantes:

```text
projeto
   ↓
dataset
   ↓
tabela
```

### Estrutura completa

```text
`ID_DO_PROJETO.DATASET.TABELA`
```

Esses elementos são fundamentais para localizar corretamente uma tabela dentro do BigQuery.

---

# 🔎 14. Validando os dados

As consultas SQL podem ser utilizadas para verificar se os dados foram importados corretamente.

Exemplo:

```sql
SELECT *
FROM `projeto.dataset.pedidos`
LIMIT 10;
```

O `LIMIT` permite limitar a quantidade de registros retornados.

Também podemos analisar os diferentes **status dos pedidos**.

Exemplo:

```sql
SELECT status, COUNT(*) AS quantidade
FROM `projeto.dataset.pedidos`
GROUP BY status;
```

Essa consulta permite observar quantos pedidos existem em cada status.

---

# 🔗 15. Conectando diferentes fontes de dados

O BigQuery pode trabalhar com diferentes fontes de dados.

Isso proporciona maior flexibilidade para projetos de análise.

Neste capítulo, o fluxo principal é:

```text
Cloud Storage
      ↓
   BigQuery
      ↓
     SQL
      ↓
   Análise
```

A integração entre serviços permite separar responsabilidades:

- **Cloud Storage:** armazenamento dos arquivos
- **BigQuery:** processamento e análise
- **SQL:** consulta e exploração dos dados

---

# 🧠 16. Conceitos principais para memorizar

| Conceito | Significado |
| --- | --- |
| **Cloud Storage** | Serviço de armazenamento de objetos na nuvem |
| **Bucket** | Contêiner onde os objetos são armazenados |
| **Objeto** | Arquivo armazenado em um bucket |
| **Standard** | Classe adequada para dados acessados com frequência |
| **Localização** | Região ou conjunto de regiões onde os dados ficam armazenados |
| **Acesso público** | Permissão que pode tornar dados acessíveis publicamente |
| **BigQuery** | Plataforma de análise de dados do Google Cloud |
| **Dataset** | Agrupador lógico de tabelas no BigQuery |
| **Tabela** | Estrutura organizada de dados consultável por SQL |
| **Esquema (Schema)** | Estrutura que define colunas e tipos de dados |
| **Detecção automática de esquema** | Recurso que identifica automaticamente a estrutura dos dados |
| **SQL** | Linguagem utilizada para consultar e analisar dados |
| **CSV** | Formato de arquivo baseado em valores separados por delimitadores |
| **JSON** | Formato estruturado para representação de dados |

---

# 🧪 17. Exercício prático do capítulo

### Cloud Storage

- [ ] Criar um bucket
- [ ] Utilizar um nome válido para o bucket
- [ ] Configurar a localização
- [ ] Definir a classe de armazenamento como Standard
- [ ] Ativar a prevenção do acesso público
- [ ] Fazer upload dos arquivos CSV
- [ ] Fazer upload dos arquivos JSON
- [ ] Organizar os arquivos em pastas quando necessário

### BigQuery

- [ ] Criar um projeto ou utilizar um projeto existente
- [ ] Criar um dataset
- [ ] Criar tabelas
- [ ] Conectar as tabelas aos arquivos armazenados no Cloud Storage
- [ ] Utilizar a detecção automática de esquema
- [ ] Verificar o mapeamento dos campos
- [ ] Importar os dados CSV

### SQL

- [ ] Executar uma consulta para validar os dados
- [ ] Identificar os status dos pedidos
- [ ] Contar a quantidade de pedidos por status
- [ ] Verificar se os tipos das colunas foram identificados corretamente

---

# 🔗 Conexões

**Conceitos relacionados:**

- [[Fundamentos de Nuvem]]
- [[Cloud Computing]]
- [[Google Cloud]]
- [[Cloud Storage]]
- [[BigQuery]]
- [[Banco de Dados]]
- [[SQL]]
- [[Dataset]]
- [[Data Pipeline]]
- [[Dados Estruturados]]
- [[Dados Não Estruturados]]
- [[Big Data]]
- [[Data Analytics]]

---

# 💡 Insight pessoal

> O Cloud Storage e o BigQuery possuem funções diferentes, mas trabalham muito bem juntos: o Cloud Storage pode armazenar os arquivos brutos, enquanto o BigQuery permite estruturar, consultar e analisar esses dados utilizando SQL.

---

# 📌 Resumo em uma frase

**O Google Cloud Storage permite armazenar e organizar arquivos na nuvem, enquanto o BigQuery possibilita transformar esses dados em estruturas analisáveis e realizar consultas SQL para extrair informações.**
