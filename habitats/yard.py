from .habitat import Habitat
from interfaces import IWalking

class Yard(Habitat):
  def __init__(self, name):
    super().__init__(name)

  def add_animal(self, animal):
    if isinstance(animal, IWalking) :
      self.animals.add(animal)
    else:
      print(f'{animal} is not allowed here')