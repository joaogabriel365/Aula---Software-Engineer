from app.banco_de_dados import BancoDeDados

class ServidorNubank:
    def __init__(self):
        self.banco = BancoDeDados()

    def processar_transferencia(self, user_id: str, valor: float) -> dict:
        saldo = self.banco.verificar_saldo(user_id)

        if saldo >= valor:
            self.banco.debitar(user_id, valor)
            saldo_restante = self.banco.verificar_saldo(user_id)

            return {
                "status": "aprovado",
                "saldo_restante": saldo_restante
            }
        else:
            return {
                "status": "recusado",
                "motivo": "saldo insuficiente"
            }