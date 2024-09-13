from osdefs import *
import os

sair = None
animais = []

while sair != 0:
    escolha = menu()
    os.system("cls")

    animais[0] = Cachorro()

    if escolha == 1:

        animais.append(cadastro())

    elif escolha == 2:

        listar(animais)

    elif escolha == 3:

        consulta(animais)

    elif escolha == 0:
        print("")
        os.system("pause")
        sair = 0
    else:
        print("OPÇÃO INVALIDA")
        print("")
        os.system("pause")
        os.system("cls")