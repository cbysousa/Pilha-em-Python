# Implementação de Pilha em Python

Esse repositório contém uma implementação simples de uma estrutura de dados de pilha (LIFO - Last In, First Out) em Python.

### Arquivos

* **`node.py`**: Define a classe `Node`, que representa um nó individual na pilha. Cada nó armazena um valor (`data`) e uma referência para o próximo nó na pilha (`next`).

* **`pilha.py`**: Define a classe `Pilha`, que implementa a própria pilha.  Utiliza a classe `Node` para armazenar os elementos.

### Classe `Node` (`node.py`)

A classe `Node` é uma estrutura básica para armazenar dados em uma estrutura encadeada.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

- data: Armazena o valor do nó.
- next: Referência para o próximo nó na sequência (ou None se for o último nó).

### Classe Pilha (pilha.py)
A classe Pilha fornece as seguintes operações:

- push(elemento): Insere um elemento no topo da pilha.
- pop(): Remove e retorna o elemento do topo da pilha. Lança um IndexError se a pilha estiver vazia.
- peek(): Retorna o elemento do topo da pilha sem removê-lo. Lança um IndexError se a pilha estiver vazia.
- __len__(): Retorna o número de elementos na pilha.
- __repr__(): Retorna uma representação de string da pilha, mostrando os elementos do topo para a base.

### Exemplo de uso
```python
from pilha import Pilha

pilha = Pilha()
pilha.push(10)
pilha.push(20)
pilha.push(30)

print(len(pilha))  # Saída: 3
print(pilha.peek()) # Saída: 30
print(pilha.pop())  # Saída: 30
print(pilha)       # Saída: 20\n10\n
```
Exemplo de execução
```python
3
30
30
20
10
```
