# API-CARLOS | scripts/verify_canonical_hashes.py
# ID: API-CARLOS-SRC-VERIFY-CANONICAL-HASHES
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: SCRIPT DE VERIFICAÇÃO | Fase: G2 — Governação e segurança | Estado: EM_REVISAO
# Versão: 1.0.0 | Data de atualização: 2026-10-24 | Responsável: Carlos Andrade
# Aprovador: Pendente de aprovação formal
# Origem: Norma de cabeçalhos GOVERNANCA e controlo independente de integridade
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO
"""Independently verify canonical SHA-256 declarations in governance Markdown files."""
from __future__ import annotations
import hashlib
import re
import sys
from pathlib import Path
FILES = (Path('README.md'), Path('ROADMAP.md'), Path('docs/ARQUITETURA.md'), Path('docs/ESCOPO.md'), Path('docs/CONTRATO_API.md'), Path('docs/CONFORMIDADE_GOVERNANCA.md'))
HASH_ROW = re.compile(r'^\\| \\*\\*SHA-256 \\(conteúdo canónico\\)\\*\\* \\| ([0-9a-f]{64}) \\|$')
EXCLUDED = ('**SHA-256 (conteúdo canónico)**', '**Commit de referência (versão anterior)**')
def canonical_bytes(text: str) -> bytes:
    text = text.lstrip('\\ufeff').replace('\\r\\n', '\\n').replace('\\r', '\\n')
    return '\\n'.join(line for line in text.split('\\n') if not any(field in line for field in EXCLUDED)).encode('utf-8')
def verify(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    declared = next((m.group(1) for line in text.splitlines() if (m := HASH_ROW.match(line))), None)
    if declared is None:
        print(f'FAIL {path}: SHA-256 metadata row missing'); return False
    actual = hashlib.sha256(canonical_bytes(text)).hexdigest()
    ok = declared == actual
    print(f'{"PASS" if ok else "FAIL"} {path}: declared={declared} calculated={actual}')
    return ok
if __name__ == '__main__':
    sys.exit(0 if all(verify(path) for path in FILES) else 1)
