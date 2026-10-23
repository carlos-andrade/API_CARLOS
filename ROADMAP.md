# Roadmap — API_CARLOS

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-ROADMAP-001 |
| **Projeto** | API_CARLOS |
| **Repositório** | [carlos-andrade/API_CARLOS](https://github.com/carlos-andrade/API_CARLOS) |
| **Tipo documental** | ROADMAP |
| **Fase** | F0–R6 — Ciclo de vida do projeto |
| **Estado** | EM_REVISAO |
| **Versão** | 0.1.0 |
| **SHA-256 (conteúdo canónico)** | 3653ee6f4a04c63b692f9795dbfc560c43c67be0a537e2168875511e87290f51 |
| **Commit de referência (versão anterior)** | [5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b](https://github.com/carlos-andrade/API_CARLOS/commit/5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b) |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Carlos Andrade |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Artefacto do projeto API_CARLOS; atualização de conformidade documental |
| **Autoridade superior** | [Norma GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Painel executivo

- **Missão:** API modular para extração auditável de dados públicos e de acesso livre.
- **Requisito transversal:** invocação por outros repositórios através de contrato estável, versionado e autenticado.
- **Estado da implementação:** núcleo inicial implementado e integrado em `main`; validação CI e aprovação de segurança ainda pendentes de evidência.
- **Próximo marco:** corrigir/confirmar CI, inspecionar a conformidade documental e rever âmbito/arquitetura.
- **Bloqueio principal:** execução CI ainda não confirmada após correção de empacotamento; arquitetura, contrato e controlos de produção carecem de aprovação.
- **Percentual de conclusão:** não calculado. Não há baseline de critérios ponderados validada; não inventar percentuais.

## Fases e gates

| Fase | Estado | Entregáveis | Critério de saída |
|---|---|---|---|
| F0 — Âmbito e governação | EM_REVISAO | README, âmbito, roadmap e mapa de governação | Âmbito aprovado; adoção local e evidências registadas |
| G1 — Viabilidade | PROPOSTO | Alternativas técnicas, custos, riscos e implantação | Decisões de viabilidade justificadas |
| G2 — Arquitetura | PROPOSTO | Contrato OpenAPI, modelo de ameaças, arquitetura e decisões tecnológicas | Revisão de arquitetura e segurança aprovada |
| I3 — Núcleo e conectores | EM_REVISAO | Serviço REST e extração inicial JSON/CSV/XML/HTML implementados; cobertura ainda limitada | CI verde, testes revistos e segurança mínima aprovada |
| I4 — Integração externa | NÃO_INICIADO | Exemplo de cliente, integração com outro repositório e autenticação | Teste de ponta a ponta reproduzível |
| O5 — Operação | NÃO_INICIADO | CI, métricas, logs, alertas, recuperação e documentação operacional | Testes operacionais e de segurança aprovados |
| R6 — Release | NÃO_INICIADO | Versão, notas de release, rollback e decisão formal | Autorização explícita e evidências pós-release |

## Ações prioritárias

1. Rever os documentos nesta branch e aprovar formalmente o âmbito.
2. Inspecionar requisitos locais da GOVERNANCA aplicáveis e registar conformidade ou desvios.
3. Definir OpenAPI para submissão de extração, estado, resultado, erros e saúde.
4. Escolher stack, autenticação, fila e persistência após análise de alternativas.
5. Implementar um conector simples e um cliente de outro repositório como prova de interoperabilidade.
6. Automatizar testes de contrato, segurança e integração antes de ampliar o catálogo de conectores.

## Riscos e bloqueios

- Alterações e limites das fontes externas.
- Restrições de licenciamento, privacidade e redistribuição.
- SSRF e conteúdo externo malicioso.
- Dependência operacional dos repositórios clientes em relação ao serviço central.
- Custos de processamento de documentos e navegação automatizada.
- Arquitetura e decisões tecnológicas ainda pendentes.

## Evidências e estado

A implementação inicial foi integrada em `main` pelo merge commit [5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b](https://github.com/carlos-andrade/API_CARLOS/commit/5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b). O primeiro CI reportado falhou no empacotamento Hatchling; foi preparada correção em PR #3, mas o sucesso da nova execução ainda não está confirmado. Não há evidência de implantação pública nem de conformidade integral.

## Histórico

| Data | Alteração | Evidência |
|---|---|---|
| 2026-10-23 | Roadmap inicial criado com fases, dependências e critérios de saída | Branch docs/escopo-interoperabilidade-v1; aguarda revisão |
