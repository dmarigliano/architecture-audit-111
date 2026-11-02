---
type: llm
focus: trace
weight: 1
---

A auditoria transversal de WhatsApp aponta que src/routes/whatsapp.js não valida a assinatura do webhook e usa o tenant vindo do corpo da requisição, e aponta o telefone do remetente registrado em log.
