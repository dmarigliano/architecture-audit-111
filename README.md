# Architecture Audit 111

**Skill para Claude e OpenAI Codex que audita aplicações SaaS contra 111 controles de arquitetura, segurança e operação (ARC-001 a ARC-111) e aponta o que precisa ser corrigido, ajustado, melhorado ou criado.**

*English summary: an Agent Skill for Claude (Claude.ai, Claude Code) and OpenAI Codex that runs a read-only, evidence-based architecture audit of SaaS applications (especially AI-assisted / "vibe-coded" ones) against a 111-control catalog, and returns a prioritized action backlog plus a project-closure verdict. Instructions and catalog are in Brazilian Portuguese.*

## Para que serve

Pensado para o **fechamento de projetos de software**, em especial aplicações criadas com apoio de IA (Lovable, Replit, Codex, Cursor e similares). O agente:

- audita individualmente os 111 controles, com evidência rastreável (arquivo e linha, configuração, teste);
- separa evidência de **código**, **pipeline** e **produção**, e nunca confunde ausência de evidência com falha (`NOT_VERIFIED`);
- gera, para cada pendência, uma **ação tipada**: `CORRIGIR`, `AJUSTAR`, `CRIAR`, `MELHORAR` ou `VERIFICAR`;
- avalia oito áreas transversais (multi-tenancy, autenticação, APIs e webhooks, prompt injection, pagamentos, LGPD, custos, frontend/backoffice) e, se houver, WhatsApp;
- entrega um **parecer de fechamento** (apto, apto com ressalvas ou não apto) e uma planilha de evidências;
- é **somente diagnóstico**: não altera código, banco nem configuração sem autorização expressa.

## O que acompanha

| Item | Caminho |
|------|---------|
| Instruções do skill | `skills/architecture-audit-111/SKILL.md` |
| Catálogo dos 111 controles (fonte de verdade) | `skills/architecture-audit-111/references/controls.md` |
| Template da Evidence Matrix (.xlsx) | `skills/architecture-audit-111/assets/evidence-matrix-template.xlsx` |
| Validador (catálogo e matriz) | `skills/architecture-audit-111/scripts/validate_catalog.py` |
| Casos de teste e projeto fictício | `skills/architecture-audit-111/evals/` |

Grupos do catálogo: tráfego, integração e resiliência (24) · dados, concorrência e escala (26) · entrega e observabilidade (16) · segurança (14) · recuperação e plataforma (10) · rede, contratos e performance (13) · operações e infraestrutura como código (8).

## Instalação

### Claude.ai e Claude Desktop
1. Baixe [`architecture-audit-111.zip`](https://github.com/dmarigliano/architecture-audit-111/releases/latest/download/architecture-audit-111.zip) na página de [**Releases**](https://github.com/dmarigliano/architecture-audit-111/releases) deste repositório. Não use o botão "Download ZIP" do código: ele embrulha o repositório inteiro e o envio é recusado.
2. No Claude, vá em **Customize > Skills** (em contas mais antigas, **Settings > Capabilities**), crie um skill e escolha **Upload a skill**.
3. Envie o ZIP e deixe o skill ativado.

Requisitos: um plano com suporte a skills e **Code execution and file creation** habilitado. Em planos Team e Enterprise, o administrador precisa habilitar Skills na organização. Detalhes atualizados no [Help Center](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### Claude Code
Copie a pasta do skill para o diretório de skills:

```bash
git clone https://github.com/dmarigliano/architecture-audit-111.git
cd architecture-audit-111
mkdir -p ~/.claude/skills
cp -R skills/architecture-audit-111 ~/.claude/skills/
```

Para valer só em um projeto, use `.claude/skills/` na raiz dele. Documentação: [Claude Code, Skills](https://code.claude.com/docs/en/skills).

### OpenAI Codex
O Codex usa o mesmo formato (`SKILL.md`). Copie a pasta do skill para o diretório de skills do usuário:

```bash
git clone https://github.com/dmarigliano/architecture-audit-111.git
cd architecture-audit-111
mkdir -p ~/.agents/skills
cp -R skills/architecture-audit-111 ~/.agents/skills/
```

Para valer só em um repositório, use `.agents/skills/` na raiz dele. Se o skill não aparecer, reinicie o Codex. Fora do Claude.ai, a planilha de evidências é preenchida com `openpyxl` (`pip install openpyxl`). Documentação: [Codex, Agent Skills](https://developers.openai.com/codex/skills).

### Gerar o ZIP você mesmo
```bash
bash scripts/package.sh   # cria dist/architecture-audit-111.zip
```

## Como usar

Com o skill ativo, descreva o pedido e disponibilize o código (e, se tiver, pipeline, IaC, configuração e dados de produção). Exemplos:

- "Faça a auditoria Architecture Audit 111 completa deste projeto para o fechamento."
- "Só tenho o repositório. Audite os controles de segurança (ARC-067 a ARC-080)."
- "Reaudite o projeto e compare com a auditoria anterior."

Quanto mais acesso o agente tiver (produção, CI/CD, provedor de nuvem), menos controles ficam `NOT_VERIFIED`. A planilha e a validação final seguem o fluxo descrito em `SKILL.md`.

## Validação

```bash
cd skills/architecture-audit-111
python scripts/validate_catalog.py                       # integridade do catálogo (111 IDs únicos, 24/26/16/14/10/13/8)
python scripts/validate_catalog.py --matrix minha-matriz.xlsx   # confere 111 linhas, nomes do catálogo e soma de status = 111
```

O validador de matriz em `.xlsx` precisa da biblioteca `openpyxl` (`pip install openpyxl`).

## Limitações importantes

- O skill é um **apoio técnico**, não substitui teste de intrusão, revisão de segurança por especialistas, nem parecer jurídico ou de conformidade (LGPD, PCI DSS etc.).
- A lista de **controles críticos** (26) usada no parecer é uma **proposta de trabalho**, não faz parte do catálogo: ajuste conforme o contexto.
- O catálogo é uma diretriz de inspeção, não prova de conformidade.
- Regras e detalhes de plataformas externas (por exemplo WhatsApp) mudam; o agente marca como `NOT_VERIFIED` o que depende de documentação vigente que ele não consultou.
- Validado até agora apenas em um caso de teste com projeto fictício; feedback com projetos reais é bem-vindo.

## Contribuindo

Issues e pull requests são bem-vindos. Ao propor mudanças no catálogo, preserve os IDs `ARC-001` a `ARC-111` (são estáveis para comparar auditorias) e rode o validador antes de enviar.

## Licença

[MIT](LICENSE) © 2026 Daniel Marigliano.
