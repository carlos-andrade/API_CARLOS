# API-CARLOS | scripts/check_canonical_hashes.py
# ID: API-CARLOS-SRC-CANONICAL-HASH-CHECK
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: SCRIPT DE VERIFICAÇÃO | Fase: G2 — Governação e segurança | Estado: EM_REVISAO
# Versão: 1.0.0 | Data de atualização: 2026-10-24 | Responsável: Carlos Andrade
# Aprovador: Pendente de aprovação formal
# Origem: Norma de cabeçalhos GOVERNANCA
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO
import hashlib
import sys
from pathlib import Path
FILES = ['README.md', 'ROADMAP.md', 'docs/ARQUITETURA.md', 'docs/ESCOPO.md', 'docs/CONTRATO_API.md', 'docs/CONFORMIDADE_GOVERNANCA.md']
def main():
    failed = False
    for name in FILES:
        text = Path(name).read_text(encoding='utf-8').lstrip(chr(65279)).replace(chr(13)+chr(10), chr(10)).replace(chr(13), chr(10))
        lines = text.split(chr(10))
        row = next((line for line in lines if line.startswith('| **SHA-256 (conteúdo canónico)** |')), None)
        if row is None:
            print('FAIL', name, 'missing hash row'); failed = True; continue
        declared = row.split('|')[2].strip()
        canonical = chr(10).join(line for line in lines if '**SHA-256 (conteúdo canónico)**' not in line and '**Commit de referência (versão anterior)**' not in line)
        actual = hashlib.sha256(canonical.encode('utf-8')).hexdigest()
        ok = declared == actual
        print(('PASS' if ok else 'FAIL'), name, 'declared='+declared, 'calculated='+actual)
        failed = failed or not ok
    return 1 if failed else 0
if __name__ == '__main__':
    sys.exit(main())
