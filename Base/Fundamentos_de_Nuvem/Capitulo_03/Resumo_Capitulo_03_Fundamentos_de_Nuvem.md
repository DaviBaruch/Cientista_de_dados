# Capítulo 3 – Integração Google Colab ↔ Google Cloud

> Curso: Fundamentos de Nuvem  
> Capítulo: 3  
> Tema principal: Autenticação e conexão Colab → GCP

---

## 🎯 Objetivo
Entender como conectar o Google Colab ao Google Cloud Storage e ao BigQuery para manipulação de dados na nuvem.

---

## 🧩 Conceitos
- Autenticação com `google.colab.auth`
- Uso dos módulos `google.colab`, `google.cloud.storage`, `google.cloud.bigquery`
- Conexão do Colab ao Cloud Storage (dados brutos)
- Configuração do cliente BigQuery
- Execução de consultas SQL no Python
- Conversão de resultados em DataFrame com pandas

---

## 🔄 Como funciona
1. Autentique o Colab com as credenciais do GCP.  
2. Importe os módulos necessários (`colab`, `storage`, `bigquery`).  
3. Conecte o Colab ao Cloud Storage para acessar dados brutos.  
4. Configure o cliente do BigQuery.  
5. Execute consultas SQL diretamente no Python.  
6. Converta os resultados em DataFrame para análise.

---

## 🧠 Conceitos principais para memorizar

| Conceito | Significado |
|---|---|
| Autenticação | Permite acesso seguro ao GCP via Colab |
| Cloud Storage | Armazenamento de dados brutos |
| BigQuery | Banco de dados analítico |
| SQL | Linguagem para consultas |
| DataFrame | Estrutura tabular do pandas |

---

## 🧪 Exercício prático
- [ ] Autenticar Colab com GCP  
- [ ] Criar conexão com Cloud Storage  
- [ ] Configurar cliente BigQuery  
- [ ] Executar consulta SQL simples  
- [ ] Converter resultado em DataFrame  

---

## 🔗 Conexões
- [[Cloud Storage]]  
- [[BigQuery]]  
- [[SQL]]  
- [[Python]]  
- [[Pandas]]  

---

## 💡 Insight pessoal
> A integração Colab ↔ GCP transforma o notebook em uma ferramenta poderosa para análise de dados em escala.

---

## 📌 Resumo em uma frase
Conectar o Colab ao GCP permite manipular dados brutos e consultar BigQuery diretamente com Python.
