# Capítulo 4 – ETL com BigQuery e Cloud Storage

> Curso: Fundamentos de Nuvem  
> Capítulo: 4  
> Tema principal: Transformação e ciclo ETL

---

## 🎯 Objetivo
Realizar um ciclo completo de ETL usando BigQuery, pandas e Cloud Storage.

---

## 🧩 Conceitos
- Criação de coluna de atraso (diferença de datas)
- Transformação de dados com pandas
- Carregamento de DataFrame para BigQuery (`load_table_from_dataframe`)
- Exportação de DataFrame para CSV
- Upload de CSV para Cloud Storage
- Ciclo ETL: Extract → Transform → Load

---

## 🔄 Como funciona
1. Execute consulta no BigQuery e converta para DataFrame.  
2. Use pandas para criar nova coluna de atraso.  
3. Carregue o DataFrame transformado de volta ao BigQuery.  
4. Exporte os dados para CSV.  
5. Faça upload do CSV para o Cloud Storage.  

---

## 🧠 Conceitos principais para memorizar

| Conceito | Significado |
|---|---|
| ETL | Processo de extrair, transformar e carregar dados |
| pandas | Biblioteca Python para manipulação de dados |
| load_table_from_dataframe | Função para enviar DataFrame ao BigQuery |
| CSV | Formato de exportação de dados |
| Cloud Storage | Armazenamento final dos dados |

---

## 🧪 Exercício prático
- [ ] Criar coluna de atraso em DataFrame  
- [ ] Carregar DataFrame transformado no BigQuery  
- [ ] Exportar DataFrame para CSV  
- [ ] Fazer upload do CSV para GCS  

---

## 🔗 Conexões
- [[ETL]]  
- [[Pipeline de Dados]]  
- [[BigQuery]]  
- [[Cloud Storage]]  
- [[Pandas]]  

---

## 💡 Insight pessoal
> O ciclo ETL garante que os dados sejam limpos, transformados e armazenados de forma organizada para análises futuras.

---

## 📌 Resumo em uma frase
O ETL integra BigQuery, pandas e Cloud Storage para transformar e organizar dados de ponta a ponta.
