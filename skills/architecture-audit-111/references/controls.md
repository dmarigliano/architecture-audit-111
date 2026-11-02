# Architecture Audit 111
## Catálogo de 111 controles de arquitetura, segurança e operação

**Versão:** 1.0.0

### Objetivo

Este catálogo define 111 controles para avaliação técnica de aplicações SaaS, plataformas digitais, APIs, sistemas distribuídos e aplicações desenvolvidas com ferramentas tradicionais ou assistidas por IA.

Os IDs são estáveis para permitir comparação entre auditorias e acompanhamento da evolução arquitetural.

A pergunta de cada controle é uma diretriz de inspeção, não uma prova de conformidade.

**Regras fundamentais:**
- Determinar a aplicabilidade antes de atribuir um status.
- Registrar evidências rastreáveis, incluindo caminhos, linhas, configurações, testes ou sistemas de origem.
- Não considerar uma tecnologia obrigatória apenas porque aparece no catálogo.
- Não recomendar complexidade arquitetural sem justificativa técnica.
- Não classificar um controle como aprovado apenas pela existência de uma biblioteca, dependência ou arquivo.
- Diferenciar evidências de código, pipeline, implantação e comportamento real.

---

## 01. Tráfego, integração e resiliência

### ARC-001 — Rate Limiting
Identifique limites por IP, usuário, tenant e operação. Avalie respostas HTTP 429, janelas de limitação, bypass por headers confiados e impacto de tráfego distribuído.

**Aplicável quando:** APIs expostas, endpoints custosos, autenticação ou integrações.

### ARC-002 — Caching
Mapeie caches, TTL, isolamento por tenant, consistência, estratégia de chaves e utilização real. Avalie comportamento de cache hit/miss e riscos de exposição de dados.

**Aplicável quando:** Existem leituras repetidas ou dados passíveis de cache.

### ARC-003 — Load Balancing
Valide distribuição de tráfego, roteamento baseado em saúde, afinidade de sessão quando justificada e possíveis pontos únicos de falha.

**Aplicável quando:** Existem múltiplas instâncias ou roteamento entre backends.

### ARC-004 — Reverse Proxies
Valide encaminhamento, TLS, headers, IP de origem, limites de requisição e tratamento de erros.

**Aplicável quando:** Existem proxies como Nginx, Traefik, Cloudflare ou equivalentes.

### ARC-005 — API Gateways
Examine autenticação, roteamento, políticas por rota, throttling e logs. Não imponha um gateway dedicado sem justificativa.

**Aplicável quando:** Existem APIs com gateway ou necessidade arquitetural justificada.

### ARC-006 — CI/CD
Analise pipelines, testes automatizados, gates de qualidade, menor privilégio, proteção de branches, publicação e rollback.

**Aplicável quando:** O projeto possui build ou deploy automatizável.

### ARC-007 — Docker
Inspecione imagens, builds multi-stage, execução como usuário não-root, healthchecks, versões fixadas, SBOM e exposição de secrets durante o build.

**Aplicável quando:** Existem serviços containerizados ou estratégia prevista de containerização.

### ARC-008 — Kubernetes
Analise objetos, limites de recursos, RBAC, policies, quotas, probes e necessidade operacional da plataforma.

**Aplicável quando:** Somente quando o projeto utiliza ou planeja Kubernetes.

### ARC-009 — Service Discovery
Confirme como os serviços localizam suas dependências e se existem endpoints frágeis, inconsistentes ou configurados manualmente de forma inadequada.

**Aplicável quando:** Existem múltiplos serviços ou instâncias com necessidade de descoberta.

### ARC-010 — Circuit Breakers
Verifique mecanismos de proteção de chamadas remotas contra falhas em cascata, incluindo configurações padrão, estados e métricas.

**Aplicável quando:** Existem dependências remotas críticas.

### ARC-011 — Timeouts
Valide timeouts explícitos por etapa de comunicação e deadlines fim a fim. Identifique operações com espera indefinida.

**Aplicável quando:** Existem chamadas externas ou operações de longa duração.

### ARC-012 — Retries
Revise políticas de repetição por classe de erro, orçamento de tentativas e prevenção de repetição de efeitos colaterais.

**Aplicável quando:** Existem operações de I/O sujeitas a falhas transitórias.

### ARC-013 — Exponential Backoff
Verifique crescimento progressivo dos intervalos, limite máximo, jitter e compatibilidade com rate limits.

**Aplicável quando:** Existe política de retry.

### ARC-014 — Idempotency
Confirme uso de chaves de idempotência, deduplicação, escopo e proteção de operações financeiras ou de criação de recursos.

**Aplicável quando:** Existem POSTs com efeitos colaterais, pagamentos, webhooks ou processamento por filas.

### ARC-015 — Message Queues
Confirme semântica de entrega, persistência, acknowledgements, ordenação e monitoramento de lag.

**Aplicável quando:** Existe processamento assíncrono por filas.

### ARC-016 — Pub/Sub
Valide fanout, assinantes, filtros, perda ou duplicação de mensagens e isolamento entre consumidores.

**Aplicável quando:** Eventos são consumidos por múltiplos serviços.

### ARC-017 — Event-Driven Architecture
Verifique contratos de eventos, compatibilidade, correlação e mecanismos de reconciliação.

**Aplicável quando:** A arquitetura é baseada em eventos.

### ARC-018 — Distributed Transactions
Valide consistência entre recursos e decisões de coordenação ou compensação de operações.

**Aplicável quando:** Existem operações que cruzam sistemas independentes.

### ARC-019 — Saga Pattern
Verifique orquestração ou coreografia, compensações e estados de falha.

**Aplicável quando:** Existem transações distribuídas com necessidade de compensação.

### ARC-020 — Dead Letter Queues
Confirme destino de mensagens irrecuperáveis, retenção, alarmes, replay seguro e responsabilidade operacional.

**Aplicável quando:** Filas possuem mensagens com falha permanente.

### ARC-021 — Cron Jobs
Revise timezone, concorrência, idempotência, retries e mecanismos de detecção de execuções perdidas.

**Aplicável quando:** Existem tarefas agendadas.

### ARC-022 — WebSockets
Valide autenticação contínua, fanout, reconexão, heartbeats e limites de conexões.

**Aplicável quando:** Existe comunicação bidirecional persistente.

### ARC-023 — Long Polling
Valide timeouts, consumo de conexões e estratégia de reconexão.

**Aplicável quando:** Long polling é utilizado.

### ARC-024 — Server-Sent Events
Verifique event IDs, reenvio, autenticação, limites e buffering por proxy.

**Aplicável quando:** Existe streaming unidirecional do servidor para o cliente.

---

## 02. Dados, concorrência e escala

### ARC-025 — Database Indexing
Verifique índices para filtros e ordenações críticas utilizando EXPLAIN e avaliando o custo de escrita.

**Aplicável quando:** Existem bancos relacionais ou documentais com suporte a índices.

### ARC-026 — Query Optimization
Revise consultas lentas, planos de execução e regressões utilizando dados representativos.

**Aplicável quando:** Existem consultas persistentes relevantes.

### ARC-027 — N+1 Queries
Procure consultas executadas individualmente dentro de loops. Avalie contagem de queries e possibilidades de batch loading.

**Aplicável quando:** Existem ORM, GraphQL ou acesso relacional.

### ARC-028 — Connection Pooling
Valide pool por processo, limites do banco, vazamentos e risco de explosão de conexões durante autoscaling.

**Aplicável quando:** Existe acesso concorrente a bancos ou conexões.

### ARC-029 — Read Replicas
Verifique atraso de replicação, roteamento de leitura e comportamento de read-after-write.

**Aplicável quando:** Existem réplicas de leitura.

### ARC-030 — Sharding
Verifique chave de distribuição, hot shards, estratégia de resharding e justificativa de escala.

**Aplicável quando:** Sharding existe ou é tecnicamente necessário.

### ARC-031 — Partitioning
Inspecione política de partições, partition pruning, retenção e operações de manutenção.

**Aplicável quando:** Existem tabelas ou datasets particionados, ou candidatos justificáveis.

### ARC-032 — Replication
Valide replicação, RPO, lag, conflitos e recuperação.

**Aplicável quando:** Dados são replicados entre nós ou regiões.

### ARC-033 — Leader Election
Verifique fencing, split-brain, TTL e comportamento diante da perda do líder.

**Aplicável quando:** Workers ou control planes utilizam eleição de líder.

### ARC-034 — CAP Theorem
Documente o comportamento do sistema durante partições de rede e os trade-offs entre disponibilidade e consistência.

**Aplicável quando:** Existe sistema distribuído sujeito a partições.

### ARC-035 — Eventual Consistency
Valide experiência do usuário, reconciliação, limites de staleness e idempotência.

**Aplicável quando:** Existem sistemas assíncronos ou replicados.

### ARC-036 — Optimistic Locking
Confirme mecanismos de compare-and-swap ou versionamento e tratamento de conflitos visível ao cliente.

**Aplicável quando:** Existem atualizações concorrentes com versionamento.

### ARC-037 — Pessimistic Locking
Revise escopo, duração dos locks, ordem de aquisição e bloqueios.

**Aplicável quando:** Existem transações com bloqueios explícitos.

### ARC-038 — Distributed Locks
Verifique lock leasing, fencing, renovação, liberação e comportamento em falhas de rede.

**Aplicável quando:** Existe coordenação entre múltiplos processos.

### ARC-039 — Race Conditions
Inspecione operações check-then-act, workers e requisições simultâneas.

**Aplicável quando:** Existe estado mutável compartilhado.

### ARC-040 — Deadlocks
Revise ordem de aquisição de locks, detecção e retries seguros.

**Aplicável quando:** Existem transações ou bloqueios concorrentes.

### ARC-041 — Memory Leaks
Avalie listeners, intervalos, caches sem limite e crescimento de heap.

**Aplicável quando:** Existem processos de longa duração.

### ARC-042 — Garbage Collection
Verifique pausas, pressão de memória e tuning justificado, considerando as características da runtime.

**Aplicável quando:** A runtime utiliza gerenciamento automático de memória.

### ARC-043 — Thread Safety
Revise objetos globais, estado compartilhado, workers e mecanismos de exclusão mútua.

**Aplicável quando:** Existe concorrência por threads ou processos.

### ARC-044 — Backpressure
Verifique limitação de entrada, buffers, quotas e sinais de sobrecarga.

**Aplicável quando:** Existem streams, filas, workers ou tráfego variável.

### ARC-045 — Autoscaling
Valide sinais de escala, limites mínimos e máximos, cooldown, limites de custos e testes.

**Aplicável quando:** Recursos possuem escala automática.

### ARC-046 — Horizontal Scaling
Verifique estado externo, sessões, jobs únicos e independência entre instâncias.

**Aplicável quando:** Workloads operam com múltiplas réplicas.

### ARC-047 — Vertical Scaling
Valide capacidade, limites de máquina e plano de crescimento.

**Aplicável quando:** Workloads são dimensionados por CPU ou memória.

### ARC-048 — CDN
Valide distribuição de conteúdo estático, TTL, invalidação e exposição indevida de conteúdo privado.

**Aplicável quando:** Existem assets públicos que se beneficiam de distribuição global.

### ARC-049 — Edge Caching
Inspecione chaves, autenticação, cache-control e riscos de vazamento entre usuários ou tenants.

**Aplicável quando:** Existe cache no edge ou CDN.

### ARC-050 — Cache Invalidation
Verifique estratégia de invalidação após escrita, TTL e consistência de versões.

**Aplicável quando:** Existe cache com dados mutáveis.

---

## 03. Entrega e observabilidade

### ARC-051 — Feature Flags
Valide controle de acesso, valores padrão, limpeza de flags e kill switch.

**Aplicável quando:** Existem lançamentos ou experiências controladas por flags.

### ARC-052 — Blue-Green Deployment
Confirme estratégia, preparação de dados e troca segura de tráfego.

**Aplicável quando:** Blue-green é utilizado ou planejado.

### ARC-053 — Canary Releases
Valide percentuais de tráfego, métricas de promoção e mecanismos de aborto automático ou manual.

**Aplicável quando:** Existem deploys canários.

### ARC-054 — Rolling Deployments
Verifique compatibilidade entre versões e parâmetros como maxUnavailable e maxSurge.

**Aplicável quando:** Existem deploys progressivos em múltiplas instâncias.

### ARC-055 — Rollbacks
Verifique reversão de código, configuração e compatibilidade de migrações.

**Aplicável quando:** Existe entrega para produção.

### ARC-056 — Health Checks
Verifique endpoints e sua representatividade da saúde real da aplicação.

**Aplicável quando:** Existem serviços HTTP ou daemons.

### ARC-057 — Liveness & Readiness Probes
Verifique separação entre probes e evite mascarar dependências ou provocar reinícios em cascata.

**Aplicável quando:** Existem orquestradores com liveness e readiness.

### ARC-058 — Monitoring
Verifique monitores dos fluxos críticos e cobertura da infraestrutura.

**Aplicável quando:** O sistema opera com usuários.

### ARC-059 — Logging
Valide correlação, níveis, retenção, mascaramento e ausência de dados pessoais ou segredos.

**Aplicável quando:** Existe execução em produção.

### ARC-060 — Distributed Tracing
Confirme propagação de trace IDs entre fronteiras e estratégia de sampling.

**Aplicável quando:** Existem microsserviços ou terceiros relevantes.

### ARC-061 — Metrics
Verifique taxa de requisições, erros, duração, saturação e controle de cardinalidade das dimensões.

**Aplicável quando:** O sistema opera em produção.

### ARC-062 — Alerts
Valide alertas acionáveis, severidade, destino, deduplicação e testes.

**Aplicável quando:** Existem sistemas com operação assistida.

### ARC-063 — SLOs
Confirme metas por jornada e janela temporal, vinculadas ao impacto de negócio.

**Aplicável quando:** Serviços possuem compromissos de confiabilidade.

### ARC-064 — SLIs
Valide indicadores, numerador, denominador e instrumentação correta.

**Aplicável quando:** Serviços são medidos por confiabilidade.

### ARC-065 — Error Budgets
Revise cálculo, política de utilização e decisões sobre velocidade de releases.

**Aplicável quando:** Existem equipes que adotam SLOs.

### ARC-066 — Observability
Avalie a capacidade de explicar anomalias por meio de logs, métricas e traces correlacionados.

**Aplicável quando:** O sistema exige capacidade de diagnóstico operacional.

---

## 04. Segurança

### ARC-067 — Secrets Management
Procure segredos expostos, mecanismos de rotação, escopos, CI e entrega em runtime. Nunca imprima valores de credenciais.

**Aplicável quando:** Toda aplicação que utiliza credenciais.

### ARC-068 — IAM
Revise roles, MFA quando aplicável, permissões mínimas e credenciais de serviço.

**Aplicável quando:** Existem contas de nuvem, service accounts ou usuários.

### ARC-069 — OAuth
Valide flow, state, PKCE, redirect URI, scopes e gerenciamento de tokens.

**Aplicável quando:** OAuth é utilizado.

### ARC-070 — JWT Rotation
Verifique expiração, rotação de chaves, refresh tokens, revogação e validação de issuer e audience.

**Aplicável quando:** JWT ou tokens equivalentes são utilizados.

### ARC-071 — TLS
Verifique versões, certificados, terminação e política de HTTPS.

**Aplicável quando:** Existem comunicações protegidas por TLS.

### ARC-072 — Encryption at Rest
Confirme criptografia, gerenciamento de chaves e cobertura de bancos, backups e objetos armazenados.

**Aplicável quando:** Existem dados sensíveis ou persistidos.

### ARC-073 — Encryption in Transit
Valide criptografia em todos os hops, incluindo comunicações internas e integrações com terceiros.

**Aplicável quando:** Existem dados confidenciais em trânsito.

### ARC-074 — WAF
Verifique regras, bypass, falsos positivos e evidências da camada de edge.

**Aplicável quando:** Aplicações públicas possuem WAF.

### ARC-075 — DDoS Protection
Verifique mecanismos de mitigação no provedor, limites de origem e dependências.

**Aplicável quando:** Existem serviços expostos publicamente.

### ARC-076 — CORS
Audite allowlist de origens, credenciais e reflexos perigosos.

**Aplicável quando:** APIs são consumidas por browsers.

### ARC-077 — CSRF
Valide proteção baseada em cookies e métodos mutáveis. Analise SameSite e tokens anti-CSRF.

**Aplicável quando:** Aplicações utilizam autenticação via cookies.

### ARC-078 — SQL Injection
Inspecione queries parametrizadas, interpolação e validação de dados externos.

**Aplicável quando:** Existem consultas SQL com entrada externa.

### ARC-079 — XSS
Valide output encoding, sanitização e CSP, com atenção especial a HTML dinâmico.

**Aplicável quando:** Dados não confiáveis são renderizados.

### ARC-080 — SSRF
Inspecione fetch de URLs, allowlists, redirects e acesso a metadata de nuvem.

**Aplicável quando:** Aplicações requisitam recursos indicados pelo usuário.

---

## 05. Recuperação e plataforma

### ARC-081 — Database Migrations
Revise migrations auditáveis, backward compatibility, ordem de deploy e rollback de schema.

**Aplicável quando:** Bancos possuem schema versionado.

### ARC-082 — Schema Versioning
Valide compatibilidade entre versões de dados e clientes.

**Aplicável quando:** Existem evolução de esquemas e contratos.

### ARC-083 — Disaster Recovery
Verifique runbooks, responsáveis, RTO, RPO, simulações e dependências.

**Aplicável quando:** Sistemas críticos operam em produção.

### ARC-084 — Backups
Confirme política, retenção, criptografia e teste documentado de restauração.

**Aplicável quando:** Existem dados persistentes críticos.

### ARC-085 — Failover
Valide mudança de primário, testes e mecanismos de reconexão.

**Aplicável quando:** Recursos redundantes possuem failover.

### ARC-086 — Multi-Region Deployment
Avalie necessidade, replicação, roteamento, consistência e custo.

**Aplicável quando:** Existe exigência e arquitetura multirregião.

### ARC-087 — Chaos Engineering
Verifique experimentos seguros, hipóteses, limites e observação.

**Aplicável quando:** Sistemas maduros possuem ambiente isolado para experimentação.

### ARC-088 — Cost Optimization
Compare utilização e custos, recursos ociosos, limites e oportunidades de otimização sem introduzir riscos.

**Aplicável quando:** Existem infraestruturas ou serviços pagos.

### ARC-089 — Cold Starts
Valide latência e mitigação de inicialização de funções ou containers.

**Aplicável quando:** Existe serverless ou scale-to-zero.

### ARC-090 — Serverless Limits
Confirme timeout, memória, concorrência, tamanho de payload e quotas.

**Aplicável quando:** Existem ambientes serverless.

---

## 06. Rede, contratos e performance

### ARC-091 — Latency
Analise latência ponta a ponta por caminho crítico, região e percentis.

**Aplicável quando:** Existem serviços com requisições.

### ARC-092 — Throughput
Avalie capacidade sustentada, gargalos e limites conhecidos.

**Aplicável quando:** O sistema possui volume mensurável.

### ARC-093 — P99 Latency
Valide P99 por endpoint ou jornada sob volume relevante.

**Aplicável quando:** Existem serviços sensíveis à cauda de latência.

### ARC-094 — Tail Latency
Investigue fontes de picos, dependências e filas no extremo da distribuição.

**Aplicável quando:** O sistema apresenta variabilidade de tempo de resposta.

### ARC-095 — Network Partitions
Confirme comportamento diante de perdas de conectividade, retries e consistência.

**Aplicável quando:** Existem sistemas distribuídos ou dependências remotas.

### ARC-096 — Clock Skew
Verifique sincronização e tolerância de expiração, assinatura e event-time.

**Aplicável quando:** Existem tokens, certificados ou processos distribuídos.

### ARC-097 — DNS
Revise TTL, failover, registros, timeouts e resolução.

**Aplicável quando:** Serviços se comunicam por DNS.

### ARC-098 — TCP vs UDP
Confirme utilização e implicações dos protocolos de transporte quando pertinente.

**Aplicável quando:** Existem protocolos de rede relevantes.

### ARC-099 — HTTP/2 & HTTP/3
Verifique negociação, proxies, limites, compatibilidade e fallback.

**Aplicável quando:** APIs ou aplicações web utilizam protocolos negociados.

### ARC-100 — GRPC
Analise deadlines, streaming, retries e contratos protobuf.

**Aplicável quando:** gRPC é utilizado.

### ARC-101 — Webhooks
Valide assinatura, timestamp, deduplicação, retries e respostas HTTP 2xx e 4xx.

**Aplicável quando:** Existem integrações por webhook.

### ARC-102 — API Versioning
Valide compatibilidade, depreciação e governança de contratos.

**Aplicável quando:** Existem APIs consumidas externamente.

### ARC-103 — Semantic Versioning
Valide política de versionamento, tags e mudanças incompatíveis.

**Aplicável quando:** Existem artefatos ou bibliotecas com releases versionadas.

---

## 07. Operações e infraestrutura como código

### ARC-104 — Infrastructure as Code
Revise drift, revisão por PR, state, segredos e controle de mudanças.

**Aplicável quando:** A infraestrutura possui provisionamento definido.

### ARC-105 — Terraform
Valide provider pinning, estado, plan, políticas e módulos.

**Aplicável quando:** Terraform é utilizado.

### ARC-106 — Helm Charts
Valide templates, values, secrets, versionamento e rollbacks.

**Aplicável quando:** Helm é utilizado.

### ARC-107 — Build Caching
Verifique cache keys e invalidação determinística, evitando mistura de artefatos.

**Aplicável quando:** Pipelines de build utilizam cache.

### ARC-108 — Dependency Hell
Audite lockfiles, conflitos, versões, CVEs e política de atualização.

**Aplicável quando:** O projeto possui dependências externas.

### ARC-109 — Production Incidents
Verifique classificação, timeline, resolução e registros de incidentes.

**Aplicável quando:** Existem serviços em produção.

### ARC-110 — On-Call
Valide escala, ownership, escalonamento e runbooks.

**Aplicável quando:** Sistemas críticos possuem plantão operacional.

### ARC-111 — Postmortems
Analise RCA sem atribuição de culpa, ações corretivas, responsáveis e verificação das correções.

**Aplicável quando:** Já ocorreram incidentes relevantes.

---

## Regras de utilização do catálogo

### 1. Aplicabilidade

Antes de avaliar cada controle, classifique sua aplicabilidade:

- `APLICAVEL`: o controle é pertinente à arquitetura analisada.
- `NAO_APLICAVEL`: existe justificativa arquitetural concreta para sua não aplicação.
- `INDETERMINADA`: faltam informações para decidir.

A ausência de uma tecnologia não é, isoladamente, justificativa para `NAO_APLICAVEL`.

### 2. Status de avaliação

Utilize exclusivamente:

- `PASS_VERIFIED`: controle implementado e validado por evidência suficiente.
- `PARTIAL`: existe implementação real, mas incompleta ou insuficiente.
- `FAIL`: falha ou ausência demonstrável em controle aplicável.
- `NOT_VERIFIED`: não existem evidências suficientes para concluir.
- `NOT_APPLICABLE`: controle comprovadamente não aplicável.

### 3. Evidências

Cada avaliação deve apresentar, quando disponíveis:

- Caminho e linhas do código.
- Configurações e recursos envolvidos.
- Testes e resultados.
- Logs, métricas e traces.
- Ambiente e método de validação.
- Limitações de acesso e confiança da conclusão.

### 4. Princípio de conclusão

A auditoria deve contemplar os 111 controles, mesmo quando alguns forem não aplicáveis ou não verificáveis.

A soma dos resultados por status deve totalizar exatamente 111.

Nenhuma conclusão de prontidão para produção deve ser baseada exclusivamente em evidências estáticas quando a validação operacional for necessária.
