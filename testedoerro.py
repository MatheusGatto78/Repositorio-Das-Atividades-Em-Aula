import os

#O try except trata o erro e da uma devolutiva. Nesse caso, se escrever uma letra, ao invés dele mostrar
#o erro, ele mostra "valor inválido".
while True:
    try:
        escolha = int(input("1 ou 2\n-> "))
        break 

    except Exception as e:
        print(f"Valor inválido, o erro foi --< {e} >--")
        os.system("pause")
        os.system("cls")
