from interfaces import IWalking

class Copperhead(IWalking):
  def __init__(self, name):
    super().__init__()
    self.name = name

  def walk(self):
    print(f'{self} slithers dangerously')

  def __str__(self):
    return f'{self.name} the copperhead'