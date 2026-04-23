from app.servidor import ServidorNubank

class AppNubank:
    def __init__(self):
        self.servidor = ServidorNubank()

    def transferir(self, user_id: str, valor: float):
        print(f"[APP] Iniciando transferência de R$ {valor:.2f}...")

        resultado = self.servidor.processar_transferencia(user_id, valor)

        if resultado["status"] == "aprovado":
            print(f"[APP] ✅ Transferência aprovada! Saldo: R$ {resultado['saldo_restante']:.2f}")
        else:
            print(f"[APP] ❌ Transferência recusada: {resultado['motivo']}")