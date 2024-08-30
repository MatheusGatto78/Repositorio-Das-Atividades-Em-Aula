#CRIAR CLASSE
class professor:
    #CONSTRUTOR, fala quais parametros eu preciso para instanciar uma classe
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma

    #MÉTODOS
    #self quer dizer para usar a variavél intertna
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getTurma(self):
        return self.turma



#FORA DA CLASSE FAZ PARTE DO MAIN
print("Olá mundo")

#CRIAR O OBJETO / INSTANCIA
prof = professor('Caaarlos', 'DEV')

#ADICIONANDO OUTRO PROFESSOR
prof2 = professor('Thiago', 'LOG')

print(prof.getNome())
print("Alteração do nome")

#MODIFICANDO UM VALOR
prof.setNome("Carlos")
print(prof.getNome())

#PRINTANDO A TURMA
print(prof.getTurma())
print("Fim")