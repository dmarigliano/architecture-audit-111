const router = require('express').Router();
const db = require('../db');

// handshake de verificação
router.get('/', (req, res) => {
  if (req.query['hub.verify_token'] === process.env.WHATSAPP_VERIFY_TOKEN) {
    return res.send(req.query['hub.challenge']);
  }
  res.sendStatus(403);
});

// mensagens recebidas
router.post('/', async (req, res) => {
  const msg = req.body.entry?.[0]?.changes?.[0]?.value?.messages?.[0];
  const tenantId = req.body.tenant_id;
  if (msg) {
    console.log('mensagem recebida de', msg.from, msg.text?.body);
    await db.query('INSERT INTO clientes (tenant_id, nome, telefone) VALUES ($1,$2,$3)', [tenantId, 'novo contato', msg.from]);
  }
  res.sendStatus(200);
});

module.exports = router;
