import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard 1 - Correlação e distribuição", layout="wide")


@st.cache_data
def load_data():
    return pd.read_csv("student_exam_performance.csv")


def prepare_numeric_columns(df: pd.DataFrame):
    numeric = df.select_dtypes(include=[np.number]).columns.tolist()
    numeric = [col for col in numeric if col != "student_id"]
    return numeric


df = load_data()
quantitative_columns = prepare_numeric_columns(df)

st.sidebar.title("Dashboard 1")
st.sidebar.caption("Correlação + distribuição das variáveis quantitativas")

selected_variable = st.sidebar.selectbox(
    "Selecione a variável quantitativa para o histograma",
    quantitative_columns,
    index=quantitative_columns.index("exam_score") if "exam_score" in quantitative_columns else 0,
)

score_min, score_max = st.sidebar.slider(
    "Excluir avaliações fora do intervalo:",
    min_value=0,
    max_value=100,
    value=(40, 100),
    step=1,
)

filtered_df = df[
    (df["exam_score"] >= score_min) & (df["exam_score"] <= score_max)
].copy()

st.title("Dashboard 1 — Correlação e distribuição das variáveis quantitativas")
st.caption("Base anonimizada: sem identificação dos alunos nos gráficos.")

st.subheader("Distribuição e correlação")

col1, col2 = st.columns(2)

with col1:
    corr_df = filtered_df[quantitative_columns].corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(9.5, 8))
    sns.heatmap(corr_df, cmap="coolwarm", vmin=-1, vmax=1, annot=False, linewidths=0.3, ax=ax)
    ax.set_title("Mapa de calor de correlação")
    st.pyplot(fig)

with col2:
    hist_values = filtered_df[selected_variable].dropna()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(hist_values, bins=25, kde=True, color="#4C78A8", ax=ax)
    ax.set_title(f"Histograma de {selected_variable}")
    ax.set_xlabel(selected_variable)
    ax.set_ylabel("Frequência")
    st.pyplot(fig)

st.markdown("### Interpretação do Dashboard 1")
st.write(
    "- O mapa de calor mostra como as variáveis quantitativas se relacionam entre si.\n"
    "- O histograma revela o comportamento da variável escolhida para o grupo filtrado.\n"
    "- O filtro de avaliação permite comparar subgrupos dentro do mesmo conjunto de dados.\n"
    "- Esta primeira etapa serve como base para a análise do próximo dashboard, focado em KPIs e métricas de gestão."
)
