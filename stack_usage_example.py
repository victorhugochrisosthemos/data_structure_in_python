#Nesse caso, se o arquitvo que contém a classe for diferente do arquivo em que ela será usada, e estão os dois arquivos na mesma pasta
#Importa a classe Pilha do arquivo pilha.py
from pilha import Pilha

minha_pilha = Pilha()

print("Pilha vazia? ", minha_pilha.is_empty())  

minha_pilha.push(22)
minha_pilha.push(33)
minha_pilha.push(55)
minha_pilha.push(66)
minha_pilha.push("Hello World")

print("Quantos elementos tem na Pilha? ", minha_pilha.size()) 
print("Elemento do topo da Pilha? ", minha_pilha.peek())
print("Elemento removido da Pilha? ", minha_pilha.pop())
print("Quantos elementos tem na Pilha agora? ", minha_pilha.size()) 
print("Elemento do topo da Pilha agora? ", minha_pilha.peek())  
print("Elemento removido da Pilha? ", minha_pilha.pop()) 
print("Elemento removido da Pilha? ", minha_pilha.pop()) 
print("Pilha vazia?", minha_pilha.is_empty())

try:
    minha_pilha.peek()
except IndexError as e:
    print(e)  # Saída: "A pilha está vazia"

try:
    minha_pilha.pop()
except IndexError as e:
    print(e)  # Saída: "Empty"
