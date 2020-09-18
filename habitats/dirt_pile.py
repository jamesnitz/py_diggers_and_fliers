from .habitat import Habitat
from interfaces import IDigging

class Dirt_Pile(Habitat):
  def __init__(self, name):
    super().__init__(name)

  def add_animal(self, animal):
    if isinstance(animal, IDigging) :
      self.animals.add(animal)
    else:
      print(f'{animal} is not allowed here')