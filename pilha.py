from node import Node

class Pilha:
    #Implementa uma estrutura de dados de pilha (LIFO - Last in first out).
 
    def __init__(self):
        #Inicializa uma pilha vazia
        self.top = None
        self._size = 0

    def push(self, elemento):
        #Insere um elemento no topo da pilha
        node = Node(elemento)
        node.next = self.top #o novo nó deve apontar para o topo atual
        self.top = node
        self._size += 1

    def pop(self):
        '''
        Remove e retorna o elemento do topo da pilha

        Raises:
         IndexError: Se a pilha estiver vazia
        '''
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        raise IndexError('A pilha está vazia!')

    def peek(self):
         '''
        Retorna o elemento do topo da pilha sem removê-lo

        Raises:
         IndexError: Se a pilha estiver vazia
        '''
        if self._size > 0:
            return self.top.data
        raise IndexError('A pilha está vazia!')
    
    def __len__(self):
        #Retorna o número de elementos na pilha
        return self._size
    
    def __repr__(self):
        #Retorna uma representação em string da pilha
        r = ""
        pointer = self.top
        while pointer:
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r
