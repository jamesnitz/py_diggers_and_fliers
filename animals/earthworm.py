from interfaces import IDigging

class Earth_Worm(IDigging):
  def __init__(self, name):
    super().__init__()
    self.name = name

  def dig(self):
    print(f'{self} eats dirt')

  def __str__(self):
    return f'{self.name} the worm'