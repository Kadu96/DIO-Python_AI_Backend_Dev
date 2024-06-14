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