from interfaces import IWalking

class Snake(IWalking):
  def __init__(self, name):
    super().__init__()
    self.name = name

  def walk(self):
    print(f'{self} slithers happily')

  def __str__(self):
    return f'{self.name} the snake'