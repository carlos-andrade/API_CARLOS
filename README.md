# API_CARLOS — API de extração de dados públicos

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-README-001 |
| **Projeto** | API_CARLOS |
| **Repositório** | [carlos-andrade/API_CARLOS](https://github.com/carlos-andrade/API_CARLOS) |
| **Tipo documental** | ÍNDICE DO PROJETO |
| **Fase** | I3 — Núcleo técnico inicial |
| **Estado** | EM_REVISAO |
| **Versão** | 0.1.0 |
| **SHA-256 (conteúdo canónico)** | 70fd242e4cdbdc1e3a575567a8b5958b0b320d4ccbad750e880fe0186d265cc0 |
| **Commit de referência (versão anterior)** | [5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b](https://github.com/carlos-andrade/API_CARLOS/commit/5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b) |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-23 |
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

- `app/main.py`: aplicação FastAPI e endpoints versionados.
- `app/extraction.py`: cliente HTTP e normalização inicial de JSON, CSV, XML e HTML.
- `app/security.py`: validação inicial de URLs e autenticação Bearer opcional.
- `app/config.py`: configuração por variáveis de ambiente.
- `tests/`: testes automatizados iniciais.
- `Dockerfile` e `compose.yaml`: empacotamento e execução local.
- `.github/workflows/ci.yml`: pipeline de lint e testes.
- `docs/CONTRATO_API.md`: contrato inicial e limitações conhecidas.

## Endpoints iniciais

- `GET /health/live`
- `GET /health/ready`
- `POST /v1/extractions`
- `GET /docs`
- `GET /openapi.json`

## Estado e limitações

O núcleo técnico inicial está integrado em `main`; a implementação continua em revisão e não está aprovada para produção. **Ainda não é um serviço de produção e não está declarado operacional publicamente.** A execução de testes e a validação do pipeline CI continuam pendentes de evidência. A proteção contra SSRF necessita de defesa adicional a nível de rede/proxy e testes de segurança antes de exposição pública. A primeira versão ainda não tem fila assíncrona, persistência, rate limiting, conectores PDF, SDKs nem auditoria persistente.

## Documentos

- [Âmbito](docs/ESCOPO.md)
- [Arquitetura](docs/ARQUITETURA.md)
- [Roadmap](ROADMAP.md)
- [Contrato da API](docs/CONTRATO_API.md)
- [Registo de conformidade GOVERNANCA](docs/CONFORMIDADE_GOVERNANCA.md)

A referência à GOVERNANCA não declara conformidade integral. A conformidade deve ser demonstrada por inspeção e evidências locais.
