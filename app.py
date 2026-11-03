import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px

st.set_page_config(page_title="Dashboard de desempenho acadêmico", layout="wide")


@st.cache_data
def load_data():
    return pd.read_csv("student_exam_performance.csv")


def prepare_numeric_columns(df: pd.DataFrame):
    numeric = df.select_dtypes(include=[np.number]).columns.tolist()
    numeric = [col for col in numeric if col != "student_id"]
    return numeric


df = load_data()
quantitative_columns = prepare_numeric_columns(df)

with st.sidebar:
    st.title("Filtros")
    st.caption("Público-alvo: coordenação pedagógica")

    selected_variable = st.selectbox(
        "Selecione a variável quantitativa para o histograma",
        quantitative_columns,
        index=quantitative_columns.index("exam_score") if "exam_score" in quantitative_columns else 0,
    )

    score_min, score_max = st.slider(
        "Excluir avaliações fora do intervalo:",
        min_value=0,
        max_value=100,
        value=(40, 100),
        step=1,
    )

    dashboard_group = st.selectbox(
        "Agrupar no Dashboard 2:",
        ["gender", "school_type", "urban_rural", "performance_level"],
        index=0,
    )

filtered_df = df[
    (df["exam_score"] >= score_min) & (df["exam_score"] <= score_max)
].copy()

st.title("Dashboard de desempenho acadêmico")
st.caption("Base anonimizada: sem identificação individual nos gráficos e métricas.")

dashboard_1, dashboard_2 = st.tabs(["Dashboard 1", "Dashboard 2"])

with dashboard_1:
    st.subheader("Laboratório de análise")

    col1, col2 = st.columns(2)

    with col1:
        corr_df = filtered_df[quantitative_columns].corr(numeric_only=True)
        heatmap = px.imshow(
            corr_df,
            text_auto=True,
            aspect="auto",
            color_continuous_scale="RdBu_r",
            zmin=-1,
            zmax=1,
            title="Mapa de calor de correlação",
        )
        st.plotly_chart(heatmap, use_container_width=True)

    with col2:
        hist_values = filtered_df[selected_variable].dropna()
        hist_fig = px.histogram(
            hist_values,
            nbins=25,
            title=f"Histograma de {selected_variable}",
            labels={"value": selected_variable, "count": "Frequência"},
            color_discrete_sequence=["#4C78A8"],
        )
        st.plotly_chart(hist_fig, use_container_width=True)

    st.markdown("### Interpretação do Dashboard 1")
    st.write(
        "- O mapa de calor mostra como as variáveis quantitativas se relacionam entre si.\n"
        "- O histograma revela a distribuição da variável selecionada dentro do intervalo de notas escolhido.\n"
        "- A análise comparativa ajuda a identificar quais fatores têm maior relação com o desempenho acadêmico."
    )

with dashboard_2:
    st.subheader("KPIs e métricas de gestão escolar")

    pass_rate = (filtered_df["pass_status"] == "Pass").mean() * 100
    avg_score = filtered_df["exam_score"].mean()
    high_performance_share = (filtered_df["performance_level"] == "High").mean() * 100
    avg_study_hours_pass = filtered_df.loc[filtered_df["pass_status"] == "Pass", "study_hours_per_day"].mean()
    risk_share = (filtered_df["exam_score"] < 60).mean() * 100

    metric_cols = st.columns(5)
    metric_cols[0].metric("Taxa de aprovação", f"{pass_rate:.1f}%")
    metric_cols[1].metric("Nota média", f"{avg_score:.1f}")
    metric_cols[2].metric("Alunos em nível alto", f"{high_performance_share:.1f}%")
    metric_cols[3].metric("Horas de estudo (aprovados)", f"{avg_study_hours_pass:.2f}h")
    metric_cols[4].metric("Alunos em risco", f"{risk_share:.1f}%")

    st.markdown("### Visuais da gestão escolar")

    col_a, col_b = st.columns(2)

    with col_a:
        chart_group = filtered_df.groupby(dashboard_group, dropna=False)["exam_score"].mean().reset_index(name="nota_media")
        chart_group = chart_group.sort_values("nota_media", ascending=False)
        bar_chart = alt.Chart(chart_group).mark_bar(color="#F97316").encode(
            x=alt.X(f"{dashboard_group}:N", title="Grupo"),
            y=alt.Y("nota_media:Q", title="Média da nota"),
            tooltip=[f"{dashboard_group}:N", "nota_media:Q"],
        ).properties(title=f"Média de desempenho por {dashboard_group}")
        st.altair_chart(bar_chart, use_container_width=True)

    with col_b:
        scatter_data = filtered_df[["study_hours_per_day", "exam_score", "performance_level"]].dropna()
        scatter_chart = alt.Chart(scatter_data).mark_circle(opacity=0.7, size=50).encode(
            x=alt.X("study_hours_per_day:Q", title="Horas de estudo por dia"),
            y=alt.Y("exam_score:Q", title="Nota da prova"),
            color=alt.Color("performance_level:N", title="Nível"),
            tooltip=["study_hours_per_day:Q", "exam_score:Q", "performance_level:N"],
        ).properties(title="Relação entre estudo e nota")
        st.altair_chart(scatter_chart, use_container_width=True)

    box_chart = alt.Chart(filtered_df).mark_boxplot(extent="min-max").encode(
        x=alt.X("school_type:N", title="Tipo de escola"),
        y=alt.Y("exam_score:Q", title="Nota da prova")
    ).properties(title="Distribuição de notas por tipo de escola")
    st.altair_chart(box_chart, use_container_width=True)

    st.markdown("### Interpretação do Dashboard 2")
    st.write(
        "- A taxa de aprovação e o risco acadêmico ajudam a priorizar ações de apoio e recuperação.\n"
        "- A nota média e o nível de desempenho indicam a saúde geral do grupo e o nível de acompanhamento necessário.\n"
        "- O estudo por horas e o tipo de escola ajudam a relacionar contexto, esforço e desempenho."
    )
