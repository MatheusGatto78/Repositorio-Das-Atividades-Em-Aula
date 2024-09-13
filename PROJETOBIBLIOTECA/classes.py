#CRIANDO A CLASSE DOS LIVROS
class Livros:
    #O INIT É O CONSTRUTOR, NÓS ESTAMOS CRIANDO OS ATRIBUTOS USANDO O SELF.
    def __init__ (self, nome_livro, nome_autor,genero):
        self.nome_livro = nome_livro
        self.nome_autor = nome_autor
        self.genero = genero
        self.emprestimo_leitor = "Livre"

    #CRIANDO OS MÉTODOS
    #O GET PARA "PEGAR" O NOME NESSE EXEMPLO
    def getNome(self):
        return self.nome_livro
    #O SET É PARA "SETAR" O NOME
    def setNome(self, nome_livro):
        self.nome = nome_livro

    def getNomeAutor(self):
        return self.nome_autor
    def setNomeAutor(self, nome_autor):
        self.nome_autor = nome_autor

    def getGenero(self):
        return self.genero
    def setGenero(self, genero):
        self.genero = genero

    def getEmprestado(self):
        return self.emprestimo_leitor
    def setEmprestado(self, emprestimo):
        self.emprestimo_leitor = emprestimo
        