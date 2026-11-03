# Atividade AVD - Etapa 1: Dashboard 1

Este repositório está seguindo a ideia da atividade de dois dashboards, mas nesta primeira entrega foi implementada somente a etapa do Dashboard 1: correlação + distribuição das variáveis quantitativas.

## Links

- Repositório público: https://github.com/clarissalopes6/atividade_AVD
- App publicado (Streamlit): https://clarissalopes6-atividade-avd.streamlit.app
- App local: http://localhost:8501

## Conteúdo da primeira entrega

- Notebook com a EDA: `ENTREGA_AVD_Prática_EDA (1).ipynb`
- Dataset: `student_exam_performance.csv`
- Aplicativo principal: `app.py`
- Rascunhos de entrega: `entregas/`
- Prompt orientador: `prompts/`

## Dashboard 1

O app atual contempla:

- painel lateral com seletor de variável quantitativa
- filtro por intervalo de avaliação
- mapa de calor de correlação
- histograma da variável selecionada
- foco na análise exploratória do desempenho acadêmico

## Próxima etapa

A próxima parte da atividade será adicionar o Dashboard 2, com KPIs e métricas de gestão escolar.

## Como rodar localmente

```bash
streamlit run app.py
```
