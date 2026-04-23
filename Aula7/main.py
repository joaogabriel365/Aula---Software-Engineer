from app.app_nubank import AppNubank

app = AppNubank()

print("=== Teste 1: Transferência dentro do saldo ===")
app.transferir("user_123", 200.0)

print("\n=== Teste 2: Transferência acima do saldo ===")
app.transferir("user_123", 500.0)

print("\n=== Teste 3: Múltiplas transferências ===")
app.transferir("user_123", 100.0)
app.transferir("user_123", 250.0)