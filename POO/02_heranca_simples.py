class Veiculo:
    def __init__(self, cor, placa, nro_rodas):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas
        
    def ligar_motor(self):
        print("Ligando motor...")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, nro_rodas, carregado):
        super().__init__(cor, placa, nro_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Estou carregado' if self.carregado else 'Não estou carregado'}")

vei01 = Motocicleta(cor="Preta",placa="ABC2453",nro_rodas=2)
print(vei01)
vei01.ligar_motor()
print()

vei02 = Carro(cor="Vermelho",placa="EZA58D6",nro_rodas=4)
print(vei02)
vei02.ligar_motor()
print()

vei03 = Caminhao(cor="Branco",placa="PRJ8752",nro_rodas=8, carregado= True)
print(vei03)
vei03.ligar_motor()
vei03.esta_carregado()
print()