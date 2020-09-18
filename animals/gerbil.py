from interfaces import IWalking

class Gerbil(IWalking):
  def __init__(self, name):
    super().__init__()
    self.name = name

  def walk(self):
    print(f'{self} scurries')

  def __str__(self):
    return f'{self.name} the gerbil'