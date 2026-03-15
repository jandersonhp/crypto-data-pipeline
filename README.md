# Crypto Data Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-learning-orange)
![Project](https://img.shields.io/badge/project-data_pipeline-green)
![ETL](https://img.shields.io/badge/focus-ETL-purple)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Pipeline de dados criado com o objetivo de aprender **Engenharia de Dados na prática**.

O projeto simula o fluxo real de trabalho de um engenheiro de dados:

coletar dados → transformar dados → armazenar dados → automatizar pipelines → disponibilizar dados para análise.

Os dados utilizados vêm de uma API pública de criptomoedas.

---

# Objetivo do Projeto

Construir um pipeline de dados capaz de:

* coletar dados de criptomoedas de uma API
* transformar os dados em um dataset estruturado
* armazenar dados em banco de dados
* automatizar a coleta de dados
* disponibilizar os dados para análise e dashboards

Este projeto funciona como um **laboratório prático de engenharia de dados**.

---

# Tecnologias Utilizadas

Durante o desenvolvimento do projeto são utilizadas ferramentas comuns no ecossistema de dados.

## Linguagem

Python

Uma das linguagens mais utilizadas em engenharia de dados.

---

## Consumo de API

Biblioteca utilizada:

requests

Responsável por realizar requisições HTTP e consumir dados de APIs externas.

API utilizada no projeto:

CoinGecko API

---

## Transformação de Dados

Biblioteca utilizada:

Pandas

Pandas permite trabalhar com estruturas chamadas **DataFrames**, que funcionam como tabelas dentro do Python.

Essa biblioteca é amplamente utilizada em:

* ETL
* pipelines de dados
* análise de dados
* preparação de datasets

---

## Manipulação de caminhos

Biblioteca utilizada:

pathlib

Permite trabalhar com caminhos de arquivos de forma segura e portátil entre sistemas operacionais.

---

# Conceito Central

O projeto segue o padrão clássico de pipelines de dados:

ETL

Extract
Transform
Load

---

# Extract (Extração)

Nesta etapa o pipeline coleta dados de uma API externa.

Os dados coletados incluem informações como:

* nome da criptomoeda
* símbolo
* preço atual
* market cap
* volume de negociação

---

# Transform (Transformação)

Após a coleta, os dados passam por transformações:

* conversão do JSON da API para DataFrame
* seleção das colunas relevantes
* organização do dataset
* adição de timestamp de coleta

---

# Load (Carga)

Os dados transformados são armazenados para uso posterior.

Inicialmente os dados são exportados para **CSV**, mas posteriormente serão armazenados em **banco de dados**.

---

# Estrutura do Dataset

O dataset atual contém as seguintes colunas:

* name
* symbol
* current_price
* market_cap
* total_volume
* collected_at

A coluna **collected_at** registra o momento da coleta, permitindo criar **dados históricos de preços**.

---

# Checklist do Projeto

## Etapas concluídas

* [x] Criar projeto em Python
* [x] Consumir API de criptomoedas
* [x] Converter resposta JSON em estrutura Python
* [x] Criar DataFrame com Pandas
* [x] Explorar colunas retornadas pela API
* [x] Selecionar colunas relevantes
* [x] Adicionar coluna `collected_at`
* [x] Exportar dataset para CSV
* [x] Utilizar `pathlib` para caminhos de arquivos

---

## Próximas etapas

### Melhorias no Pipeline

* [ ] Persistir dados sem sobrescrever CSV
* [ ] Criar histórico de preços
* [ ] Criar sistema de logs
* [ ] Separar código em funções
* [ ] Modularizar pipeline

---

### Banco de Dados

* [ ] Instalar PostgreSQL
* [ ] Criar banco de dados
* [ ] Criar tabela para criptomoedas
* [ ] Inserir dados no banco usando Python
* [ ] Criar queries analíticas

---

### Automação

* [ ] Automatizar execução do pipeline
* [ ] Criar agendamento de coleta
* [ ] Orquestrar pipeline

Ferramenta planejada:

Apache Airflow

---

### Visualização de Dados

* [ ] Conectar banco a ferramenta de BI
* [ ] Criar dashboard de preços
* [ ] Criar ranking por market cap
* [ ] Visualizar volume de negociação
* [ ] Analisar evolução de preços

Ferramentas possíveis:

* Power BI
* Metabase

---

# Melhorias Futuras

Possíveis evoluções do projeto:

* Docker
* pipelines CI/CD
* monitoramento de pipelines
* validação de qualidade de dados
* ingestão incremental
* data warehouse
* processamento em batch
* processamento em streaming

---

# Status do Projeto

Projeto em desenvolvimento com foco em aprendizado prático de **engenharia de dados**.
