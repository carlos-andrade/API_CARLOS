# Contrato HTTP — API_CARLOS

| Campo | Valor |
|---|---|
| ID | API-CARLOS-CONTRACT-001 |
| Versão | 0.1.0 |
| Estado | PROPOSTA TÉCNICA — validação pendente |
| Base path | /v1 |
| Contrato gerado | /openapi.json |

## Autenticação

Em ambiente local, sem `API_KEYS`, a autenticação está desativada para desenvolvimento. Em ambiente partilhado, configurar `API_KEYS` com segredos fortes e usar HTTPS num proxy de confiança. A implementação inicial usa Bearer token estático; antes de produção deve ser substituído ou complementado por gestão de identidade, rotação e armazenamento seguro de segredos.

## POST /v1/extractions

Pedido:
```json
{"url":"https://example.org/data.json"}
```

Resposta: `source_url`, `retrieved_at`, `http_status`, `content_type`, `parser`, `data`, `truncated`.

Códigos principais: 400 URL não permitida/redirecionamento bloqueado; 401 credencial ausente; 403 credencial inválida; 413 resposta demasiado grande; 422 pedido/formato inválido; 502 erro HTTP da fonte; 504 timeout.

## Endpoints operacionais

- `GET /health/live`: processo ativo.
- `GET /health/ready`: versão pronta para receber pedidos.
- `GET /docs`: Swagger UI.
- `GET /openapi.json`: contrato OpenAPI gerado pelo FastAPI.

## Limitações conhecidas

Esta primeira versão é síncrona e suporta HTTP(S) com normalização inicial de JSON, CSV, XML e HTML. Ainda não implementa fila de trabalhos, persistência, quotas por cliente, auditoria persistente, extração PDF, conectores específicos, SDK ou autenticação OIDC. O resultado pode ser truncado por limite de caracteres.

A validação DNS de URL é uma proteção inicial, não uma garantia suficiente isoladamente contra DNS rebinding em ambientes hostis. Antes de exposição pública, é obrigatório implementar e testar egress filtering no nível de rede/proxy, restrição de portas, limites de concorrência, rate limiting e testes de segurança dedicados. Não seguir redirecionamentos automaticamente.
