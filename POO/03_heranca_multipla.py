class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return (
            f"{self.__class__.__name__}:{', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        )


class Mamimefero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico


class Gato(Mamimefero):
    pass


class Ornitorrinco(Mamimefero, Ave):
    def __init__(self, cor_pelo, **kw):
        super().__init__(cor_pelo, **kw)
        print(Ornitorrinco.mro())  # mostra a ordem da resolução dos métodos


gato = Gato(nro_patas=4, cor_pelo="preto")
print(gato)
print()

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="marrom", cor_bico="laranja")
print(ornitorrinco)
print()
