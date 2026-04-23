catalogo = [
    {"titulo": "Design PatternsClean Code", "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "The Pragmatic Programmer", "autor": "Hunt & Thomas", "disponivel": True},
    {"titulo": "Design Patterns", "autor": "Gang of Four", "disponivel": True},
]

emprestimos = []

# ============================================================
# UC-01: LISTAR CATÁLOGO
# ============================================================
print("📚 Catálogo disponível:")
for livro in catalogo:
    status = "✅" if livro["disponivel"] else "❌"
    print(f"  {status} {livro['titulo']} — {livro['autor']}")

# ============================================================
# UC-02: BUSCAR LIVRO
# ============================================================
print("\n🔍 Buscando livro...")
busca = input("Digite o nome do livro: ")

encontrados = False

for livro in catalogo:
    if busca.lower() in livro["titulo"].lower():
        status = "✅" if livro["disponivel"] else "❌"
        print(f"  {status} {livro['titulo']} — {livro['autor']}")
        encontrados = True

if not encontrados:
    print("❌ Nenhum livro encontrado.")

# ============================================================
# UC-03: EMPRESTAR LIVRO
# ============================================================
print("\n📌 Empréstimo:")
leitor = input("Digite seu nome: ")
titulo = input("Digite o título do livro que deseja: ")

livro_encontrado = None

for livro in catalogo:
    if livro["titulo"].lower() == titulo.lower():
        livro_encontrado = livro
        break

if livro_encontrado is None:
    print("❌ Livro não encontrado no catálogo.")

elif not livro_encontrado["disponivel"]:
    print(f"⚠️ '{livro_encontrado['titulo']}' já está emprestado!")

else:
    livro_encontrado["disponivel"] = False
    emprestimos.append({
        "leitor": leitor,
        "livro": livro_encontrado["titulo"]
    })
    print(f"✅ '{livro_encontrado['titulo']}' emprestado para {leitor}!")

# ============================================================
# UC-04: DEVOLVER LIVRO
# ============================================================
print("\n🔄 Devolução:")
leitor_devolvendo = input("Quem está devolvendo o livro? ")
titulo_devolvendo = input("Qual livro deseja devolver? ")

registro_encontrado = None

# 1. procurar o empréstimo
for emp in emprestimos:
    if emp["leitor"].lower() == leitor_devolvendo.lower() and emp["livro"].lower() == titulo_devolvendo.lower():
        registro_encontrado = emp
        break

# 2. se encontrou, marcar livro como disponível
if registro_encontrado:
    for livro in catalogo:
        if livro["titulo"].lower() == titulo_devolvendo.lower():
            livro["disponivel"] = True
            break

    # remover empréstimo
    emprestimos.remove(registro_encontrado)

    print(f"✅ '{titulo_devolvendo}' devolvido com sucesso!")

    # multa
    atraso = input("O livro foi devolvido com atraso? (s/n): ").lower()
    if atraso == "s":
        print("📋 Multa aplicada!")

# 3. se não encontrou
else:
    print("❌ Empréstimo não encontrado.")

# ============================================================
# ESTADO FINAL
# ============================================================
print("\n📖 Catálogo após operações:")
for livro in catalogo:
    status = "✅" if livro["disponivel"] else "❌"
    print(f"  {status} {livro['titulo']}")

print(f"\n📋 Empréstimos ativos: {emprestimos}")