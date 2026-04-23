def cadastro_usuario(email: str, senha: str, email_ja_existe: bool, confirmou_email: bool) -> str:
    # 1. Validar se email tem formato correto (Decisão 1 do seu diagrama)
    if "@" not in email or "." not in email:
        return "Erro: E-mail com formato inválido."

    # 2. Verificar se email já está cadastrado (Decisão 2 do seu diagrama)
    if email_ja_existe:
        return "Erro: E-mail já cadastrado no sistema."

    # 3. Criar conta e 4. Enviar e-mail de confirmação (Ações do Sistema)
    # Aqui simulamos que o sistema processou o cadastro e enviou o link
    
    # 5. Aguardar confirmação (Ação do Usuário no seu diagrama)
    if not confirmou_email:
        return "Cadastro pendente: Por favor, confirme seu e-mail."

    # 6. Liberar acesso (Ação final do Sistema)
    return f"Sucesso! Acesso liberado para o usuário {email}."

# --- Testes para validar o fluxo ---

# Caso 1: Tudo certo (Sucesso)
print(cadastro_usuario("jgbortoli@email.com", "240306", False, True)) 

# Caso 2: E-mail mal escrito (Cai na primeira decisão)
print(cadastro_usuario("email-invalido", "240306", False, True)) 

# Caso 3: Usuário já existe (Cai na segunda decisão)
print(cadastro_usuario("jgbortoli@email.com", "240306", True, True))

# Caso 4: E-mail válido mas usuário não clicou no link (Pendente)
print(cadastro_usuario("usuario@email.com", "123456", False, False))