from interfaces import IFlying

class Finch(IFlying):
  def __init__(self, name):
    super().__init__()
    self.name = name

  def fly(self):
    print(f'{self} flies around')

  def __str__(self):
    return f'{self.name} the finch'