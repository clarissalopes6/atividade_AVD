# Declaração de Uso de IA

**Nome:** Clarissa Lopes  
**Data:** 2026-11-02

## Ferramenta

GitHub Copilot (modelo MAI-Code-1.1-Flash)

## Prompt usado

### Prompt 1 — revisão da estrutura do dashboard

**Contexto**

Estou revisando a estrutura do dashboard em Streamlit para verificar se ele segue a proposta da atividade. O objetivo é confirmar se a organização da interface, os filtros e as visualizações estão coerentes com a EDA e com os requisitos da parte 1.

**Entrada**

Tenho o arquivo `app.py` com a estrutura do Dashboard 1 e o dataset `student_exam_performance.csv`. A análise deve manter foco em correlação, distribuição e filtros de avaliação.

**Restrições**

- revisar a lógica, não reescrever tudo do zero;
- priorizar correção e reforço do que já existe;
- manter o uso de dados anonimizados;
- validar se não há inconsistência com o dataset real.

**Formato de saída**

Checklist de pontos que estão corretos, pontos que precisam ajustes e sugestões de correção objetiva.

### Prompt 2 — verificação de widgets e interação

**Contexto**

Preciso verificar se os widgets do painel lateral e as visualizações do Dashboard 1 respondem corretamente. Vou checar se o seletor de variável e o slider de intervalo estão funcionando como esperado.

**Entrada**

O app já está implementado e quero validar sua interação no ambiente local.

**Restrições**

- validar que os widgets aparecem e respondem;
- checar se o filtro do intervalo funciona;
- garantir que a seleção de variável muda a visualização sem erro;
- evitar qualquer dado sensível na interface.

**Formato de saída**

Resumo de validação com evidência do comportamento dos widgets e do app em execução.

### Prompt 3 — correção de erros e refinamento do código

**Contexto**

Estou avaliando o código do app para detectar erros de sintaxe, warnings de compatibilidade e pequenos ajustes de qualidade antes de avançar para a próxima etapa do projeto.

**Entrada**

Tenho o código do `app.py` e quero uma revisão focada em correção, não em recomeçar a implementação.

**Restrições**

- corrigir apenas o que for necessário;
- manter a ideia original do dashboard;
- preservar o uso do dataset real;
- reforçar a clareza do código e a estabilidade do app.

**Formato de saída**

Lista de correções aplicadas, justificativa das mudanças e confirmação de que o app continua funcional.

## O que foi aceito, modificado ou rejeitado e por quê

- **Aceito:** a estrutura do Dashboard 1, a lógica de filtro por nota, a análise coerente com o dataset e a negociação da anonimização no app.
- **Modificado:** ajustes de compatibilidade e validação para garantir funcionamento estável do código sem alterar a proposta do dashboard.
- **Rejeitado:** qualquer sugestão que fosse apenas para recriar o projeto de zero ou que partisse de premissas sem suporte no dataset.
