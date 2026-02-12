class ContaBancaria:
    # Atributo de classe: compartilhado por todas as contas
    taxa_juros = 0.05

    def __init__(self, titular: str, saldo: float)->None:
        self.titular = titular
        self.saldo = saldo

    def calcular_juros(self):
        """Calcula o valor do juro baseado no saldo atual e na taxa da classe."""
        valor_juros = self.saldo * ContaBancaria.taxa_juros
        return valor_juros

    def aplicar_juros(self):
        """Adiciona os juros ao saldo da conta."""
        juros = self.calcular_juros()
        self.saldo += juros
        print(f"Juros de R${juros:.2f} aplicados à conta de {self.titular}.")

    def __str__(self) -> str:
        """Define como o objeto será exibido ao usar print()."""
        return (
            f"\n--- Dados da Conta ---"
            f"\nTitular: {self.titular}"
            f"\nSaldo Atual: R${self.saldo:.2f}"
            f"\nTaxa de Juros: {ContaBancaria.taxa_juros * 100}%"
            f"\nValor dos Juros: R${self.calcular_juros():.2f}"
            f"\n----------------------"
        )