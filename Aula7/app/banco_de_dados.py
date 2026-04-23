class BancoDeDados:
    def __init__(self):
        self.saldos = {
            "user_123": 500.0
        }

    def verificar_saldo(self, user_id: str) -> float:
        return self.saldos.get(user_id, 0.0)

    def debitar(self, user_id: str, valor: float) -> bool:
        saldo = self.verificar_saldo(user_id)

        if saldo >= valor:
            self.saldos[user_id] -= valor
            return True
        else:
            return False