import functools


def duplicar(func):
    @functools.wraps(func)
    # esse decorador faz com que 'print(aprender.__name__)'
    # retorne o nome da função em questão, nesse caso "aprender"
    # sem esse decorador 'print(aprender.__name__)' retornará "envelope"
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return envelope


@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()


tecnologia = aprender("Python")
print(tecnologia)
print(aprender.__name__)
