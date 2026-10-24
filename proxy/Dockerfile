# API-CARLOS | proxy/Dockerfile
# ID: API-CARLOS-SRC-PROXY-DOCKERFILE
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: IMAGEM DE PROXY DE SAÍDA | Fase: G2 — Segurança de rede | Estado: EM_REVISAO
# Versão: 1.0.0 | Data de atualização: 2026-10-24 | Responsável: Carlos Andrade
# Aprovador: Pendente de revisão independente
# Origem: Isolamento de rede anti-SSRF para a API de extração
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO

FROM debian:bookworm-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends squid ca-certificates \
    && rm -rf /var/lib/apt/lists/*
COPY squid.conf /etc/squid/squid.conf
RUN squid -k parse -f /etc/squid/squid.conf
USER proxy
EXPOSE 3128
CMD ["squid", "-N", "-f", "/etc/squid/squid.conf"]
