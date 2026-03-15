# Crypto Data Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue)
![ETL](https://img.shields.io/badge/focus-ETL-purple)
![Status](https://img.shields.io/badge/status-learning-orange)

Projeto criado para aprender **Engenharia de Dados na prática**.

O pipeline coleta dados de criptomoedas de uma API pública, transforma os dados e armazena um dataset histórico.

---

# Objetivo

Construir um pipeline de dados capaz de:

* coletar dados de uma API
* transformar dados em dataset estruturado
* armazenar dados com histórico
* evoluir para armazenamento em banco de dados
* automatizar o pipeline

---

# Tecnologias

* **Python**
* **Pandas**
* **Requests**
* **Pathlib**

API utilizada:

* **CoinGecko API**

---

# Pipeline (ETL)

O projeto segue a arquitetura clássica de **ETL**:

* **Extract** → coleta dados da API
* **Transform** → organiza e limpa os dados
* **Load** → salva os dados

O pipeline foi modularizado em:

* `extract`
* `transform`
* `load`
* `pipeline`

---

# Dataset

Colunas atuais:

* name
* symbol
* current_price
* market_cap
* total_volume
* collected_at

Cada execução adiciona novos dados, criando **histórico de preços**.

---

# Executar o projeto

Instalar dependências:

```
pip install -r requirements.txt
```

Executar pipeline:

```
python scripts/pipeline.py
```

---

# Progresso do Projeto

### Concluído

* [x] Consumo de API
* [x] Conversão JSON → DataFrame
* [x] Transformação com Pandas
* [x] Dataset em CSV
* [x] Histórico de preços
* [x] Pipeline modular (ETL)

### Próximos passos

* [ ] PostgreSQL
* [ ] Automação do pipeline
* [ ] Apache Airflow
* [ ] Dashboard analítico

---

# Status

Projeto em desenvolvimento focado em aprendizado prático de **engenharia de dados**.
