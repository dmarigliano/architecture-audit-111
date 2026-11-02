const router = require('express').Router();
const db = require('../db');

// webhook do gateway: confirma pagamento
router.post('/', async (req, res) => {
  const { tenant_id, cliente_id, valor, ref } = req.body;
  await db.query(
    'INSERT INTO pagamentos (tenant_id, cliente_id, valor, gateway_ref) VALUES ($1,$2,$3,$4)',
    [tenant_id, cliente_id, valor, ref]
  );
  res.sendStatus(200);
});

module.exports = router;
