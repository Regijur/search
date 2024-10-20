from .Node import Node
from .Utils import Utils
import math
import numpy as np

class NumPyBFS:
    def __init__(self, node: Node):
        self.states = np.array([node], dtype=Node)
        self.initialState = node.state
        self.closed = np.array([], dtype=Node)
        self.limit = math.factorial(node.size**2)
        self.goal = Utils.getGoal(node.size)
  
    def findSolution(self):
        node = None
        times = 0

        while self.states.size > 0 and not node and times < self.limit:
            times += 1
            print(times)

            selected: Node = self.states[0]

            if selected.state == self.goal:
                node = selected
            else:
                new_children = []

                for child in selected.generateChildren():
                    if not np.isin(child, self.closed) and not np.isin(child, self.states):
                        new_children.append(child)

                if new_children:
                    self.states = np.append(self.states, new_children)

                self.closed = np.append(self.closed, selected)

                self.states = np.delete(self.states, 0)

        Utils.cls()
        if node:
            print(f'Foram necessárias {times} análises de estados')
            print(f'Ainda restaram {len(self.states)} nós na fila')
            print(f'Foram fechados {len(self.closed)} nós')
            self.printSolution(node)
        else:
            print('Não foi possível encontrar uma solução')

    def printSolution(self, node: Node):
        Utils.printState(self.initialState)
        solution = []
        while node.origin:
            solution.append(node.label)
            node = node.origin
        print('Solution: ', end='')
        for i in range(len(solution) - 1, -1, -1):
            print(solution[i], end='\n' if i == 0 else ' -> ')
