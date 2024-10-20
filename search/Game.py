import random

from .Utils import Utils
from .BFS import BFS
from .Node import Node

class Game:
  def __init__(self, size):
    self.size = size
    self.state = self.generateRandomState()
    self.goal = Utils.getGoal(size)
    
  @staticmethod
  def welcome():
    print('Bem-vindo ao jogo')
    print('Digite o número da opção esperada:')
    print('0 - Sair')
    print('1 - Jogar')
    print('2 - Ver IA jogando')

  @staticmethod
  def IA():
    print('Aperte 0 para sair')
    print('Aperte 1 para iniciar')
    print('Aperte 2 para criar um novo estado inicial')
    

  def play(self):
    print('Digite o número da opção correspondente:')
    print('0 - Sair')

    allowed = Utils.allowedActions(self.size, self.state)
    if(allowed[0]):
      print('1 - Mover o X para a Direita')
    if(allowed[1]):
      print('2 - Mover o X para a Cima')
    if(allowed[2]):
      print('3 - Mover o X para a Baixo')
    if(allowed[3]):
      print('4 - Mover o X para a Esquerda')
    print('5 - Reiniciar o jogo')

  def restartState(self):
    self.state = self.generateRandomState()

  def generateRandomState(self):
    ordered = [x + 1 if x + 1 != self.size ** 2 else None for x in range(self.size**2)]

    quantityOfMoves = random.randint(10000, 10000 * random.randint(3,6))

    state = Utils.segregate(self.size, ordered)
    
    for i in range(quantityOfMoves):
      Utils.printState(state)
      state = Utils.action(self.size, random.randint(1,4), state)

    return state
  
  def changeState(self, state):
    self.state = state

  def run(self):
    opt = 1
    started = 0

    while int(opt) != 0:
      Utils.cls() 
      if started == 0:
        self.welcome()
        opt = int(input())

        if(opt == 1):
          started = 1
        if (opt == 2):
          started = 2

      elif started == 1:
        Utils.printState(self.state)
        if self.state != self.goal:
          self.play()
          opt = int(input())
          if opt >= 1 and opt <= 4:
            if(Utils.allowedActions(self.size, self.state)[opt - 1]):
              self.state = Utils.action(self.size, opt, self.state)
          if opt == 5:
            self.restartState()

          Utils.printState(self.state)
        else:
          print('Parabéns, você venceu')
          print('Digite 0 para sair ou 5 para reiniciar')
          opt = int(input())

          if opt == 5:
            self.restartState()
      
      elif started == 2:
        self.IA()
        Utils.printState(self.state)
        opt = int(input())

        if opt == 2:
          self.restartState()
        if opt == 1:
          node = Node(self.size, self.state)
          bfs = BFS(node)

          bfs.findSolution()
          input()