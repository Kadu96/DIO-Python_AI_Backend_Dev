class Bicicleta:  # definindo uma classe
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("Plim PLim Plim")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmm...")

    # def __str__(self) -> str:
    #    return f"Bicicleta: cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano}, valor= {self.valor}"

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}:{', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        )


b1 = Bicicleta("vermelha", "caloi", 2022, 600)

b1.buzinar()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
print()

b2 = Bicicleta("verde", "monark", 2000, 200)
Bicicleta.buzinar(b2)
print()

print(b2)
