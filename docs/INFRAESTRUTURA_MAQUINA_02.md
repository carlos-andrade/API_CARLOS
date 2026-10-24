# Inventário da Máquina 02 — Infraestrutura candidata da API_CARLOS

| Campo | Valor |
|---|---|
| **ID** | API-CARLOS-INFRA-MAQUINA-02-001 |
| **Projeto** | API_CARLOS |
| **Repositório** | [carlos-andrade/API_CARLOS](https://github.com/carlos-andrade/API_CARLOS) |
| **Tipo documental** | INVENTÁRIO DE INFRAESTRUTURA |
| **Fase** | O5 — Preparação de ambiente |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 9c7897958969851df3b238f127a33f55342cce6e724d5cd1b41182118d04fcaa |
| **Commit de referência (versão anterior)** | Não aplicável — documento inicial |
| **Data de criação** | 2026-10-24 |
| **Data de atualização** | 2026-10-24 |
| **Responsável** | Carlos Andrade |
| **Aprovador** | Pendente de aprovação formal |
| **Origem** | Saídas de diagnóstico fornecidas pelo responsável no chat em 2026-10-24 |
| **Autoridade superior** | [Norma GOV-CAB-NORMA-001 v1.0.3](https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Objetivo e âmbito

Este documento regista as características observadas da Máquina 02, disponibilizada pelo responsável como possível servidor dedicado à API_CARLOS. É um inventário documental baseado nas saídas de comandos fornecidas; não representa acesso independente ao equipamento nem certifica a segurança do servidor.

A intenção declarada é reservar a Máquina 02 exclusivamente à API_CARLOS. No momento do inventário, contudo, estavam ativos outros serviços. A dedicação exclusiva é, portanto, um objetivo de transição ainda não concretizado.

## 2. Hardware e sistema operativo observados

| Elemento | Evidência fornecida |
|---|---|
| Arquitetura | x86_64 |
| Processador | Intel Core i3-4130 @ 3,40 GHz |
| CPU | 2 núcleos físicos, 4 threads |
| Memória | 15 GiB reportados; cerca de 13 GiB livres e 13 GiB disponíveis na recolha |
| Swap | 4,0 GiB; sem utilização na recolha |
| Sistema operativo | Ubuntu 24.04.4 LTS, codename `noble` |
| Disco | Dispositivo `sda` de 223,6 GB reportados |
| Partição raiz | `/dev/sda2`, ext4, 218 GB reportados, 13 GB utilizados, 195 GB disponíveis |
| Partição EFI | `/dev/sda1`, vfat, aproximadamente 1,1 GB reportados |

Os tamanhos variam entre as saídas por causa da forma como as ferramentas apresentam unidades e capacidades. Não foi solicitada nem executada qualquer alteração de particionamento.

## 3. Software e rede observados

| Elemento | Evidência fornecida |
|---|---|
| Docker Engine | 29.2.1 |
| Docker Compose | v5.0.2 |
| Estado do Docker | Serviço ativo |
| Interface de rede | `enp1s0`, ativa |
| Endereço IPv4 | `192.168.60.141/24` |
| Gateway predefinido | `192.168.60.1` |
| Rede Docker Compose | `chirpstack-docker_default` |
| Projeto Compose identificado | `chirpstack-docker`, ficheiro `/home/userguest/chirpstack-docker/docker-compose.yml` |

## 4. Serviços presentes no momento da recolha

Foram observados os seguintes serviços ou aplicações:

- Sete contentores do projeto ChirpStack: Mosquitto, ChirpStack REST API, Gateway Bridge, ChirpStack, Basic Station Gateway Bridge, Redis e PostgreSQL 14.
- Zabbix Server e Zabbix Agent.
- MySQL Community Server.
- PostgreSQL 16 no sistema anfitrião.
- Redis no sistema anfitrião.
- BIND DNS (`named`).
- Apache HTTP Server.
- Dovecot IMAP/POP3.
- Mosquitto instalado via Snap.
- SSH e Docker.

As portas publicadas dos contentores ChirpStack incluem `3001`, `8080` e `8090`, vinculadas a todas as interfaces IPv4 e IPv6 na saída recolhida. A listagem de portas também mostrou serviços nas portas 80, 443, 22, 10050, 110, 143, 993 e 995, entre outras. Esta observação não prova, por si só, acessibilidade a partir da Internet; as regras de firewall e do router não foram auditadas.

## 5. Estado e limitações

- A máquina física e o sistema Ubuntu foram demonstrados através de saídas de terminal fornecidas pelo responsável.
- Os recursos de CPU, RAM e armazenamento parecem adequados para preparar um ambiente inicial de testes da API_CARLOS; o dimensionamento de produção não foi validado.
- O Docker estava ativo, mas as primeiras consultas sem `sudo` falharam por falta de permissão para aceder ao socket. A recolha posterior com `sudo` identificou os contentores e o projeto Compose.
- A API_CARLOS ainda não foi instalada nem validada nesta máquina.
- Não foram executados testes de segurança, carga, recuperação, disponibilidade ou acesso externo neste servidor.
- Não foi verificada a existência de backups restauráveis nem a política de firewall.
- A intenção de dedicar a máquina exclusivamente à API_CARLOS não significa que os serviços anteriores tenham sido migrados ou removidos.

## 6. Próximas ações — apenas quando autorizadas

1. Decidir quais os serviços existentes que devem ser migrados, preservados ou desativados; identificar proprietários, dependências e dados persistentes antes de qualquer alteração.
2. Confirmar backups e testar a restauração dos dados relevantes antes de uma migração ou remoção.
3. Quando a máquina estiver efetivamente dedicada, preparar o diretório de implantação e instalar a API_CARLOS a partir do repositório oficial, confirmando o commit pretendido.
4. Validar configuração, segredos, persistência, proxy de saída Squid, isolamento de rede, logs e endpoints de saúde.
5. Executar testes no ambiente-alvo e atualizar o roadmap apenas com resultados observados.
6. Manter a decisão **NO-GO para produção pública** até à conclusão dos gates de segurança, operação e revisão independente.

## 7. Histórico

| Data | Alteração | Evidência |
|---|---|---|
| 2026-10-24 | Inventário inicial da Máquina 02 registado a partir das saídas fornecidas pelo responsável | CPU, sistema operativo, memória, disco, Docker, rede, contentores e serviços observados no chat |
