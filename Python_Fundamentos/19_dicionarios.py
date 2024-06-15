pessoa = {"nome": "Carlos", "idade": 28}
pessoa = dict(nome="Carlos", idade= 28)
print(pessoa)
print()

pessoa["telefone"] = "33335500"
print(pessoa)
print()

for chave, valor in pessoa.items():
    print(chave, valor)
  
# forma menos convencional    
for chave in pessoa:
    print(chave, pessoa[chave])
print()


pessoa1 = pessoa.copy()
print(pessoa1)
pessoa2 = dict.fromkeys(["nome","telefone"])
print(pessoa2)
resultado = pessoa.get("chave")
print(resultado)
resultado = pessoa.get("chave", {})
print(resultado)
resultado1 = pessoa.get("idade", {})
print(resultado1)
print(pessoa.keys())
print(pessoa.values())
pessoa1.pop("telefone",{})
print(pessoa1)
pessoa1.popitem()
print(pessoa1)
pessoa1.setdefault("idade",19)
print(pessoa1)
pessoa1.update({"idade": 28 })
print(pessoa1)
resultado = "nome" in pessoa
print(resultado)
resultado = "telefone" in pessoa1
print(resultado)
del pessoa["telefone"]
print(pessoa)
pessoa.clear()
print(pessoa)