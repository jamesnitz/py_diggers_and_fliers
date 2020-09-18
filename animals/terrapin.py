from interfaces import IWalking

class Terrapin(IWalking):
  def __init__(self, name):
    super().__init__()
    self.name = name

  def walk(self):
    print(f'{self} walks slowly')

  def __str__(self):
    return f'{self.name} the turtle'