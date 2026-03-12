# ============================================================
# SRS em Python — FIAP Marketplace
# Aula 04 — Engenharia de Software · FIAP
# ============================================================

from dataclasses import dataclass, field
from typing import List
from enum import Enum


class Prioridade(Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"


@dataclass
class RequisitoFuncional:
    id: str
    nome: str
    descricao: str
    prioridade: Prioridade
    ator: str
    pre_condicao: str
    pos_condicao: str


@dataclass
class RequisitoNaoFuncional:
    id: str
    categoria: str
    descricao: str
    criterio_aceitacao: str


@dataclass
class SRS:
    projeto: str
    versao: str
    descricao: str
    requisitos_funcionais: List[RequisitoFuncional] = field(default_factory=list)
    requisitos_nao_funcionais: List[RequisitoNaoFuncional] = field(default_factory=list)

    def adicionar_rf(self, req: RequisitoFuncional):
        self.requisitos_funcionais.append(req)
        print(f"✅ RF '{req.id}' adicionado!")

    def adicionar_rnf(self, req: RequisitoNaoFuncional):
        self.requisitos_nao_funcionais.append(req)
        print(f"✅ RNF '{req.id}' adicionado!")

    def relatorio(self):
        print(f"\n{'='*50}")
        print(f" SRS — {self.projeto} v{self.versao}")
        print(f"{'='*50}")
        print(f" {self.descricao}\n")

        print(f" REQUISITOS FUNCIONAIS ({len(self.requisitos_funcionais)})")
        for rf in self.requisitos_funcionais:
            print(f"  [{rf.id}] {rf.nome} — Prioridade: {rf.prioridade.value}")
            print(f"       Ator: {rf.ator}")
            print(f"        {rf.descricao}\n")

        print(f" REQUISITOS NÃO-FUNCIONAIS ({len(self.requisitos_nao_funcionais)})")
        for rnf in self.requisitos_nao_funcionais:
            print(f"  [{rnf.id}] {rnf.categoria}")
            print(f"        {rnf.descricao}")
            print(f"         Critério: {rnf.criterio_aceitacao}\n")


# ============================================================
# Função de validação de requisitos
# ============================================================

def validar_requisito(rf: RequisitoFuncional) -> dict:
    """
    Valida se um requisito funcional segue boas práticas.
    """

    resultados = {}

    resultados["descricao_valida"] = len(rf.descricao) > 20

    resultados["pre_condicao_definida"] = rf.pre_condicao.strip() != ""

    resultados["criterio_mensuravel"] = any(char.isdigit() for char in rf.descricao)

    return resultados

def exportar_markdown(srs: SRS) -> str:
    """
    Exporta o SRS para formato Markdown.
    """

    md = ""

    md += f"# SRS — {srs.projeto}\n"
    md += f"**Versão:** {srs.versao}\n\n"
    md += f"## Descrição\n{srs.descricao}\n\n"

    md += "## Requisitos Funcionais\n\n"

    for rf in srs.requisitos_funcionais:
        md += f"### {rf.id} — {rf.nome}\n"
        md += f"- **Prioridade:** {rf.prioridade.value}\n"
        md += f"- **Ator:** {rf.ator}\n"
        md += f"- **Descrição:** {rf.descricao}\n"
        md += f"- **Pré-condição:** {rf.pre_condicao}\n"
        md += f"- **Pós-condição:** {rf.pos_condicao}\n\n"

    md += "## Requisitos Não Funcionais\n\n"

    for rnf in srs.requisitos_nao_funcionais:
        md += f"### {rnf.id} — {rnf.categoria}\n"
        md += f"- **Descrição:** {rnf.descricao}\n"
        md += f"- **Critério de aceitação:** {rnf.criterio_aceitacao}\n\n"

    return md


# ============================================================
# Criando o SRS do FIAP Marketplace
# ============================================================

srs = SRS(
    projeto="FIAP Marketplace",
    versao="1.0",
    descricao="Marketplace interno onde alunos podem vender produtos artesanais entre si."
)

# ------------------------------------------------------------
# REQUISITOS FUNCIONAIS
# ------------------------------------------------------------

srs.adicionar_rf(RequisitoFuncional(
    id="RF-001",
    nome="Cadastro de Produto",
    descricao="Permitir que alunos vendedores cadastrem produtos com nome, preço e categoria.",
    prioridade=Prioridade.ALTA,
    ator="Aluno Vendedor",
    pre_condicao="Usuário autenticado no sistema",
    pos_condicao="Produto disponível no marketplace"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-002",
    nome="Busca por Categoria",
    descricao="Permitir que usuários busquem produtos por categoria com retorno em até 2 segundos.",
    prioridade=Prioridade.MEDIA,
    ator="Aluno Comprador",
    pre_condicao="Usuário acessando o marketplace",
    pos_condicao="Lista de produtos exibida na tela"
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-003",
    nome="Checkout de Compra",
    descricao="Permitir que usuários finalizem compras após adicionar produtos ao carrinho.",
    prioridade=Prioridade.ALTA,
    ator="Aluno Comprador",
    pre_condicao="Produto adicionado ao carrinho",
    pos_condicao="Pedido registrado no sistema"
))


# ------------------------------------------------------------
# REQUISITOS NÃO FUNCIONAIS
# ------------------------------------------------------------

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-001",
    categoria="Disponibilidade",
    descricao="O sistema deve possuir disponibilidade mínima de 99.9%.",
    criterio_aceitacao="Monitoramento de uptime maior ou igual a 99.9%"
))

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-002",
    categoria="Segurança",
    descricao="O sistema deve garantir proteção dos dados dos usuários conforme LGPD.",
    criterio_aceitacao="Auditoria de conformidade com LGPD"
))


# ============================================================
# RELATÓRIO DO SRS
# ============================================================

srs.relatorio()


# ============================================================
# TESTANDO A VALIDAÇÃO DOS REQUISITOS
# ============================================================

print("\n Validação dos Requisitos Funcionais\n")

for rf in srs.requisitos_funcionais:
    resultado = validar_requisito(rf)
    print(f"{rf.id} → {resultado}")

    markdown = exportar_markdown(srs)

print("\n SRS em Markdown:\n")
print(markdown)

markdown = exportar_markdown(srs)

with open("srs_fiap_marketplace.md", "w", encoding="utf-8") as arquivo:
    arquivo.write(markdown)

print(" Arquivo Markdown gerado com sucesso!")