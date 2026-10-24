# Revisão de arquitetura e segurança para produção — API_CARLOS

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-SECURITY-REVIEW-001 |
| **Projeto** | API_CARLOS |
| **Repositório** | [carlos-andrade/API_CARLOS](https://github.com/carlos-andrade/API_CARLOS) |
| **Tipo documental** | REVISÃO DE ARQUITETURA E SEGURANÇA |
| **Fase** | G2 — Arquitetura e autorização de produção |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | c37a7cd3a476a50311e2be393510678c69c5a71ca368b2f09f8d0330876e1789 |
| **Commit de referência (versão anterior)** | [ca7cd727d33957a3ef2218068d40795dded71291](https://github.com/carlos-andrade/API_CARLOS/commit/ca7cd727d33957a3ef2218068d40795dded71291) |
| **Data de criação** | 2026-10-24 |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Carlos Andrade |
| **Aprovador** | Pendente de aprovação explícita |
| **Origem** | Inspeção técnica da implementação publicada |
| **Autoridade superior** | [Norma GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Decisão técnica

**NO-GO para produção pública.** A arquitetura é uma base de desenvolvimento, mas a evidência atual não sustenta uma autorização de produção. Um CI verde não substitui revisão de segurança nem testes no ambiente de implantação.

## Evidências e bloqueios

1. A validação de URL resolve o hostname antes da ligação, mas não demonstra que o endereço validado é o mesmo usado pelo socket. É necessário testar DNS rebinding, redirecionamentos e destinos internos e demonstrar bloqueio de saída na rede.
2. A autenticação Bearer pode ficar desativada quando não há API_KEYS configurado. O ambiente de produção deve falhar ao arrancar sem autenticação e deve ter rotação segura de credenciais.
3. Não há evidência documentada de rate limiting, quotas, limites de concorrência, auditoria persistente, alertas, teste de penetração, staging ou rollback testado.
4. Devem ser validados limites de bytes em streaming, timeouts totais, permissões mínimas do workflow e endurecimento do container.

## Critérios de fecho

- [ ] Testes de segurança SSRF e de redirecionamentos aprovados.
- [ ] Controlo de egress e restrição de destinos demonstrados.
- [ ] Autenticação obrigatória em produção, quotas e rate limiting implementados.
- [ ] Logs, métricas, alertas e auditoria verificados sem expor segredos.
- [ ] Scan de dependências, configuração de container e permissões CI revistos.
- [ ] Testes de integração e revisão independente concluídos.
- [ ] Plano de implantação, resposta a incidentes e rollback testados.
- [ ] Decisão explícita do aprovador registada com data e evidências.

## Registo formal

- Arquitetura: aprovação pendente.
- Segurança para produção: não aprovada até ao fecho dos critérios acima.
- Aprovador designado: pendente.
- Data e referência da decisão: pendentes.

## Histórico

| Versão | Data | Alteração |
|---|---|---|
| 1.0.0 | 2026-10-24 | Registo inicial de revisão com decisão NO-GO e critérios de aprovação. |
