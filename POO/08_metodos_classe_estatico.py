class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod  # método de classe
    def criar_de_data_nascimento(cls, ano, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod  # método estático
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1996, "Carlos")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(p.idade))
print(Pessoa.e_maior_idade(15))
