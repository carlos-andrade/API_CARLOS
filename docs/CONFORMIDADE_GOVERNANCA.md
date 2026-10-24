# Registo de conformidade documental — API_CARLOS

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-GOV-INSPECTION-001 |
| **Projeto** | API_CARLOS |
| **Repositório** | [carlos-andrade/API_CARLOS](https://github.com/carlos-andrade/API_CARLOS) |
| **Tipo documental** | REGISTO DE INSPEÇÃO DE CONFORMIDADE |
| **Fase** | F0–I3 — Governação documental e núcleo técnico |
| **Estado** | EM_REVISAO |
| **Versão** | 0.1.0 |
| **SHA-256 (conteúdo canónico)** | 391fb81198da13d3e5c934ad3d68507d39fb998a702f642bde67e275ed1ae679 |
| **Commit de referência (versão anterior)** | [5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b](https://github.com/carlos-andrade/API_CARLOS/commit/5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b) |
| **Data de criação** | 2026-10-23 |
| **Data de atualização** | 2026-10-23 |
| **Responsável** | Carlos Andrade |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Inspeção documental e adoção local das normas GOVERNANCA |
| **Autoridade superior** | [Norma GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo e autoridade

Este registo documenta a inspeção inicial de adoção da norma de cabeçalho no repositório API_CARLOS. A referência obrigatória é [GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md). O roadmap deve também respeitar [GOV-CARTA-ROADMAP-001](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CARTA-CONTRATO-PADRAO-ROADMAP.md) e [GOV-STD-STATUS-001](https://github.com/carlos-andrade/GOVERNANCA/blob/main/standards/status-e-percentual-de-conclusao.md).

## Âmbito inspecionado

- Documentos Markdown: `README.md`, `ROADMAP.md`, `docs/ESCOPO.md`, `docs/ARQUITETURA.md` e `docs/CONTRATO_API.md`.
- Código Python: `app/` e `tests/`.
- Configuração e automação: `.env.example`, `.gitignore`, `.github/workflows/ci.yml`, `Dockerfile`, `compose.yaml` e `pyproject.toml`.

## Resultado da inspeção

- **Cabeçalhos Markdown:** normalizados para H1 seguido de tabela de metadados com os campos obrigatórios, incluindo SHA-256 canónico, commit de referência, origem, autoridade superior e cadeia de autoridade.
- **Código e configuração:** acrescentados blocos de comentários com identificação do artefacto, projeto, repositório, tipo, fase, estado, versão, data, responsável, origem e autoridade.
- **Roadmap:** alinhado com a existência do núcleo técnico já integrado em `main`; o estado do CI permanece pendente de confirmação por execução.
- **Aprovação:** pendente. Este registo não declara aprovação formal do âmbito, arquitetura, contrato ou release.
- **Conformidade global:** parcial e em revisão. A existência dos cabeçalhos não demonstra, por si só, conformidade técnica, segurança de produção ou validação de testes.

## Não conformidades e pendências

1. Confirmar que todos os SHA-256 canónicos dos Markdown correspondem ao conteúdo publicado e à regra de exclusão das duas linhas de metadados.
2. O CI [run 39941146403](https://github.com/carlos-andrade/API_CARLOS/actions/runs/39941146403) falhou em `ruff check .` com SIM117, F841, UP017, I001 e F401; o passo pytest foi ignorado. Correções de lint foram aplicadas nesta branch e aguardam nova execução CI.
3. Rever a política de segurança SSRF, incluindo DNS rebinding, redirecionamentos, egress filtering e restrição de portas.
4. Formalizar a aprovação do âmbito, da arquitetura e do contrato HTTP.
5. Rever a completude dos cabeçalhos de código/configuração e validar que os comentários não alteram o comportamento dos formatos.
6. Não declarar serviço operacional ou percentual de conclusão até haver critérios ponderados e evidência verificável.

## Evidências de execução

- Commit de referência anterior à presente revisão: [`5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b`](https://github.com/carlos-andrade/API_CARLOS/commit/5134e2d4c4b6ebd717e1656cbe44b9fbd97f125b).
- Branch de trabalho: `chore/governance-headers-v1`.
- PR de conformidade: a criar após revisão final dos ficheiros.
- Testes automatizados e CI nesta alteração: ainda não executados/verificados por este registo.

## Critérios de aceitação

- [ ] Cada Markdown começa por H1 e tabela de metadados canónica.
- [ ] Os dois campos excluídos do cálculo SHA-256 estão identificados exatamente.
- [ ] Os hashes canónicos foram recalculados e verificados independentemente após a última alteração de conteúdo.
- [ ] Código/configuração contém comentários de metadados adequados ao formato.
- [ ] Roadmap apresenta fases, gates, evidências, riscos, bloqueios e critérios de saída.
- [ ] CI executado com sucesso, sem alegações baseadas apenas em commits.
- [ ] Revisão de segurança concluída e aprovada.
- [ ] Aprovação formal registada antes de promover o estado a APROVADO.

## Histórico

| Versão | Data | Alteração |
|---|---|---|
| 0.1.0 | 2026-10-23 | Registo inicial de adoção e inspeção; conformidade parcial, pendências explícitas. |
