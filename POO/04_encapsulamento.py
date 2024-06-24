class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo  # '_' no inicio define encapsulamento, e portanto privado
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

    def __str__(self):
        return (
            f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        )


conta = Conta(nro_agencia="0001", saldo=100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
