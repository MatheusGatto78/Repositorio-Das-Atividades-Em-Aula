from osdefs import *
import os

animais = []

while True:
    while True:
        try:
            escolha = menu()
            break

        except Exception as e:
            print(f"Valor inválido, o erro foi --< {e} >--")
            os.system("pause")
            os.system("cls")
            break

    match escolha:
        case 1:
            animais.append(cadastro())

        case 2:
            listar(animais)

        case 3:
            consulta(animais)

        case 0:
            print("")
            os.system("pause")
            break

        case _:
            print("OPÇÃO INVALIDA")
            print("")
            os.system("pause")
            os.system("cls")
