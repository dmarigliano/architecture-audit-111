const router = require('express').Router();
const db = require('../db');

// lista clientes do tenant autenticado
router.get('/', async (req, res) => {
  const r = await db.query('SELECT * FROM clientes WHERE tenant_id = $1 ORDER BY nome', [req.user.tenant_id]);
  res.json(r.rows);
});

// busca por nome
router.get('/busca', async (req, res) => {
  const q = req.query.nome;
  const r = await db.query(`SELECT * FROM clientes WHERE tenant_id = ${req.user.tenant_id} AND nome ILIKE '%${q}%'`);
  res.json(r.rows);
});

// detalhe do cliente
router.get('/:id', async (req, res) => {
  const r = await db.query('SELECT * FROM clientes WHERE id = $1', [req.params.id]);
  res.json(r.rows[0]);
});

module.exports = router;
