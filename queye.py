import random

time = 0
balance = 0

class Node:
    def __init__(self, val = None, nxt = None):
        self.val = val
        self.nxt = nxt

class Stack:
    def __init__(self):
        self.top = Node()

    def push(self, val):
        global time, balance
        n = Node(val, self.top.nxt)
        self.top.nxt = n
        time += 1
        balance -= 1
        assert balance >= 0 

    def pop(self):
        global time, balance
        if self.is_empty():
            return None
        n = self.top.nxt
        self.top.nxt = n.nxt
        assert balance >= 0
        return n.val

    def is_empty():
        return self.top.nxt == None

    def prt(self):
        cur = self.top
        while cur.nxt:
            print(cur.nxt.val, end=" ")
            cur = cur.nxt
        print()

stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
stk.prt()
print("pop", stk.pop())
print("pop", stk.pop())
stk.prt()

class Queue:
    def __init__(self):
        self.rear = Stack()
        self.front = Stack()

    def enqueue(self, val):
        global balance
        self.rear.push(val)
        balance += 4

    def move(self):
        if self.rear.is_empty():
            return
        x = self.rear.pop()
        self.front.push(x)

    def dequeue(self):
        if self.front.is_empty():
            while not self.rear.is_empty():
                self.move()
            return self.front.pop()

    def is_empty2(self):
        return 

    def prt2(self):
        print("rear:", end=" ")
        self.rear.prt()
        print("front:", end=" ")
        self.front.prt()

    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.prt()
q.enqueue(4)
q.enqueue(5)
print("deq", q.dequeue())
print("deq", q.dequeue())
print("deq", q.dequeue())
q.prt()

val = 0
for n in range (10, 30000, 100):
    time = 0
    q = Queue()
    for _c in range(n):
        op = 'ins' if q.is_empty() else 'ins' if random.random() < 0.5 else 'del'
        if op == 'ins':



# Análise Amortizada: Uma operação pode ter tempos de execução diferentes dependendo do contexto e estado da estrutura 
#  -> Considera custo médio por operação após número de operações executadas
#  -> Operações mais custosas podem ter um custo "amortizado" por outras menos custosas 

# Para que essa análise faça sentido, precisamos garantir cota superior para custo médio real no pior caso!!

# 3 métodos:
# -> Análise agregada
#    -> A ideia é estimar T(n) := custo agregado de n operações
#    -> Temos que garantir que T(n) >= Somatório dos custos reais das n operações
#    -> Com isso, podemos calcular o custo amortizado por operação := T(n)/n por operação
#    -> Temos uma média "globalzona" para todas as operações, possivelmente de tipos diferentes
#    -> No exemplo da fila com n operações de enfileirar e desenfileirar, temos que
#       -> Tpush = Tpop = 1 (na verdade, 0(1))
#       -> Tmove = Tpush + Tpop = 2
#       -> T(n) = Somatório (Tpush(R)) + Somatório (Tmove) + Somatório (Tpop(F))
#       -> Mas... Cada elemento movido <= 1 vez:
#           -> elementos <= n
#           -> moves <= n
#           -> Somatório (Tmoves) <= 2n = 0(n)
#           -> Somatório (Tpush(R)) = Somatório (Tpop(F)) = 0(n)
#           -> T(n) = 0(n) + 0(n) + 0(n) = 0(n)
#           -> CUSTO MÉDIO AMORTIZADO: 0(n)/n = 0(1)
#   -> Exemplo de um contador binário de k bits, com única operação de incrementar b (b++)
#       -> k = 5: 0 0 0 0 0
#       ->        0 0 0 0 1
#       ->        0 0 0 1 0
#       ->        0 0 0 1 1
#       ->        0 0 1 0 0
#       ->        0 0 1 0 1
#       ->        0 0 1 1 0
#       ->        0 0 1 1 1
#       ->        0 1 0 0 0
#       ->        0 1 0 0 1
#       ->        0 1 0 1 0
#       ->        .........
#   -> Tincr = 0(#flips) = 0(k) no pior caso (considere Tflip = 1)
#   -> Em n incrementos, o bit B[i] muda Piso(n/(2^i)) vezes
#   -> T(n) = Total de flips = Somatório (i = 0 até k-1) Piso(n/(2^i)) <= n Somatório (i=0 até infinito) 1/(2^n) = 2n
#   -> Ou seja... T(n) = 0(n). Custo amortizado 0(1) por incremento

# -> Método do banqueiro (accounting method)
# -> Método do potencial 

# -> Pilha: Lifo (padrão)
# -> Fila: Usando duas pilhas
#     - Uma representa Rear, outra Front
#     - Se a pilha Front estiver vazia, copia a pilha Rear para ela
#     - Se a pilha Front não estiver vazia, é só dar pop na pilha Front

# tempo enqueue = 0(1)
# tempo dequeue 
#     se a fila não estiver vazia = 0(1)
#     se a fila estiver vazia = 0(size(P) + 1) = linear

# para n operações: T(n) = n * 0(n) = 0(n^2) no pior caso (cota frouxa -> superestimação)


