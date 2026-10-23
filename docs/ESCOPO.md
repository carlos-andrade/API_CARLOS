# Carta de âmbito — API_CARLOS

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-SCOPE-001 |
| **Projeto** | API_CARLOS |
| **Repositório** | [carlos-andrade/API_CARLOS](https://github.com/carlos-andrade/API_CARLOS) |
| **Tipo documental** | CARTA DE ÂMBITO |
| **Fase** | F0 — Definição de âmbito e governação |
| **Estado** | EM_REVISAO |
| **Versão** | 0.1.0 |
| **SHA-256 (conteúdo canónico)** | 3edab1adf74aa2b6f8b262ab672a3e3a37d436e7fd668051c8a64ee5c96c5d2e |
| **Commit de referência (versão anterior)** | [5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b](https://github.com/carlos-andrade/API_CARLOS/commit/5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b) |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Carlos Andrade |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Artefacto do projeto API_CARLOS; atualização de conformidade documental |
| **Autoridade superior** | [Norma GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-SCOPE-001 |
| **Projeto** | API_CARLOS |
| **Tipo documental** | CARTA DE ÂMBITO |
| **Fase** | F0 — Definição de âmbito e governação |
| **Estado** | EM_REVISAO |
| **Versão** | 0.1.0 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Carlos Andrade |
| **Aprovador** | Âmbito confirmado na conversa; aprovação formal deste documento pendente |
| **Autoridade superior** | Lei aplicável, contratos vinculativos e políticas formalmente aprovadas |
| **Governação de referência** | https://github.com/carlos-andrade/GOVERNANCA |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Propósito

Construir uma API modular e reutilizável para descobrir, extrair, normalizar, validar e disponibilizar dados públicos e de acesso livre publicados na Internet. A solução deverá cobrir fontes fáceis e fontes de elevada complexidade técnica, sem prometer acesso universal nem contornar restrições.

## 2. Beneficiários e consumidores

- Outros repositórios GitHub do proprietário ou de colaboradores autorizados.
- Aplicações, serviços internos e pipelines de dados.
- Ferramentas de análise, monitorização, investigação e agentes de software.
- Utilizadores autorizados que consumam a API mediante contratos e limites definidos.

## 3. Objetivos funcionais

1. Receber pedidos de extração por contrato documentado.
2. Identificar ou aceitar a fonte e selecionar o conector adequado.
3. Executar extração síncrona para tarefas rápidas e assíncrona para tarefas longas.
4. Normalizar resultados para formato comum, preservando conteúdo bruto quando permitido.
5. Validar esquema, campos, duplicados e qualidade básica.
6. Devolver resultados, estado, erros e metadados de proveniência.
7. Registar execuções e permitir auditoria e diagnóstico.
8. Adicionar conectores sem alterar o contrato público de forma incompatível.
9. Permitir invocação por outros repositórios através de HTTPS, credenciais de serviço e exemplos reproduzíveis.

## 4. Famílias de fontes previstas

- APIs oficiais e endpoints públicos documentados.
- Ficheiros e datasets: CSV, JSON, XML, ZIP e formatos tabulares comuns.
- RSS/Atom e feeds.
- HTML, tabelas, paginação e páginas com navegação complexa.
- PDF e documentos públicos.
- Fontes que exigem JavaScript ou automação de navegador, quando autorizadas.
- Fontes históricas, volumosas ou instáveis que necessitem de filas, retentativas e processamento incremental.

A inclusão de uma família não implica que todos os sites dessa família já sejam suportados. Cada conector necessita de implementação, testes e validação próprios.

## 5. Requisitos não funcionais

- **Interoperabilidade:** REST/HTTPS, JSON como formato padrão e OpenAPI como contrato publicado.
- **Versionamento:** prefixo de versão na API, como /v1, e política para alterações compatíveis e incompatíveis.
- **Segurança:** autenticação entre serviços, autorização por escopo, gestão de segredos, limitação de pedidos e proteção contra SSRF.
- **Confiabilidade:** timeouts, retentativas com backoff, idempotência quando aplicável, filas e estados explícitos.
- **Auditabilidade:** identificador de tarefa, fonte, timestamps, versão do conector, resultado, erros e hashes quando apropriado.
- **Qualidade:** validação de esquema, normalização determinística e sinalização de dados incompletos.
- **Observabilidade:** logs estruturados, métricas, correlação por request/job ID e alertas.
- **Manutenibilidade:** conectores isolados, testes automatizados e documentação operacional.
- **Privacidade e conformidade:** minimização de dados, retenção definida e respeito às obrigações legais e contratuais.

## 6. Fora do âmbito e limites

- Contornar paywalls, autenticação, CAPTCHA ou controlos de acesso.
- Extrair dados pessoais ou sensíveis sem base legal e autorização apropriadas.
- Garantir que qualquer fonte da Internet pode ser acedida ou extraída.
- Prometer disponibilidade, latência, cobertura ou quotas antes de medições reais.
- Republicar conteúdo protegido sem direitos ou autorização adequados.
- Aceder a destinos de rede arbitrários sem isolamento e controlos de segurança.

## 7. Modelo de integração entre repositórios

A API será um serviço central consumido por clientes externos; a implementação dos conectores permanece no repositório API_CARLOS. Os repositórios consumidores não deverão depender de caminhos locais, importar ficheiros internos do servidor nem copiar conectores.

Fluxo previsto:

1. O repositório cliente obtém credencial de serviço por mecanismo seguro.
2. Invoca o endpoint HTTPS versionado e envia uma tarefa validada.
3. Recebe resultado imediato ou identificador de tarefa assíncrona.
4. Consulta estado, quando necessário, e recolhe o resultado.
5. Guarda no próprio repositório os dados e evidências que lhe competem, incluindo origem e identificador da tarefa.
6. Trata erros transitórios, limites e falhas segundo o contrato publicado.

Credenciais nunca devem ser gravadas no código, histórico Git, issues públicas ou artefactos de workflow. Em GitHub Actions, usar secrets ou identidade federada quando suportada.

## 8. Critérios de aceitação do âmbito

- [ ] Missão, beneficiários, objetivos e limites documentados.
- [ ] Contrato REST versionado definido em OpenAPI.
- [ ] Exemplo de cliente externo documentado.
- [ ] Autenticação de serviço e autorização especificadas.
- [ ] Formato de erro, limites, timeouts e idempotência especificados.
- [ ] Modelo de proveniência e estados de execução definidos.
- [ ] Regras de segurança para destinos e conteúdos externos documentadas.
- [ ] Roadmap local publicado e ligado no README.
- [ ] Inspeção de conformidade com GOVERNANCA registada.
- [ ] Testes de integração entre serviço e repositório consumidor executados antes de declarar interoperabilidade operacional.

## 9. Riscos e dependências

- Fontes alteram estrutura, URLs, formatos e limites sem aviso.
- Termos, licenças ou direitos de utilização variam por fonte.
- Navegação automatizada aumenta custo, superfície de ataque e fragilidade.
- O serviço central torna-se dependência operacional dos repositórios consumidores.
- Armazenamento e redistribuição podem ter restrições distintas da recolha.
- Autenticação e quotas precisam de ser concebidas antes da exposição pública.

## 10. Histórico

| Versão | Data | Alteração |
|---|---|---|
| 0.1.0 | 2026-10-23 | Primeira definição de âmbito, limites e interoperabilidade; aguarda revisão formal. |
