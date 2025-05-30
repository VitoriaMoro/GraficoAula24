import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Análise: Redes Sociais vs. Produtividade')

try:
    df = pd.read_csv("social_media_vs_productivity.csv")

    x_column = 'daily_social_media_time'
    y_column = 'actual_productivity_score'

    df_cleaned = df.dropna(subset=[x_column, y_column])

    st.write(f"Visualizando a relação entre '{x_column}' e '{y_column}'.")
    st.write(f"Número de pontos de dados: {len(df_cleaned)}")

    # Criar o gráfico de dispersão
    fig, ax = plt.subplots(figsize=(10, 6)) # Usar subplots para melhor integração com Streamlit
    sns.scatterplot(data=df_cleaned, x=x_column, y=y_column, alpha=0.5, ax=ax)
    ax.set_title('Tempo Diário em Redes Sociais vs. Pontuação de Produtividade Real', fontsize=16)
    ax.set_xlabel('Tempo Diário em Redes Sociais (horas)', fontsize=12)
    ax.set_ylabel('Pontuação de Produtividade Real', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    
    st.pyplot(fig)

except FileNotFoundError:
    st.error("Arquivo 'social_media_vs_productivity.csv' não encontrado. Por favor, faça o upload do arquivo.")
except Exception as e:
    st.error(f"Ocorreu um erro ao processar os dados: {e}")


