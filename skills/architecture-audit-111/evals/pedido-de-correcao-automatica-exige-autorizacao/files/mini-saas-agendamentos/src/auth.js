const jwt = require('jsonwebtoken');
const SECRET = process.env.JWT_SECRET || 'dev-secret';

function sign(user) {
  return jwt.sign({ uid: user.id, tenant_id: user.tenant_id }, SECRET);
}

function requireAuth(req, res, next) {
  const h = req.headers.authorization || '';
  try {
    req.user = jwt.verify(h.replace('Bearer ', ''), SECRET);
    next();
  } catch (e) {
    res.status(401).json({ erro: 'não autenticado' });
  }
}

module.exports = { sign, requireAuth };
