from interfaces import ISwimming

class Fish(ISwimming):
  def __init__(self, name):
    super().__init__()
    self.name = name

  def swim(self):
    print(f'{self} blurbbles')

  def __str__(self):
    return f'{self.name} the fish'