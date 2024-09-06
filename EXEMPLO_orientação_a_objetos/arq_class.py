class pessoa:
    def __init__(self,nome):
        self.nome = nome
    
    def andar(self):
        print("Andando...")
    
    def falar(self):
        print("Falando")
    
    def setNome(self,novo_nome):
        self.nome = novo_nome
        print(self.nome)
    
    def getNome(self):
        return self.nome