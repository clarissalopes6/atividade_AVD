# Rascunho do Dashboard 1 - Laboratório de análise

## Objetivo
Explorar a distribuição das variáveis quantitativas e entender como elas se correlacionam entre si, com foco em identificar indicadores que influenciam o desempenho acadêmico.

## Público-alvo
Coordenação pedagógica e gestão escolar.

## Estrutura visual

- Painel lateral
  - seletor de variável quantitativa
  - slider para excluir notas fora de um intervalo desejado

- Bloco esquerdo
  - mapa de calor de correlação entre variáveis numéricas

- Bloco direito
  - histograma da variável selecionada

## Indicadores de interesse

- nota da prova (`exam_score`)
- desempenho anterior (`previous_exam_score`)
- GPA (`previous_gpa`)
- frequência (`attendance_percentage`)
- horas de estudo (`study_hours_per_day`)
- tempo de gestão (`time_management_score`)
- ansiedade (`exam_anxiety_level`)

## Observações da EDA

- A nota final tem relação forte com aspectos de estudo, organização e frequência.
- Existem diferenças visíveis por perfil de estudo e nível de comprometimento.
- O filtro de nota ajuda a isolar trechos do dataset para análise comparativa.
