print(set([1,2,3,1,3,4])) # {1,2,3,4}
print(set("abacaxi")) # {"b","a","c","x","i"}
print(set(("palio","gol","celta","palio"))) # {"gol", "celta", "palio"}
print()

linguagens = {"python",'java',"python"}
print(linguagens)
print(set(["python",'java',"python"]))
print()

numeros = {1,2,3,2}
print(numeros)
nro = list(numeros)
print(nro[0])
print()

carros = {"palio","gol","celta","palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
print()

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
conjunto_c = {4,1,2,5,6,3}
conjunto_d = {6,7,8,9}

print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_a.issubset(conjunto_c))
print(conjunto_c.issubset(conjunto_a))
print(conjunto_a.issuperset(conjunto_c))
print(conjunto_c.issuperset(conjunto_a))
print(conjunto_a.isdisjoint(conjunto_d))
print(conjunto_a.isdisjoint(conjunto_b))
conjunto_a.add(10)
print(conjunto_a)
conjunto_e = conjunto_a.copy()
print(conjunto_e)
conjunto_a.discard(10)
print(conjunto_a)
conjunto_a.remove(3)
print(conjunto_a)
conjunto_a.pop()
print(conjunto_a)
print(len(conjunto_c))
print(4 in conjunto_c)
print(40 in conjunto_c)
conjunto_a.clear()
print(conjunto_a)