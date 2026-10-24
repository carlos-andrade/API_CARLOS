# API-CARLOS | tests/test_deployment_security.py
# ID: API-CARLOS-SRC-TESTS-DEPLOYMENT-SECURITY-PY
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: TESTES PYTHON | Fase: G2 — Segurança de rede | Estado: EM_REVISAO
# Versão: 1.0.0 | Data de atualização: 2026-10-24 | Responsável: Carlos Andrade
# Aprovador: Pendente de revisão independente
# Origem: Testes estáticos de regressão para isolamento de rede e ACL do proxy
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO

from pathlib import Path

import yaml


def test_api_has_no_direct_egress_network():
    compose = yaml.safe_load(Path("compose.yaml").read_text(encoding="utf-8"))
    assert compose["services"]["api"]["networks"] == ["api_internal"]
    assert compose["networks"]["api_internal"]["internal"] is True
    assert "proxy_egress" in compose["services"]["egress-proxy"]["networks"]


def test_proxy_denies_private_and_reserved_destinations():
    policy = Path("proxy/squid.conf").read_text(encoding="utf-8")
    for acl in (
        "http_access deny deny_local",
        "http_access deny to_linklocal",
        "http_access deny private_ipv4",
        "http_access deny reserved_ipv4",
        "http_access deny private_ipv6",
        "http_access deny reserved_ipv6",
    ):
        assert acl in policy
