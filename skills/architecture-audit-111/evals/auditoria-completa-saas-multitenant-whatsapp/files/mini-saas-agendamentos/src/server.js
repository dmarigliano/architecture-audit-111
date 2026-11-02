const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { requireAuth } = require('./auth');

const app = express();
app.use(helmet());
app.use(cors({ origin: true, credentials: true }));
app.use(express.json());

// rate limit apenas no login
app.use('/login', rateLimit({ windowMs: 60_000, max: 10 }));

app.use('/webhooks/pagamento', require('./routes/pagamentos'));
app.use('/webhooks/whatsapp', require('./routes/whatsapp'));
app.use('/clientes', requireAuth, require('./routes/clientes'));

app.get('/health', (req, res) => res.json({ ok: true }));

app.listen(process.env.PORT || 3000);
