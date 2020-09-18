from .habitat import Habitat
from interfaces import ISwimming

class Aquarium(Habitat):
  def __init__(self, name):
    super().__init__(name)

  def add_animal(self, animal):
    if isinstance(animal, ISwimming):
      self.animals.add(animal)
    else:
      print(f'{animal} is not allowed here')