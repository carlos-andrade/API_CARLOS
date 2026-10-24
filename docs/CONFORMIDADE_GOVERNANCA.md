# Registo de conformidade documental — API_CARLOS

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-GOV-INSPECTION-001 |
| **Projeto** | API_CARLOS |
| **Repositório** | [carlos-andrade/API_CARLOS](https://github.com/carlos-andrade/API_CARLOS) |
| **Tipo documental** | REGISTO DE INSPEÇÃO DE CONFORMIDADE |
| **Fase** | G0–G2 — Governação documental, núcleo e segurança |
| **Estado** | EM_REVISAO |
| **Versão** | 0.3.0 |
| **SHA-256 (conteúdo canónico)** | 2d7f14be13ad8231167586893f736f7c7d50d92cdc9a7b86bc2373230cb3e08f |
| **Commit de referência (versão anterior)** | [8f8b6046ac2c94cb2b6d2f48d86ec12da8ce9023](https://github.com/carlos-andrade/API_CARLOS/commit/8f8b6046ac2c94cb2b6d2f48d86ec12da8ce9023) |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Carlos Andrade |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Inspeção documental, CI e revisão de segurança |
| **Autoridade superior** | [Norma GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo e autoridade

Regista o estado de adoção documental, integridade canónica e segurança do repositório. A norma obrigatória é [GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md). O roadmap respeita [GOV-CARTA-ROADMAP-001](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md) e [GOV-STD-STATUS-001](https://github.com/carlos-andrade/GOVERNANCA/blob/main/standards/status-e-percentual-de-conclusao.md).

## Resultado verificado

- **Hashes canónicos:** verificação automática PASS para os seis documentos nucleares e para a revisão de arquitetura/segurança na branch de hardening, usando Python hashlib e a normalização especificada.
- **CI final da main:** PASS no commit `a41297403239cae9062423a1cb6baae003dcbff8`; [run 40048867801](https://github.com/carlos-andrade/API_CARLOS/actions/runs/40048867801). Instalação, Ruff, hashes canónicos, pytest, build Squid e teste runtime de egress passaram.
- **Hardening de segurança:** PR #6 integrado na main no commit `1e61e4dc5d89d9ecf59702288d0081824fc7a908`; adiciona autenticação fail-closed em produção, allowlist, proxy explícito obrigatório, limites, rate limiting local, concorrência limitada, auditoria SQLite e endurecimento de container.
- **Integridade documental:** hashes dos sete documentos sob controlo passaram no CI do commit indicado.
- **Proxy de saída:** PR #8 propõe serviço Squid em rede isolada com ACLs para loopback, link-local, redes privadas e endereços reservados; a validação em runtime ainda não está demonstrada.
- **Conformidade global:** parcial e em revisão. O CI verde não prova segurança de rede, operação ou aprovação formal de produção.

## Pendências de segurança e aprovação

1. Repetir a execução no ambiente-alvo real e provar bloqueio de loopback, redes privadas, link-local, metadata endpoints, DNS rebinding e egress deny-by-default.
2. Executar testes de integração de timeout, limite de bytes, redirects, autenticação, rate limiting e falhas do armazenamento de auditoria.
3. Rever supply chain: dependências fixadas e scan de vulnerabilidades, pinagem das GitHub Actions e imagem base.
4. Validar volume SQLite, permissões, backups, retenção, alertas, staging e rollback.
5. Obter revisão independente de arquitetura e segurança e registar decisão explícita do aprovador autorizado.
6. Manter NO-GO para produção até fecho dos critérios; não declarar APROVADO sem evidência.

## Critérios de aceitação

- [x] Cabeçalhos Markdown com tabela canónica de metadados.
- [x] Verificação SHA-256 independente automatizada no CI.
- [x] CI da main passou lint, hashes e testes no commit indicado.
- [ ] Proxy anti-SSRF e política de egress testados no ambiente-alvo.
- [ ] Supply chain, staging, alertas e rollback validados.
- [ ] Revisão independente concluída.
- [ ] Aprovação formal registada antes de promover para APROVADO ou autorizar produção.

## Histórico

| Versão | Data | Alteração |
|---|---|---|
| 0.1.0 | 2026-10-23 | Registo inicial de adoção e inspeção. |
| 0.2.0 | 2026-10-24 | Atualiza evidências SHA/CI e regista hardening e bloqueios de produção. |
| 0.3.0 | 2026-10-24 | Confirma integração do hardening e CI verde na main; mantém NO-GO até validação operacional e revisão independente. |
