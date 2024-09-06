from asClasses import *

lista_gatos = []
id = 0

loop_menu = 0
while loop_menu == 0:
    print("---SISTEMA DE VETERINÁRIO---")
    print("")
    print("Qual animal deseja cadastrar? \n1 - Gato\n2 - Cachorro\n3 - Sair")
    escolha_menu = int(input("--> "))
    
    #GATO
    if escolha_menu == 1:
        while escolha_menu == 1:
            print("1 - cadastrar\n2 - voltar ao menu principal")
            escolha_gato = int(input("--> "))
            if escolha_gato == 1:
                id += 1
                cat_name = input("Nome -> ")
                cat_raca = input("Raça -> ")
                cat_dono = input("Dono -> ")
                cat_idade = input("Idade -> ")
                cat_procedimento = input("Procedimento -> ")

                novo_gato = Gato(cat_name, cat_raca, cat_dono, cat_idade, cat_procedimento)
                lista_gatos.append(novo_gato)
                print("")
                print("Lista de gatos:")
                print("")

                for osgatos in lista_gatos:
                    print(f"Nome: {osgatos.getNome()} | Raça: {osgatos.getRaca()}")

    #CACHORRO
    elif escolha_menu == 2:
        pass

    elif escolha_menu == 3:
        loop_menu = 1
        print("Saindo...")

    else:
        print("Opção invalida")