from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractmethod #@abstractproperty :: Deprecated, use 'property' with 'abstractmethod' instead
    def marca(self):
        pass
    
class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada")
        
    def desligar(self):
        print("Desligando a TV...")
        print("Desligada")
        
    @property
    def marca(self):
        return "LG"
        
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado")
        
    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado")        
        
    @property
    def marca(self):
        return "Philco"

controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)