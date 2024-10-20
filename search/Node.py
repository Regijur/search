from .Utils import Utils

class Node:
  def __init__(self, size: int, state: list[list[int | None]], label: int | None = None, origin = None):
    self.state = state
    self.origin = origin
    self.label = label
    self.size = size
  
  def generateChildren(self):
    allowed = Utils.allowedActions(self.size, self.state)
    children: list[Node] = []
    

    for i in range(4):
      if allowed[i]:
        state = Utils.action(self.size, i + 1, self.state)
        node = Node(self.size, state, i + 1, self)
        children.append(node)

    return children