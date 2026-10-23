# Arquitetura inicial — API_CARLOS

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-ARCH-001 |
| **Projeto** | API_CARLOS |
| **Repositório** | [carlos-andrade/API_CARLOS](https://github.com/carlos-andrade/API_CARLOS) |
| **Tipo documental** | ARQUITETURA |
| **Fase** | G2 — Arquitetura e requisitos |
| **Estado** | EM_REVISAO |
| **Versão** | 0.1.0 |
| **SHA-256 (conteúdo canónico)** | b552fe3d7f5bb565adb2255dad8526934d8e4ce45d66f79b8b5aadfaccc90a14 |
| **Commit de referência (versão anterior)** | [5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b](https://github.com/carlos-andrade/API_CARLOS/commit/5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b) |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Carlos Andrade |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Artefacto do projeto API_CARLOS; atualização de conformidade documental |
| **Autoridade superior** | [Norma GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Princípio arquitetural

Separar o contrato público da API, o plano de orquestração, os conectores de origem, o pipeline de qualidade e a persistência. A API pública não deve expor detalhes internos de cada conector.

## 2. Componentes lógicos

1. **API Gateway:** HTTPS, autenticação, autorização, validação inicial, quotas e correlação de pedidos.
2. **Orquestrador:** valida tarefa, escolhe conector, aplica política de execução e controla timeouts e retentativas.
3. **Registo de fontes/conectores:** capacidades, formatos, domínios permitidos, versão e requisitos de cada conector.
4. **Conectores:** módulos isolados para API/HTTP, CSV, JSON, XML, RSS/Atom, HTML, PDF e, futuramente, navegador automatizado.
5. **Pipeline de dados:** parsing, normalização, validação, deduplicação e enriquecimento de metadados.
6. **Gestor de tarefas:** execução síncrona curta e fila para tarefas longas; estados QUEUED, RUNNING, SUCCEEDED, PARTIAL, FAILED e CANCELLED.
7. **Persistência:** metadados, resultados e conteúdos brutos apenas quando permitido e necessário.
8. **Observabilidade e auditoria:** logs estruturados, métricas, request/job ID, tempos, erros e eventos de segurança.
9. **Contrato de integração:** OpenAPI versionado, esquemas de pedidos/respostas, exemplos e política de compatibilidade.

## 3. Contrato externo previsto

A nomenclatura abaixo é proposta para discussão; os endpoints ainda não existem.

- POST /v1/extractions — submeter uma extração.
- GET /v1/extractions/{job_id} — consultar estado.
- GET /v1/extractions/{job_id}/result — obter resultado.
- DELETE /v1/extractions/{job_id} — solicitar cancelamento, quando suportado.
- GET /health/live e GET /health/ready — verificações operacionais separadas, sem expor dados sensíveis.
- GET /openapi.json — contrato publicado.

O pedido deverá declarar uma fonte ou identificador de fonte registada, o formato de saída e parâmetros permitidos pelo conector. O cliente não poderá fornecer instruções arbitrárias para aceder a IPs privados, metadados de cloud, loopback ou destinos internos.

## 4. Interoperabilidade entre repositórios

- O serviço será consumido por HTTPS; os repositórios clientes não importam código privado do servidor.
- Os contratos serão versionados e compatíveis dentro de uma versão principal.
- A autenticação suportará credenciais de serviço com escopo mínimo e rotação.
- Erros terão códigos estáveis, mensagem segura e indicação de retryabilidade.
- Pedidos longos terão job_id, consulta de estado e política de expiração dos resultados.
- O contrato documentará limites de tamanho, quotas, timeouts, paginação, idempotência e cancelamento.
- SDKs e ações reutilizáveis do GitHub poderão ser criados depois de estabilizar o contrato; não serão o único método de integração.
- Testes de contrato e integração deverão correr no CI do API_CARLOS e, quando possível, no CI dos consumidores.

## 5. Segurança de extração

- Mitigar SSRF por validação e resolução DNS, bloqueio de endereços privados/reservados, validação após redirecionamentos e egress controlado.
- Aplicar allowlists de domínios por conector quando apropriado; URLs fornecidos pelo cliente não são confiáveis.
- Restringir protocolos, tamanho de resposta, tempo, profundidade de parsing, número de páginas e uso de memória/CPU.
- Isolar processamento de PDF, HTML e navegador.
- Não executar scripts extraídos de páginas nem carregar segredos do serviço em contexto de navegador.
- Respeitar termos, licenças, limites e políticas das fontes; não contornar mecanismos de acesso.
- Redigir tokens, cookies, dados pessoais desnecessários e URLs assinados dos logs.
- Usar armazenamento temporário com retenção e eliminação definidas.

## 6. Decisões em aberto

- Linguagem e framework do serviço.
- Provedor e modelo de implantação.
- Base de dados e armazenamento de objetos.
- Tecnologia de filas.
- Modelo de autenticação e gestão de tenants.
- Quotas, retenção, limites de payload e SLOs.
- Política de registo de fontes e aprovação de novos conectores.
- Necessidade e limites da automação de navegador.

Estas decisões exigem comparação de alternativas e critérios mensuráveis antes de aprovação.

## 7. Critérios para aprovar G2

- [ ] Diagramas de contexto e componentes revistos.
- [ ] Contrato OpenAPI inicial validado por ferramenta.
- [ ] Modelo de ameaças e controlos SSRF revistos.
- [ ] Contratos de autenticação, autorização, erros e quotas definidos.
- [ ] Decisões tecnológicas justificadas por requisitos e custo operacional.
- [ ] Estratégia de testes unitários, contrato, integração e segurança aprovada.
- [ ] Plano de implantação, observabilidade, recuperação e rollback documentado.
