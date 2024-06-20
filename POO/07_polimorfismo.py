class Passaro:
    def voar(self):
        print("Voando....")
        
class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")
        
def plano_de_voo(obj):
    obj.voar()
    
p1 = Pardal()        
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)