from .Node  import Node
from .Utils import Utils
import math

class BFS:
  def __init__(self, node: Node):
    self.nodes = [node]
    self.initialState = node.state
    self.closed : list[list[int | None]] = []
    self.limit = math.factorial(node.size**2)
    self.goal = Utils.getGoal(node.size)
  
  def findSolution(self):
    node = None
    times = 0

    while len(self.nodes) > 0 and not node and times < self.limit:
      times += 1
      print(times)
      if self.nodes[0].state == self.goal:
        node = self.nodes[0]
      else:
        for child in self.nodes[0].generateChildren():
          if not child.state in self.closed and not True in [x.state == child.state for x in self.nodes]:
            self.nodes.append(child)
        
        self.closed.append(self.nodes[0].state)
        del self.nodes[0]
    
    Utils.cls()
    if node:
      print(f'Foram necessárias {times} análises de estados')
      print(f'Ainda restaram {len(self.nodes)} nós na fila')
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
  

