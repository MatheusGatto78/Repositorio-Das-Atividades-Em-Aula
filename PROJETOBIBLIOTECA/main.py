#Importando as funções e claasses para o main
from funcoes import *
from classes import *
import os

livros = []

#Fantasia
livros.append(Livros('O Reino Encantado', 'Luana Almeida', 'Fantasia'))
livros.append(Livros('As Sombras do Dragão', 'Thiago Costa', 'Fantasia'))


#Aventura
livros.append(Livros('O Enigma do Templo', 'Carlos Pereira', 'Aventura'))
livros.append(Livros('A Jornada dos Heróis', 'Joana Ribeiro', 'Aventura'))
livros.append(Livros('Nos Confins do Mundo', 'Pedro Lopes', 'Aventura'))


#Suspense
livros.append(Livros('O Labirinto da Justiça', 'Ana Souza', 'Suspense'))
livros.append(Livros('O Segredo Mortal', 'Fábio Ribeiro', 'Suspense'))
livros.append(Livros('O Silêncio da Noite', 'Carla Mendes', 'Suspense'))


#Policial
livros.append(Livros('O Mistério do Colar', 'Juliana Costa','Ação'))
livros.append(Livros('A Testemunha Silenciosa', 'Marcelo Mendes','Ação'))
livros.append(Livros('O Detetive Invisível', 'Gabriel Lima','Ação'))


#Romance
livros.append(Livros('As Chamas do Passado', 'Ricardo Martins','Romance'))
livros.append(Livros('O Beijo da Meia-noite', 'Carolina Santos','Romance'))


#Drama
livros.append(Livros('O Fim do Silêncio', 'Paulo Lima','Drama'))
livros.append(Livros('As Lágrimas do Tempo', 'Mariana Souza','Drama'))
livros.append(Livros('O Coração Partido', 'Bruno Oliveira','Drama'))


#Ficção Científica
livros.append(Livros('As Estrelas do Amanhã', 'Bianca Oliveira','Ficção Científica'))
livros.append(Livros('O Futuro em Chamas', 'Lucas Pereira','Ficção Científica'))


#terror
livros.append(Livros('500 Dias com Ela', 'Bianca Oliveira','Terror'))
livros.append(Livros('Brutos - A ira ', 'Daniel Monteiro','Terror'))



loop = None
while loop != 0:
    escolha = menu()
    os.system('cls')

    #EMPRESTIMO   
    if escolha == 1:
        emprestimoo(livros)

    #CADASTRO
    elif escolha == 2:
        livros.append(cadastrar())

    #GERENCIAR (alterar ou excluir)
    elif escolha == 3:
        listar(livros)
    
    elif escolha == 4:
        pass

    #SAIR
    elif escolha == 5:
        print('saindo..')
        os.system('pause')
        os.system('cls')
        loop = 0
    
    #OPÇÃO INVÁLIDA
    else:
        print("OPÇÃO INVALIDA")
        print("")
        os.system("pause")
        os.system("cls")
