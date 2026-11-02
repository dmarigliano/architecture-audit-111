CREATE TABLE tenants (id SERIAL PRIMARY KEY, nome TEXT NOT NULL);
CREATE TABLE usuarios (id SERIAL PRIMARY KEY, tenant_id INT REFERENCES tenants(id), email TEXT UNIQUE, senha_hash TEXT);
CREATE TABLE clientes (id SERIAL PRIMARY KEY, tenant_id INT REFERENCES tenants(id), nome TEXT, telefone TEXT);
CREATE INDEX idx_clientes_tenant ON clientes(tenant_id);
