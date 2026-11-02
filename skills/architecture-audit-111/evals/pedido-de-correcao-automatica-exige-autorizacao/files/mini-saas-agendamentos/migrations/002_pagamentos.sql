CREATE TABLE pagamentos (id SERIAL PRIMARY KEY, tenant_id INT, cliente_id INT, valor NUMERIC, gateway_ref TEXT, criado_em TIMESTAMP DEFAULT now());
