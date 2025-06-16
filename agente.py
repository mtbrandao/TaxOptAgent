# Bloco 1: Importações
# Estamos trazendo as ferramentas que instalamos para dentro do nosso código.
import pandas as pd
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# Bloco 2: Configuração Inicial
# Carrega as informações do nosso "cofre" (.env) para o programa.
print("Carregando configurações...")
load_dotenv()

# Carrega as planilhas para o nosso "Especialista" (Pandas).
print("Carregando arquivos CSV...")
try:
    df_cabecalho = pd.read_csv('202401_NFs_Cabecalho.csv')
    df_itens = pd.read_csv('202401_NFs_Itens.csv')
    print("✓ Arquivos carregados com sucesso!")
except FileNotFoundError:
    print("ERRO: Arquivos CSV não encontrados. Verifique se estão na mesma pasta.")
    exit()

# Bloco 3: Criando o "Cérebro" do Agente
# Estamos definindo que o cérebro do nosso Gerente será a IA da OpenAI.
# temperature=0 significa: "Seja preciso e direto, não criativo".
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0)

# Bloco 4: Montando o Agente (O "Gerente")
# Aqui, a mágica acontece! Estamos criando o agente e entregando as ferramentas para ele.
# - llm: O cérebro que ele vai usar.
# - [df_cabecalho, df_itens]: As duas planilhas que ele pode consultar. Ele as chamará de df1 e df2.
# - verbose=True: Isso fará o agente "pensar em voz alta" no terminal. É ÓTIMO para aprender!
print("Criando o agente... 🤖")
agent_executor = create_pandas_dataframe_agent(
    llm,
    [df_cabecalho, df_itens],
    verbose=True,
    allow_dangerous_code=True
)
print("✓ Agente pronto para trabalhar!")
print("-" * 50)


# Bloco 5: A Interface de Conversa
# Um loop infinito para que possamos fazer várias perguntas sem reiniciar o programa.
while True:
    pergunta_usuario = input("Faça sua pergunta sobre as notas fiscais (ou digite 'sair'): ")
    
    if pergunta_usuario.lower() == 'sair':
        print("Até logo!")
        break
    
    # Enviando a pergunta para o agente e esperando a resposta.
    resposta = agent_executor.invoke(pergunta_usuario)
    
    # Imprimindo a resposta final do agente.
    print("\nResposta Final:")
    print(resposta['output'])
    print("-" * 50)