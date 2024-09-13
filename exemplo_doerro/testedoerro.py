import os

#O try except trata o erro e da uma devolutiva. Nesse caso, se escrever uma letra, ao invés dele mostrar
#o erro, ele mostra "valor inválido".
while True:
    while True:
        try:
            escolha = int(input("1 ou 2\n-> "))
            break 

        except Exception as e:
            print(f"Valor inválido, o erro foi --< {e} >--")
            os.system("pause")
            os.system("cls")
    
    #Pegar a variavel escolha com o match, o case fala os numeros que "escolha" espera receber,
    #nesse caso 1 ou 2. o "_" serve para ser um valor default, se o valor de "escolha" for diferente
    #de 1 ou 2 ele entra no default(_) 
    match escolha:
        case 1:
            print("Função 1")
            os.system("pause")
            os.system("cls")
            break
        case 2:
            print("Função 2")
            os.system("pause")
            os.system("cls")
            break
        case _:
            print("Opção inválida")
            os.system("pause")
            os.system("cls")
