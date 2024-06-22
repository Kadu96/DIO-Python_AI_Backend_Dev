class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
        
    def __iter__(self):     #obrigatorio
        return self
    
    def __next__(self):     #obrigatorio
        try:
            numeros = self.numeros[self.contador]
            self.contador += 1
            return numeros * 2
        except IndexError:
            raise StopIteration     #obrigatorio :: para finalizar o fluxo de iteração
        
for i in MeuIterador(numeros=[1,2,3,4,5]):
    print(i)