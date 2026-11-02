---
type: llm
focus: trace
weight: 1
---

O webhook de pagamento (src/routes/pagamentos.js) é apontado sem verificação de assinatura (ARC-101) e sem idempotência (ARC-014), com ações do tipo CORRIGIR ou CRIAR.
