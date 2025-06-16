# TaxOptAgent

O projeto Tax Opt Agent consiste no desenvolvimento de uma ferramenta gerencial de apoio à gestão empresarial, baseada em agentes autônomos de Inteligência Artificial, voltada para otimizar o planejamento tributário e oferecer subsídios para análise estratégica do mix de produtos, podendo ser aplicada tanto para produtos quanto serviços. 

A proposta é cruzar informações de custos, tributos e preços de venda para indicar automaticamente a margem líquida de cada item, considerando os regimes tributários vigentes (Simples Nacional, Lucro Presumido e Lucro Real).

O objetivo é oferecer uma visão conjunta de indicadores imprescindíveis de forma rápida e prática para gestores, contadores e consultores, especialmente diante do novo cenário tributário nacional.


## Clonando e usando

Clone o repositório
```javascript
git clone https://github.com/mtbrandao/TaxOptAgent.git
```

Crie um ambiente virtual do Python
```javascript
cd TaxOptAgent/
python -m venv TaxOptAgent
```

Ative o ambiente virtual
```javascript
source TaxOptAgent/bin/activate
```

Instale as dependencias
```javascript
pip install langchain langchain-openai pandas python-dotenv
pip install langchain-experimental tabulate langchain-google-genai
pip install --upgrade langchain langchain-google-genai google-generativeai
```


Exporte sua chave API do Google SDK
```javascript
export GOOGLE_API_KEY="sua_chave_api"

```

Chame o agente com o comando:
```javascript
python agente.py 
```
O agente deverá estar ativo e pronto para uso
```javascript
Carregando configurações...
Carregando arquivos CSV...
✓ Arquivos carregados com sucesso!
Criando o agente... 🤖
✓ Agente pronto para trabalhar!
--------------------------------------------------
Faça sua pergunta sobre as notas fiscais (ou digite 'sair'): 

```

## Sobre o Repositório

Este repositório faz parte do projeto **"Agentes Autônomos de IA para Gestão Tributária e Análise Estratégica"**, desenvolvido pelo grupo **Tax Opt Agent**.

O trabalho está sendo realizado no contexto do curso  
**"Agentes Autônomos com Redes Generativas"**, promovido pelo **Instituto I2A2** (Instituto de Inteligência Artificial Aplicada).

Aqui estão reunidos os códigos, modelos e documentos produzidos ao longo do projeto, com foco em soluções baseadas em IA para apoio à tomada de decisão na área tributária.

## Integrantes do grupo Tax Opt Agent

- Aldair Silva de Jesus  
- Anejéssica de Brito Figueiredo  
- Antonio Wilson Cruz Ferreira Filho  
- Cristiane Coradini Chiorato  
- Fábio Augusto Ribeiro  
- Marcelo Toscani Brandão  
- Mariana Oliveira Ribeiro  
- Vinicius Pereira
