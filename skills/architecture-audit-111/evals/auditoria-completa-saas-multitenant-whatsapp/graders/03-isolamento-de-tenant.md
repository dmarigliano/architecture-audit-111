---
type: llm
focus: trace
weight: 1
---

O relatório identifica que a rota de detalhe de cliente em src/routes/clientes.js consulta por id sem filtro de tenant (acesso a dados de outro tenant) como risco P0 ou P1 na auditoria transversal de multi-tenancy.
