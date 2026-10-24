# Revisão de arquitetura e segurança para produção — API_CARLOS

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-SECURITY-REVIEW-001 |
| **Projeto** | API_CARLOS |
| **Repositório** | [carlos-andrade/API_CARLOS](https://github.com/carlos-andrade/API_CARLOS) |
| **Tipo documental** | REVISÃO DE ARQUITETURA E SEGURANÇA |
| **Fase** | G2 — Arquitetura e autorização de produção |
| **Estado** | EM_REVISAO |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | a958a9a945f79b853420cb78c7cc4e9347423fd62082b2584fbb6601bef37348 |
| **Commit de referência (versão anterior)** | [8f8b6046ac2c94cb2b6d2f48d86ec12da8ce9023](https://github.com/carlos-andrade/API_CARLOS/commit/8f8b6046ac2c94cb2b6d2f48d86ec12da8ce9023) |
| **Data de criação** | 2026-10-24 |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Carlos Andrade |
| **Aprovador** | Pendente — decisão explícita do responsável e revisão independente |
| **Origem** | Inspeção técnica e hardening do núcleo da API |
| **Autoridade superior** | [Norma GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Decisão atual

**NO-GO para produção pública.** A implementação recebeu controlos adicionais e o CI base está verde, mas ainda não existe evidência suficiente para aprovação formal de operação em produção. Esta decisão é explícita; não equivale a aprovação do proprietário.

## 2. Controlos implementados nesta revisão

- Produção falha ao arrancar sem API_KEYS, ALLOWED_HOSTS, EGRESS_PROXY_URL e AUDIT_DB_PATH.
- Tokens Bearer são comparados em tempo constante.
- Validação de URL rejeita esquemas diferentes de HTTP(S), credenciais embutidas, nomes locais e respostas DNS que incluam qualquer endereço não global.
- Redirecionamentos HTTP são bloqueados; o cliente HTTP não usa variáveis de proxy implícitas do ambiente (trust_env=False) e aplica o proxy explicitamente configurado.
- São aplicados timeout total, limite de bytes recebidos, limite de concorrência e rate limit local por endereço de cliente.
- Eventos de pedido são emitidos como JSON sem token nem query string e persistidos em SQLite quando AUDIT_DB_PATH está configurado.
- O Compose mantém a porta publicada em loopback, filesystem raiz somente de leitura, volume dedicado de auditoria, limites de CPU/memória/processos, init, healthcheck, remove capabilities e ativa no-new-privileges.

## 3. Bloqueios e evidências externas ainda necessários

| ID | Estado | Fecho exigido |
|---|---|---|
| SEC-01 — SSRF/DNS rebinding | PARCIAL | Configurar e testar proxy de saída gerido que resolva o destino no momento da ligação e bloqueie loopback, redes privadas, link-local e metadata endpoints IPv4/IPv6; demonstrar egress deny-by-default. O teste DNS local não substitui esse controlo. |
| SEC-02 — Limites de transporte | PARCIAL | Testes de integração para timeout, tamanho máximo, redirects e comportamento do proxy, incluindo respostas comprimidas e lentas. |
| SEC-03 — Autenticação | IMPLEMENTADO NO CÓDIGO; CONFIGURAÇÃO PENDENTE | Provisionar chaves fortes fora do repositório, validar rotação e confirmar arranque fail-closed no ambiente de produção. |
| SEC-04 — Abuso e isolamento | PARCIAL | O rate limit atual é local ao processo. Em múltiplas réplicas, usar gateway ou armazenamento partilhado; validar quotas e carga. |
| SEC-05 — Auditoria | PARCIAL | Confirmar volume persistente, permissões, backups, retenção, monitorização de falhas de escrita e alertas no ambiente real. |
| SEC-06 — Supply chain | PENDENTE | Fixar dependências com lockfile/hashes, executar scan de vulnerabilidades e rever pinagem por SHA das GitHub Actions e imagem base. |
| SEC-07 — Operação | PENDENTE | Staging, monitorização, resposta a incidentes, rollback e recuperação testados e documentados. |
| SEC-08 — Revisão independente | PENDENTE | Revisor diferente do autor examina código, resultados de testes, proxy, rede e implantação; anexar parecer. |

## 4. Registo formal de decisão

- **Arquitetura de referência:** hardening inicial implementado; aprovação formal independente pendente.
- **Segurança para produção:** **NÃO APROVADA (NO-GO)** até ao fecho dos bloqueios e validação no ambiente-alvo.
- **Aprovador:** pendente de designação/decisão explícita do responsável do projeto.
- **Data da decisão:** 2026-10-24.
- **Evidência:** CI da main no commit 8f8b6046ac2c94cb2b6d2f48d86ec12da8ce9023 — [execução 40046560279](https://github.com/carlos-andrade/API_CARLOS/actions/runs/40046560279).

## 5. Critérios para mudar para GO

1. Configurar proxy de saída com política anti-SSRF e egress deny-by-default; apresentar teste reproduzível de bloqueio de destinos proibidos.
2. Fechar testes de integração para timeouts, limites, redirects, autenticação e rate limiting.
3. Fechar SEC-04 a SEC-07 com evidências operacionais e de supply chain.
4. Obter parecer independente e datado.
5. Registar decisão explícita do responsável autorizado após rever as evidências. Nenhum pedido de implementação nem CI verde substitui esta decisão.

## 6. Histórico

| Versão | Data | Alteração |
|---|---|---|
| 1.0.0 | 2026-10-24 | Revisão inicial com decisão NO-GO e critérios de autorização. |
| 1.1.0 | 2026-10-24 | Regista controlos implementados e separa bloqueios locais dos requisitos de produção ainda não demonstrados. |
