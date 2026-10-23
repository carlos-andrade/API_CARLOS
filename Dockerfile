# API-CARLOS | Dockerfile
# ID: API-CARLOS-SRC-DOCKERFILE
# Projeto: API_CARLOS | Repositório: https://github.com/carlos-andrade/API_CARLOS
# Tipo documental: IMAGEM DE CONTÊINER | Fase: I3 — Núcleo técnico inicial | Estado: EM_REVISAO
# Versão: 0.1.0 | Data de atualização: 2026-10-23 | Responsável: Carlos Andrade
# Aprovador: Pendente de aprovação formal
# Origem: artefacto do projeto API_CARLOS
# Autoridade superior: https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md
# Cadeia de autoridade: PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO

FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /srv/api-carlos
COPY pyproject.toml ./
COPY app ./app
RUN pip install --no-cache-dir .
RUN useradd --create-home --uid 10001 apiuser
USER apiuser
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
