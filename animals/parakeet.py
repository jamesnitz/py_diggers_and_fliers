from interfaces import IFlying

class Parakeet(IFlying):
  def __init__(self, name):
    super().__init__()
    self.name = name

  def fly(self):
    print(f'{self} parakeets')

  def __str__(self):
    return f'{self.name} the parakeet'