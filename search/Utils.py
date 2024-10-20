import os

class Utils:
  @staticmethod
  def cls():
    os.system('cls' if os.name=='nt' else 'clear')  

  @staticmethod
  def printState(state: list[list[int | None]]):
    print()
    for line in state:
      view = '\t|'
      for el in line:
        view += f' {el} ' if el != None else ' x '
      view += '|'
      print(view)
    print()

  @staticmethod
  def action(size: int, opt: int, state: list[list[int | None]]):
    newState = [line.copy() for line in state]
    
    newEmptyPosition = None
    allowedAct = Utils.allowedActions(size, newState)
    emptyPosition = Utils.getEmptyPosition(state)

    if opt == 1 and allowedAct[0]:
        newEmptyPosition = (emptyPosition[0], emptyPosition[1] + 1)
    if opt == 2 and allowedAct[1]:
        newEmptyPosition = (emptyPosition[0] - 1, emptyPosition[1])
    if opt == 3 and allowedAct[2]:
        newEmptyPosition = (emptyPosition[0] + 1, emptyPosition[1])
    if opt == 4 and allowedAct[3]:
        newEmptyPosition = (emptyPosition[0], emptyPosition[1] - 1)


    if not newEmptyPosition:
      return state
    
    newState[newEmptyPosition[0]][newEmptyPosition[1]], newState[emptyPosition[0]][emptyPosition[1]] = newState[emptyPosition[0]][emptyPosition[1]], newState[newEmptyPosition[0]][newEmptyPosition[1]]

    return newState
  
  @staticmethod
  def allowedActions(size: int, state: list[list[int | None]]):
    emptyPosition = Utils.getEmptyPosition(state)

    allowed = [True, True, True, True]

    if(emptyPosition[0] == 0):
      allowed[1] = False
    elif emptyPosition[0] == size - 1:
      allowed[2] = False
    
    if(emptyPosition[1] == 0):
      allowed[3] = False
    elif emptyPosition[1] == size - 1:
      allowed[0] = False

    return tuple(allowed)

  @staticmethod
  def getEmptyPosition(state: list[list[int | None]]):
    for y in range(len(state)):
      for x in range(len(state[y])):
        if state[y][x] == None:
          return (y, x)
        
  @staticmethod
  def segregate(size: int, scrambledNumbers: list[int | None]):
    state : list[list[None | int]] = [[] for _ in range(size)]
    sel = -1
    
    for i in range(len(scrambledNumbers)):
      if i % size == 0:
        sel += 1

      state[sel].append(scrambledNumbers[i])
    
    return state

  @staticmethod
  def getGoal(size: int):
    goal = [x + 1 if x + 1 != size**2 else None for x in range(size**2)]
    return Utils.segregate(size, goal)
