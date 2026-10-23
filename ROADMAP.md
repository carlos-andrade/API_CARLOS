# Roadmap — API_CARLOS

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-ROADMAP-001 |
| **Projeto** | API_CARLOS |
| **Tipo documental** | ROADMAP |
| **Fase atual** | F0 — Definição de âmbito e governação |
| **Estado global** | EM_REVISAO |
| **Versão** | 0.1.0 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Carlos Andrade |
| **Padrão de referência** | https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md |

## Painel executivo

- **Missão:** API modular para extração auditável de dados públicos e de acesso livre.
- **Requisito transversal:** invocação por outros repositórios através de contrato estável, versionado e autenticado.
- **Estado da implementação:** não iniciada; esta branch contém documentação proposta.
- **Próximo marco:** revisão e aprovação formal de âmbito e arquitetura.
- **Bloqueio principal:** decisões de arquitetura, contrato OpenAPI e requisitos de segurança ainda não aprovados.
- **Percentual de conclusão:** não calculado. Não há baseline de critérios ponderados validada; não inventar percentuais.

## Fases e gates

| Fase | Estado | Entregáveis | Critério de saída |
|---|---|---|---|
| F0 — Âmbito e governação | EM_REVISAO | README, âmbito, roadmap e mapa de governação | Âmbito aprovado; adoção local e evidências registadas |
| G1 — Viabilidade | PROPOSTO | Alternativas técnicas, custos, riscos e implantação | Decisões de viabilidade justificadas |
| G2 — Arquitetura | PROPOSTO | Contrato OpenAPI, modelo de ameaças, arquitetura e decisões tecnológicas | Revisão de arquitetura e segurança aprovada |
| I3 — Núcleo e conectores | NÃO_INICIADO | Serviço REST, registo de conectores, orquestrador e primeiros conectores | Testes unitários e de contrato aprovados |
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

A evidência inicial do repositório é o commit 79566388f765463947e2cb29d2c89097f6f744a7, que continha apenas LICENSE. Esta branch propõe documentação; não comprova execução de testes, serviço implantado, endpoint funcional ou conformidade integral.

## Histórico

| Data | Alteração | Evidência |
|---|---|---|
| 2026-10-23 | Roadmap inicial criado com fases, dependências e critérios de saída | Branch docs/escopo-interoperabilidade-v1; aguarda revisão |
