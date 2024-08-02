from func import *

numerador = 0
tarefas = {}

loop_menu = 1
while loop_menu == 1:
    menu()
    escolha_menu_principal = int(input("--> "))
    print("")

#LISTAR TAREFAS
    if escolha_menu_principal == 1:
        while escolha_menu_principal == 1:
            lista_tarefas()
            for chave, valor in tarefas.items():
                numerador+=1
                print(f"{numerador}º Tarefa: {chave} | Descrição da tarefa: {valor}")
            print("")
            print("1. Voltar ao menu")
            print("")
            escolha_lista = int(input("--> "))
            if escolha_menu_principal == 1:
                escolha_menu_principal = None

#ADICIONAR TAREFAS
    elif escolha_menu_principal == 2:
        while escolha_menu_principal == 2:
            add_tarefas()
            escolha_add_tarefas = int(input("--> "))
            if escolha_add_tarefas == 1:
                print("")
                nome_tarefa = input("Nome da tarefa -> ")
                descricao_tarefa = input("Descrição da tarefa -> ")
                tarefas[nome_tarefa] = descricao_tarefa
                print("")
                print("Tarefa adicionada :)")
            elif escolha_add_tarefas == 2:
                escolha_menu_principal = None

#EDITAR TAREFAS
    elif escolha_menu_principal == 3:
        edit_tarefas()
        escolha_edit_tarefa = int(input("--> "))
        if escolha_edit_tarefa == 1:
            
            pass

        elif escolha_edit_tarefa == 2:
            escolha_menu_principal = None



#EXCLUIR TAREFAS
    elif escolha_menu_principal == 4:
        while escolha_menu_principal == 4:
            exc_tarefa()
            escolha_exc_tarefa = int(input("--> "))
            if escolha_exc_tarefa == 1:
                print("")
                print("Qual tarefa deseja excluir")
                print("")
                excluir_tar = input("--> ")
                if excluir_tar in tarefas:
                    print("")
                    del tarefas[excluir_tar]
                    print("Tarefa excluida :)")
                    print("")
                    numerador = 0


            elif escolha_exc_tarefa == 2:
                escolha_menu_principal = None

#SAIR
    elif escolha_menu_principal == 5:
        print("")
        print("Saindo...")
        print("")

