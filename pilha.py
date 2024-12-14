from node import Node

#inserir na pilha
#remover da pilha
#observar o topo da pilha
 
class Pilha:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elemento):
        node = Node(elemento)
        self.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        #remove o elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        raise IndexError('A pilha está vazia!')

    def peek(self):
        #retorna o topo da pilha sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError('A pilha está vazia!')
    
    def __len__(self):
        #retorna o número de elementos na pilha
        return len(self._size)
    
    def __repr__(self):
        r = ""
        point = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()
