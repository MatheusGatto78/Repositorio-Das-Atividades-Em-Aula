from classe import *

dog1 = cachorro("Marcos", "PitBull")
cat1 = gato("Penelope", "Gato inglês")

print("")
print(f"{dog1.getnomeC()} Está ", end="")
dog1.pegar_frisbee()

print("")

cat2 = gato("Minnie", "Angorá")





dog_nome = input("Insira o nome do cachorro -> ")
dog_raca = input("Insira a raça do cachorro -> ")
dog2 = cachorro(dog_nome, dog_raca)





print("\n*CACHORROS*")
print(dog1.getnomeC())
print(dog2.getnomeC())

print("\n*GATOS*")
print(cat1.getnomeG())
print(cat2.getnomeG())