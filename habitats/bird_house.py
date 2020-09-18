from .habitat import Habitat
from interfaces import IFlying

class Bird_House(Habitat):
  def __init__(self, name):
    super().__init__(name)

  def add_animal(self, animal):
    if isinstance(animal, IFlying) :
      self.animals.add(animal)
    else:
      print(f'{animal} is not allowed here')