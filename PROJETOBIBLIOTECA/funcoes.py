from classes import *
import os

#CRIANDO O MENU
def menu():
    #MENU
    print('<• Biblioteca - Group 1 •>')
    print('• [1] - Emprestimo de Livros')
    print('• [2] - Cadastrar Livros')
    print('• [3] - Listar Livros')
    print('• [4] - Alterar livro')
    print('• [5] - Sair')
    print('•----------------------------•')

    escolha = int(input('Qual opcao deseja ?!\n•> '))
    return escolha

#CADASTRAR UM LIVRO
def cadastrar():

    print("---• CADASTRAR LIVRO •---")
    print("[1] - Cadastrar Livro")
    print("[2] - Voltar ao menu")
    escolha = int(input('qual opcao deseja?!\n•> '))
    os.system('cls')








    #CADASTRAR
    if escolha == 1:
        print('---• Cadastrar Livro •---')
        nome_livro = input('Informe o Nome do Livro\n•> ')
        nome_autor = input('Informe o Nome do Autor\n•> ')
        os.system('cls')
        print("---- Informe o Genero do livro ----\n") 
        print('[1] - Fantasia')
        print('[2] - Aventura') 
        print('[3] - Suspense') 
        print('[4] - Ação') 
        print('[5] - Romance') 
        print('[6] - Drama') 
        print('[7] - Ficção Científica') 
        print('[8] - Terror')
        print('')
        genero = int(input('Informe o Genero do Livro\n•> '))
        os.system('cls')

        #CADASTRAR FANTASIA
        if genero == 1:
            genero = "Fantasia"
            livros = Livros(nome_livro, nome_autor, genero)
            os.system('cls')
            print('Livro Cadastrado com Sucesso')
            os.system('pause')
            os.system('cls')

            return livros
        
        #CADASTRAR AVENTURA
        if genero == 2:
            genero = "Aventura"
            livros = Livros(nome_livro, nome_autor, genero)
            os.system('cls')
            print('Livro Cadastrado com Sucesso')
            os.system('pause')
            os.system('cls')

            return livros

        #CADASTRAR SUSPENSE
        if genero == 3:
            genero = "Suspense"
            livros = Livros(nome_livro, nome_autor, genero)
            os.system('cls')
            print('Livro Cadastrado com Sucesso')
            os.system('pause')
            os.system('cls')

            return livros
    
        #CADASTRAR AÇÃO
        if genero == 4:
            genero = "Ação"
            livros = Livros(nome_livro, nome_autor, genero)
            os.system('cls')
            print('Livro Cadastrado com Sucesso')
            os.system('pause')
            os.system('cls')

            return livros

        #CADASTRAR ROMANCE
        if genero == 5:
            genero = "Romance"
            livros = Livros(nome_livro, nome_autor, genero)
            os.system('cls')
            print('Livro Cadastrado com Sucesso')
            os.system('pause')
            os.system('cls')

            return livros

        #CADASTRAR DRAMA
        if genero == 6:
            genero = "Drama"
            livros = Livros(nome_livro, nome_autor, genero)
            os.system('cls')
            print('Livro Cadastrado com Sucesso')
            os.system('pause')
            os.system('cls')

            return livros
        
        #CADASTRAR FICÇÃO CIENTIFICA
        if genero == 7:
            genero = "Ficção Científica"
            livros = Livros(nome_livro, nome_autor, genero)
            os.system('cls')
            print('Livro Cadastrado com Sucesso')
            os.system('pause')
            os.system('cls')

            return livros
    
        #CADASTRAR TERROR
        if genero == 8:
            genero = "Terror"
            livros = Livros(nome_livro, nome_autor, genero)
            os.system('cls')
            print('Livro Cadastrado com Sucesso')
            os.system('pause')
            os.system('cls')

            return livros
        
        


#Gerenciar Livros
def gerenciar():
    print("---• GERENCIA DE LIVROS •---")
    print("[1] - Alterar Livro")
    print("[2] - Excluir Livro")
    print("[3] - Voltar ao menu")





#LISTAR OS TODOS OS LIVROS OU SÓ UM GENERO ESPECIFICO
def listar(lista):
    print("---• LISTAR LIVROS •---")
    print("[1] - Listar todos os livros")
    print("[2] - Listar gênero de livro")
    print('[3] - voltar')
    choose = int(input("--> "))
    os.system("cls")

    #LISTAR TODOS OS LIVROS
    import os

    if choose == 1:
        print("---- LISTA DE TODOS OS LIVROS ----\n")
        # Imprime o cabeçalho da tabela
        print(f"{'ID':<5} {'NOME DO LIVRO':<30} {'AUTOR':<25} {'GÊNERO':<15} {'EMPRÉSTIMO':<10}")

        # Usando o for para percorrer o dicionário com as instâncias
        cont = 1
        for livr in lista:
            # Imprime cada linha da tabela formatada
            print(f"{cont:<5} {livr.getNome():<30} {livr.getNomeAutor():<25} {livr.getGenero():<15} {livr.getEmprestado():<10}")
            cont += 1

        print("")
        os.system("pause")
        os.system("cls")


    #LISTAR UM GENERO ESPECIFICO
    elif choose == 2:
            while True:
                print("---- Listar gênero específico ----\n") 
                print('[1] - Fantasia')
                print('[2] - Aventura') 
                print('[3] - Suspense') 
                print('[4] - Ação') 
                print('[5] - Romance') 
                print('[6] - Drama') 
                print('[7] - Ficção Científica') 
                print('[8] - Terror')
                print('')

                #ESCOLHER QUAL GENERO QUER LISTAR
                local = int(input('qual opcao deseja?\n•> '))
                os.system('cls')
                
                #LISTAR FANTASIA
                if local == 1:
                    print('-- Livros de Fantasia --')
                    print("ID\tNOME DO LIVRO\t\t\tAUTOR\t\t\t\tGÊNERO\t\t\tEmprestimo")
                    print('')
                    cont = 1
                    for i in lista:
                        if i.getGenero() == "Fantasia":
                            print(f"{cont}\t{i.getNome()}\t\t{i.getNomeAutor()}\t\t\t{i.getGenero()}\t\t\t{i.getEmprestado()}")
                            cont += 1
                    os.system('pause')
                    os.system('cls')

                #LISTAR AVENTURAS
                elif local == 2:
                    print('-- Livros de Aventura --')
                    print("ID\tNOME DO LIVRO\t\t\tAUTOR\t\t\t\tGÊNERO\t\t\tEmprestimo")
                    print('')
                    cont = 1
                    for i in lista:
                        if i.getGenero() == "Aventura":
                            print(f"{cont}\t{i.getNome()}\t\t{i.getNomeAutor()}\t\t\t{i.getGenero()}\t\t\t{i.getEmprestado()}")
                            cont += 1
                    os.system('pause')
                    os.system('cls')
                
                #LISTAR SUSPENSE
                elif local == 3:
                    print('-- Livros de Suspense --')
                    print("ID\tNOME DO LIVRO\t\t\tAUTOR\t\t\t\tGÊNERO\t\t\tEmprestimo")
                    print('')
                    cont = 1
                    for i in lista:
                        if i.getGenero() == "Suspense":
                            print(f"{cont}\t{i.getNome()}\t\t{i.getNomeAutor()}\t\t\t{i.getGenero()}\t\t\t{i.getEmprestado()}")
                            cont += 1
                    os.system('pause')
                    os.system('cls')
                
                #LISTAR AÇÃO
                elif local == 4:
                    print('-- Livros de Ação --')
                    print("ID\tNOME DO LIVRO\t\t\tAUTOR\t\t\t\tGÊNERO\t\t\tEmprestimo")
                    print('')
                    cont = 1
                    for i in lista:
                        if i.getGenero() == "Ação":
                            print(f"{cont}\t{i.getNome()}\t\t{i.getNomeAutor()}\t\t\t{i.getGenero()}\t\t\t{i.getEmprestado()}")
                            cont += 1
                    os.system('pause')
                    os.system('cls')
                
                #LISTAR ROMANCE    
                elif local == 5:
                    print('-- Livros de Romance --')
                    print("ID\tNOME DO LIVRO\t\t\tAUTOR\t\t\t\tGÊNERO\t\t\tEmprestimo")
                    print('')
                    cont = 1
                    for i in lista:
                        if i.getGenero() == "Romance":
                            print(f"{cont}\t{i.getNome()}\t\t{i.getNomeAutor()}\t\t\t{i.getGenero()}\t\t\t{i.getEmprestado()}")
                            cont += 1
                    os.system('pause')
                    os.system('cls')

                #LISTAR DRAMA   
                elif local == 6:
                    print('-- Livros de Drama --')
                    print("ID\tNOME DO LIVRO\t\t\tAUTOR\t\t\t\tGÊNERO\t\t\tEmprestimo")
                    print('')
                    cont = 1
                    for i in lista:
                        if i.getGenero() == "Drama":
                            print(f"{cont}\t{i.getNome()}\t\t{i.getNomeAutor()}\t\t\t{i.getGenero()}\t\t\t{i.getEmprestado()}")
                            cont += 1
                    os.system('pause')
                    os.system('cls')

                #LISTAR FICÇÃO CIENTIFICA
                elif local == 7:
                    print('-- Livros de Ficção Científica --')
                    print("ID\tNOME DO LIVRO\t\t\tAUTOR\t\t\t\tGÊNERO\t\t\tEmprestimo")
                    print('')
                    cont = 1
                    for i in lista:
                        if i.getGenero() == "Ficção Científica":
                            print(f"{cont}\t{i.getNome()}\t\t{i.getNomeAutor()}\t\t\t{i.getGenero()}\t\t\t{i.getEmprestado()}")
                            cont += 1
                    os.system('pause')
                    os.system('cls')

                #LIVROS DE TERROR
                elif local == 8:
                    print('-- Livros de Terror --')
                    print("ID\tNOME DO LIVRO\t\t\tAUTOR\t\t\t\tGÊNERO\t\t\tEmprestimo")
                    print('')
                    cont = 1
                    for i in lista:
                        if i.getGenero() == "Terror":
                            print(f"{cont}\t{i.getNome()}\t\t{i.getNomeAutor()}\t\t\t{i.getGenero()}\t\t\t{i.getEmprestado()}")
                            cont += 1
                    os.system('pause')
                    os.system('cls')
                
                else:
                    print('opcao invalida')

                return local     





#EMPRESTAR UM LIVRO
def emprestimoo(lista):
    y = 0
    while y == 0:
        print("---• EMPRÉSTIMO DE LIVRO •---")
        print("[1] - Ver livros disponíveis")
        print("[2] - Pegar emprestado")
        print('[3] - Voltar')
        choose_2 = int(input("-->"))
        os.system('cls')



        if choose_2 == 1:
                print("---- Lista dos livros ----\n")
                print("ID\t\tNOME DO LIVRO\t\tAUTOR\t\tGENÊRO")

                cont = 1
                for livros in lista:
                    print(f"{cont}\t\t{livros.getNome()}\t\t{livros.getNomeAutor()}\t\t{livros.getGenero()}")
                    cont += 1

                print("")
                os.system("pause")
                os.system("cls")




        #EMPRESTAR UM LIVRO
        elif choose_2 == 2:
            print("EMPRÉSTIMO\n")
            print("Livros:\n")
            print("ID\tLIVRO\tAUTOR\tGÊNERO")
            cont = 1
            for i in lista:
                print(f"{cont}\t{i.getNome()}\t{i.getNomeAutor()}\t{i.getGenero()}") 
                cont += 1  
            print("")
            escolha = int(input("Insira o ID do livro que você deseja emprestar\n--> "))
            os.system("cls")

            print("- - Emprestimo")
            print('')
            print("- - DADOS DO LEITOR")
            nomecliente = input("\nNome: ")

            lista[escolha - 1].setEmprestado(nomecliente)
            

            print("")
            print("EMPRESTIMO REALIZADO COM SUCESSO!")
            print("\t*Esse empréstimo tem a duração de 1 mês!!")
            os.system('pause')
            os.system('cls')
        
        elif choose_2 == 3:
            break
        
        else:
            print('opcao invalida')
            os.system('pause')
            os.system('cls')

            