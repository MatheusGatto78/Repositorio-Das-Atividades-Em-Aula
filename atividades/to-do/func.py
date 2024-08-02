import os
import time

def limpa_console():
    os.system("pause")
    os.system("cls")

def menu():
    print("")
    print("~ MENU PRINCIPAL <TO-DO> ~")
    print("")
    print("O que deseja fazer?")
    print("1. Ver tarefas")
    print("2. Adicionar tarefas")
    print("3. Editar tarefas")
    print("4. Excluir tarefa")
    print("5. sair")
    print("")
    
def lista_tarefas():
    print("")
    print("~ LISTA DE TAREFAS ~")
    print("")

def add_tarefas():
    print("")
    print("~ ADICIONAR TAREFAS ~")
    print("")
    print("1. Adicionar tarefas a lista")
    print("2. Voltar ao menu")
    print("")

def edit_tarefas():
    print("")
    print("~ ADICIONAR TAREFAS ~")
    print("")
    print("1. Editar tarefa")
    print("2. Voltar ao menu")
    print("")

def exc_tarefa():
    print("")
    print("~ EXCLUIR TAREFA ~")
    print("")
    print("1. Excluir tarefa")
    print("2. Voltar ao menu")
    print("")