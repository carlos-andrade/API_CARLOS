# API_CARLOS — API de extração de dados públicos

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-README-001 |
| **Projeto** | API_CARLOS |
| **Tipo documental** | ÍNDICE DO PROJETO |
| **Fase** | F0 — Definição de âmbito e governação |
| **Estado** | EM_REVISAO |
| **Versão** | 0.1.0 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Carlos Andrade |
| **Aprovador** | Aprovação formal dos artefactos pendente |
| **Governação de referência** | https://github.com/carlos-andrade/GOVERNANCA |
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

A modalidade principal prevista é uma API HTTP REST versionada, consumida por HTTPS. Um repositório cliente poderá enviar um pedido autenticado, indicar uma fonte ou tarefa de extração, consultar o estado e receber resultados normalizados com metadados de proveniência.

Os contratos de pedido/resposta, autenticação, erros, limites, idempotência e tarefas assíncronas serão especificados antes da implementação. SDKs reutilizáveis e integração por GitHub Actions poderão ser adicionados sem substituir o contrato REST.

**Estado:** a API ainda não está implementada nem publicada como serviço operacional. Os documentos não significam que já exista um endpoint de produção.

## Documentos

- [Âmbito oficial](docs/ESCOPO.md)
- [Arquitetura inicial](docs/ARQUITETURA.md)
- [Roadmap e critérios de aceitação](ROADMAP.md)

## Estado atual

O repositório iniciou-se com o ficheiro de licença. Esta alteração documental propõe o âmbito, a arquitetura e o roadmap; ainda não implementa serviço, conectores, testes de execução ou implantação.

A referência à GOVERNANCA não declara conformidade integral. A conformidade deve ser demonstrada por inspeção e evidências locais.
