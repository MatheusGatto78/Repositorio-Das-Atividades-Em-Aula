class cachorro:
    def __init__(self,nome,raca):
        self.nome = nome
        self.raca = raca

    def deitar(self):
        print("Deitando...")

    def pegar_frisbee(self):
        print("Correndo para pegar o frisbee...")
    
    def latir(self):
        print("Au Au...")

    def setnomeC(self,novo_nome):
        self.nome = novo_nome
        print(self.nome)
    
    def getnomeC(self):
        return self.nome
    
    def getracaC(self):
        return self.raca

#######################################

class gato:
    def __init__(self,nome,raca):
        self.nome = nome
        self.raca = raca

    def espreguiçar(self):
        print("Se espreguiçando...")
    
    def escalar(self):
        print("Escalando...")

    def miar(self):
        print("Miau...")
    
    def setnomeG(self,novo_nome):
        self.nome = novo_nome
        print(self.nome)
    
    def getnomeG(self):
        return self.nome
    