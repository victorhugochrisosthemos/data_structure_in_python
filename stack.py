''' 
Stack = pilha
A Pìlha é uma estrutura de dados abstrata
Possui o princípio LIFO (Last In, First Out), ou seja, o último elemento adicionado é o primeiro a ser removido
Suas aplicações:
  Ao navegar em páginas web, a opção voltar a página anterior usa esse conceito
  Desfazer ações em geral como editores de texto
  Algoritmos de recursão usado em compiladores usa pilha de chamadas para manter controle de funções
  Usado para avaliar expressões matemáticas em notação infixa e pós-fixa
'''
class Stack:
  #O construtor da classe, é chamado automaticamente quando uma instância da classe é criada
  def __init__(self):
    self.itens = []
    
  def push(self, item):
    #Adiciona no topo da pilha
    self.itens.append(item)
    
  def pop(self):
    #Remove e retorna o topo da pilha, se estiver vazia vai avisar
    if self.is_empty():
      raise IndexError("Empty!")
    return self.itens.pop()
    
  def peek(self):
    #Mostra o topo da pilha, se estiver vazio vai avisar
    if self.is_empty():
      raise IndexError("Empty!")
    return self.itens[-1]
    
  def is_empty(self):
    #Mostra True se vazia e False se tiver elementos
    return len(self.itens) == 0
    
  def size(self):
    #Mostra a quantidade de itens na pilha
    return len(self.itens)
    



minha_pilha = Stack()

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


