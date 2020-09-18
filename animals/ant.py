from interfaces import IDigging, IWalking

class Ant(IDigging, IWalking):
  def __init__(self, name):
    IDigging.__init__(self)
    IWalking.__init__(self)
    self.name = name

  def walk(self):
    print(f'{self} walk walk walks')

  def dig(self):
    print(f'{self} dig dig digs')

  def __str__(self):
    return f'{self.name} the ant'