# Casos de teste do skill

Três cenários executáveis com o projeto fictício `mini-saas-agendamentos` (falhas plantadas de propósito).

| Caso | O que verifica |
|------|----------------|
| `auditoria-completa-saas-multitenant-whatsapp` | Auditoria dos 111 controles, falhas plantadas, parecer, planilha e proteção de segredos |
| `sem-acesso-ao-ambiente-nao-confunde-ausencia-com-falha` | Ausência de evidência vira NOT_VERIFIED/VERIFICAR, nunca FAIL |
| `pedido-de-correcao-automatica-exige-autorizacao` | Auditoria é diagnóstica: não altera arquivos sem autorização expressa |

Cada caso tem `prompt.md`, `case.yaml`, `graders/` e `files/`. O arquivo `files/.../dot-env` é um arquivo de ambiente **fictício**, versionado com esse nome para não acionar detectores de segredo; o script `place-files.sh` o renomeia para `.env` ao montar o cenário.

Para rodar com o Claude Code (v2.1.269 ou superior), a partir da pasta do skill:

```bash
claude plugin eval . --allow-tools Write,Edit,Bash --scaffold
```

São execuções reais de modelo, com custo. O projeto de teste é vulnerável de propósito: não o use em produção.
