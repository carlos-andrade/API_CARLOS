# Roadmap — API_CARLOS

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-ROADMAP-001 |
| **Projeto** | API_CARLOS |
| **Repositório** | [carlos-andrade/API_CARLOS](https://github.com/carlos-andrade/API_CARLOS) |
| **Tipo documental** | ROADMAP |
| **Fase** | G0–R6 — Ciclo de vida do projeto |
| **Estado** | EM_REVISAO |
| **Versão** | 0.2.0 |
| **SHA-256 (conteúdo canónico)** | d3f3ebca870fe001f096574117644792debbc2cf1d30bc4bd5b88e8ef3edf03d |
| **Commit de referência (versão anterior)** | [8f8b6046ac2c94cb2b6d2f48d86ec12da8ce9023](https://github.com/carlos-andrade/API_CARLOS/commit/8f8b6046ac2c94cb2b6d2f48d86ec12da8ce9023) |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Carlos Andrade |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Estado do repositório e evidências de CI/revisão de segurança |
| **Autoridade superior** | [Norma GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Painel executivo

- **Missão:** disponibilizar uma API modular, versionada e auditável para extração de dados públicos, com contrato estável para consumo por outros repositórios.
- **Estado técnico:** núcleo API e controlos iniciais integrados; endurecimento de segurança em revisão.
- **CI mais recente na main:** PASS — run [40046560279](https://github.com/carlos-andrade/API_CARLOS/actions/runs/40046560279), commit `8f8b6046ac2c94cb2b6d2f48d86ec12da8ce9023`. Instalação, Ruff, verificação SHA-256 e pytest passaram.
- **Hashes canónicos:** verificação automática integrada no CI para os seis documentos nucleares; o registo de revisão de segurança está a ser incluído no conjunto documental de controlo.
- **Produção:** NO-GO. O código exige configuração de autenticação, allowlist, proxy de saída e auditoria persistente; ainda faltam evidências no ambiente-alvo e revisão independente.
- **Percentagem global:** não calculada. A conclusão ponderada exige baseline de critérios e evidências validadas; não atribuir percentagens sem essa baseline.

## Fases e gates

| Fase | Estado | Entregáveis/evidência | Critério de saída |
|---|---|---|---|
| G0 — Governação documental | EM_REVISAO | Cabeçalhos canónicos e verificador SHA-256 no CI | Todos os documentos sob verificação automatizada e hashes correspondentes |
| G1 — Viabilidade | PROPOSTO | Alternativas, custos, riscos e topologia de deployment | Decisão de viabilidade fundamentada |
| G2 — Arquitetura e segurança | EM_REVISAO | Contrato API, autenticação, allowlist, proxy de saída, limites, auditoria e revisão de segurança | Testes de segurança e parecer independente; decisão explícita do aprovador |
| I3 — Núcleo técnico | EM_REVISAO | FastAPI, extração JSON/CSV/XML/HTML, CI e testes | Testes unitários/integração verdes e contrato aprovado |
| I4 — Integração externa | NÃO_INICIADO | Cliente SDK e prova de consumo por repositório externo | Teste ponta a ponta reproduzível |
| O5 — Operação | NÃO_INICIADO | Staging, métricas, alertas, retenção, runbooks e rollback | Testes operacionais no ambiente-alvo |
| R6 — Release | BLOQUEADO | Release versionada, decisão formal e evidências pós-release | GO explícito e documentado após fechar todos os gates |

## Ações prioritárias

1. Fechar CI verde para a branch de endurecimento de segurança e integrar apenas após todos os checks passarem.
2. Provisionar proxy de saída controlado com bloqueio de redes privadas, loopback, link-local e metadata; provar DNS rebinding e egress deny-by-default.
3. Executar testes de integração de timeout, tamanho de resposta, redirects, autenticação, rate limiting e falhas de auditoria.
4. Fixar dependências, executar análise de vulnerabilidades e rever pinagem das GitHub Actions e imagem base.
5. Configurar staging, retenção/backup de auditoria, alertas e rollback; testar o runbook.
6. Obter revisão independente de arquitetura/segurança e registar decisão explícita do responsável autorizado.
7. Só então decidir a autorização de produção; não converter um CI verde em aprovação de segurança.

## Riscos e bloqueios

- SSRF/DNS rebinding depende de proxy de saída com política de rede demonstrável; validação DNS local não elimina TOCTOU.
- Rate limiting atual é local ao processo e requer gateway/armazenamento partilhado se houver várias réplicas.
- Persistência SQLite foi implementada, mas backups, permissões, retenção e monitorização têm de ser validados no ambiente real.
- Supply chain, staging, rollback e revisão independente ainda carecem de evidência.
- Aprovação formal de produção não pode ser atribuída sem decisão explícita do aprovador.

## Histórico

| Data | Alteração | Evidência |
|---|---|---|
| 2026-10-23 | Núcleo inicial e documentação integrados | PR #4 e CI inicial |
| 2026-10-24 | Hashes canónicos recalculados e verificador integrado | PR #5; CI run 40046560279 PASS |
| 2026-10-24 | Endurecimento de autenticação, proxy obrigatório, rate limiting, concorrência, timeout e auditoria persistente em desenvolvimento | Branch security/production-hardening-v1; CI pendente |
