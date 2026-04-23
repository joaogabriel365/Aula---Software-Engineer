# SRS — FIAP Marketplace
**Versão:** 1.0

## Descrição
Marketplace interno onde alunos podem vender produtos artesanais entre si.

## Requisitos Funcionais

### RF-001 — Cadastro de Produto
- **Prioridade:** Alta
- **Ator:** Aluno Vendedor
- **Descrição:** Permitir que alunos vendedores cadastrem produtos com nome, preço e categoria.
- **Pré-condição:** Usuário autenticado no sistema
- **Pós-condição:** Produto disponível no marketplace

### RF-002 — Busca por Categoria
- **Prioridade:** Média
- **Ator:** Aluno Comprador
- **Descrição:** Permitir que usuários busquem produtos por categoria com retorno em até 2 segundos.
- **Pré-condição:** Usuário acessando o marketplace
- **Pós-condição:** Lista de produtos exibida na tela

### RF-003 — Checkout de Compra
- **Prioridade:** Alta
- **Ator:** Aluno Comprador
- **Descrição:** Permitir que usuários finalizem compras após adicionar produtos ao carrinho.
- **Pré-condição:** Produto adicionado ao carrinho
- **Pós-condição:** Pedido registrado no sistema

## Requisitos Não Funcionais

### RNF-001 — Disponibilidade
- **Descrição:** O sistema deve possuir disponibilidade mínima de 99.9%.
- **Critério de aceitação:** Monitoramento de uptime maior ou igual a 99.9%

### RNF-002 — Segurança
- **Descrição:** O sistema deve garantir proteção dos dados dos usuários conforme LGPD.
- **Critério de aceitação:** Auditoria de conformidade com LGPD

