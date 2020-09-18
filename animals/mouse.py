from interfaces import IWalking

class Mouse(IWalking):
  def __init__(self, name):
    super().__init__()
    self.name = name

  def walk(self):
    print(f'{self} mouses about')

  def __str__(self):
    return f'{self.name} the mouse'