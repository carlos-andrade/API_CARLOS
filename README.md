# API_CARLOS — API de extração de dados públicos

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-README-001 |
| **Projeto** | API_CARLOS |
| **Repositório** | [carlos-andrade/API_CARLOS](https://github.com/carlos-andrade/API_CARLOS) |
| **Tipo documental** | ÍNDICE DO PROJETO |
| **Fase** | G2 — Endurecimento de segurança |
| **Estado** | EM_REVISAO |
| **Versão** | 0.2.0 |
| **SHA-256 (conteúdo canónico)** | PENDENTE DE RECÁLCULO |
| **Commit de referência (versão anterior)** | [5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b](https://github.com/carlos-andrade/API_CARLOS/commit/5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b) |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Carlos Andrade |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Artefacto do projeto API_CARLOS; atualização de conformidade documental |
| **Autoridade superior** | [Norma GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Missão

Desenvolver uma API modular para descobrir, extrair, normalizar, validar e disponibilizar dados públicos e de acesso livre na Internet, desde fontes simples até fontes tecnicamente complexas. A solução deverá ser invocável por outros repositórios, aplicações, pipelines e agentes de software através de contratos estáveis e documentados.

## Requisitos centrais

1. Interface de integração uniforme, independente do método interno de extração.
2. Priorizar APIs oficiais e conjuntos de dados estruturados quando adequados.
3. Conectores para HTTP, JSON, CSV, XML, RSS, HTML e PDF; métodos avançados por módulos.
4. Proveniência, data da recolha, versão do conector, estado de execução e validação.
5. Invocação por repositórios externos sem copiar o código interno.
6. Contratos versionados, documentação OpenAPI e exemplos de integração.
7. Segurança, quotas, observabilidade, retentativas controladas e validação de dados.
8. Respeito por leis, licenças, direitos de autor, privacidade e controlos de acesso.

## Integração com outros repositórios

A modalidade de integração é uma API HTTP REST versionada, destinada a ser publicada por HTTPS. Os repositórios clientes poderão enviar pedidos autenticados, indicar fontes ou tarefas de extração e receber dados normalizados com proveniência. O contrato público será o OpenAPI, sem necessidade de copiar o código interno da API.

## Estrutura técnica

- `app/main.py`: aplicação FastAPI, readiness e auditoria de pedidos.
- `app/extraction.py`: extração HTTP com timeout total, redirects bloqueados e limite de bytes.
- `app/security.py`: validação de URLs, allowlist, autenticação Bearer em tempo constante e rate limiting local.
- `app/config.py`: configuração e validação fail-closed das pré-condições de produção.
- `app/audit.py`: trilho de auditoria SQLite persistente.
- `proxy/squid.conf` e `proxy/Dockerfile`: proxy de saída com bloqueio de redes privadas e reserved ranges; a validação runtime ainda é obrigatória.
- `tests/`: testes de API, segurança e persistência de auditoria.
- `Dockerfile` e `compose.yaml`: container não-root, filesystem read-only, volume de auditoria, healthcheck e limites de recursos.
- `scripts/check_canonical_hashes.py`: verificação independente dos hashes canónicos no CI.
- `.github/workflows/ci.yml`: pipeline de Ruff, hashes e testes.

## Endpoints iniciais

- `GET /health/live`
- `GET /health/ready`
- `POST /v1/extractions`
- `GET /docs`
- `GET /openapi.json`

## Estado e limitações

O hardening inicial foi integrado em `main` no commit `1e61e4dc5d89d9ecf59702288d0081824fc7a908`; o proxy Squid isolado foi integrado no commit `0948ceaaeeee387c06849f49d9286753fcc818db`. O CI da branch de teste runtime [run 40048594469](https://github.com/carlos-andrade/API_CARLOS/actions/runs/40048594469) passou Ruff, hashes, pytest, build Squid e teste de rede com containers: o proxy bloqueou o alvo privado e a API não conseguiu egress direto. A autorização de produção continua NO-GO até revisão independente e validação operacional no ambiente-alvo. **A API continua NO-GO para produção pública.** O ambiente de produção tem de configurar `API_KEYS` com tokens fortes, `ALLOWED_HOSTS`, `EGRESS_PROXY_URL` apontando para um proxy gerido com política anti-SSRF e `AUDIT_DB_PATH`. Ainda faltam testes de rede no ambiente-alvo para comprovar o proxy Squid e o bloqueio de egress, verificação de supply chain, staging/rollback e revisão independente. O rate limiting é local ao processo e requer gateway partilhado para múltiplas réplicas. Ainda não existem fila assíncrona, conectores PDF nem SDKs.

## Documentos

- [Âmbito](docs/ESCOPO.md)
- [Arquitetura](docs/ARQUITETURA.md)
- [Roadmap](ROADMAP.md)
- [Contrato da API](docs/CONTRATO_API.md)
- [Registo de conformidade GOVERNANCA](docs/CONFORMIDADE_GOVERNANCA.md)
- [Revisão de arquitetura e segurança para produção](docs/REVISAO_ARQUITETURA_SEGURANCA_PRODUCAO.md)

A referência à GOVERNANCA não declara conformidade integral. A conformidade deve ser demonstrada por inspeção e evidências locais.
