'''
- Filas são estruturas de dados
- Usam o princípio FIFO(first in, first out), o primeiro a entrar é o primeiro a sair
- Podem ser usadas em sistemas operacionais para ordenar a execução de programas, buffer de dados em redes de computadores, algoritmos de busca de grafos
'''


class Queue:

    #Inicializa a fila como uma lista vazia
    def __init__(self):
        self.items = []
      
    #Verifica se a fila está vazia
    def is_empty(self):
        return len(self.items) == 0
      
    #Adiciona um item ao final da fila
    def enqueue(self, item):
        self.items.append(item)

    #Remove e retorna o item no início da fila
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    #Retorna o item no início da fila sem removê-lo
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from an empty queue")

    #Retorna o número de itens na fila
    def size(self):
        return len(self.items)

    #Retorna uma representação em string da fila para facilitar a visualização
    def __str__(self):
        return str(self.items)



# Exemplo 
fila = Queue()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)

print(fila)        
print(fila.dequeue())  
print(fila)       
print(fila.peek())     
print(fila.size())    
