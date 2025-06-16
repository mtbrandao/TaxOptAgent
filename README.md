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
