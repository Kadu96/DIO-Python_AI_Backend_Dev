# list :: listas :: []
linguagens = ["python", "java", "js", "c"]
print(linguagens)

linguagens.append("csharp")
print(linguagens)

linguagens.extend(["csharp", "java"])
print(linguagens)

print(linguagens.count("csharp"))

print(linguagens.index("python"))

linguagens.sort()
print(linguagens)

print(sorted(linguagens))

linguagens.clear()
print(linguagens)

# tupla :: lista imutável :: ()
frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil",)

frutas[0] #laranja
frutas[2] #uva

matriz = (
    (1,"a",2),
    ("b",3,4),
    (6,5,"c")
)

matriz[0]       # (1,"a",2)
matriz[0][0]    # 1
matriz[0][-1]   # 2
matriz[-1][-1]  # "c"