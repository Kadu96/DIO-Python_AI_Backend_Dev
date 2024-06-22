def meu_decorador(funcao):
    def envelope():
        print ("faz algo antes de executar")
        funcao()
        print ("faz algo depois de executar")
        
    return envelope

@meu_decorador  #açucar sintax
def ola_mundo():
    print("Ola mundo!")

#ola_mundo = meu_decorador(ola_mundo)    ## essa linha é substituida pela linha @meu_decorador
ola_mundo()