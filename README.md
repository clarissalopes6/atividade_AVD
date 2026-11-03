# Atividade AVD - Etapa 3: publicação e validação

Aplicação de análise do desempenho acadêmico, construída com Streamlit a partir da EDA do dataset `student_exam_performance.csv`. A etapa 3 contempla a publicação do app, a verificação do acesso público e a organização dos entregáveis no repositório.

## Links

- Repositório: [clarissalopes6/atividade_AVD](https://github.com/clarissalopes6/atividade_AVD)
- Aplicação publicada: [Dashboard de desempenho acadêmico](https://clarissalopes6-atividade-avd.streamlit.app/)

## Aplicação

O app está organizado em duas abas:

- **Dashboard 1 - Laboratório de análise:** mapa de correlação e histograma de uma variável quantitativa, com filtro por intervalo de notas.
- **Dashboard 2 - KPIs e gestão escolar:** taxa de aprovação, nota média, percentual em nível alto, horas de estudo entre aprovados, percentual em risco e visualizações comparativas.

## Entregáveis do repositório

- EDA: [notebook/ENTREGA_AVD_Prática_EDA.ipynb](notebook/ENTREGA_AVD_Prática_EDA.ipynb)
- Dataset: [student_exam_performance.csv](student_exam_performance.csv)
- Aplicação Streamlit: [app.py](app.py)
- Rascunhos dos dashboards: [entregas/](entregas/)
- Documentação de prompts e declaração de uso de IA: [prompts/](prompts/)
- Dependências: [requirements.txt](requirements.txt)

## Execução local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
