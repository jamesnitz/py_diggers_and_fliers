from animals import Parakeet, Earth_Worm, Terrapin, Snake, Mouse, Ant, Finch, Fish, Copperhead, Gerbil
from habitats import Aquarium, Bird_House, Dirt_Pile, Yard

parakeet = Parakeet('parry')
worm = Earth_Worm('wormy')
turtle = Terrapin('terry')
snake = Snake('snake')
mouse = Mouse('mickey')
ant = Ant('Anty')
finch = Finch('finchy')
betta = Fish('fishy')
Copperhead = Copperhead('coppy')
gerbil = Gerbil("gerry")

aquarium = Aquarium("aquarium")
bird_house = Bird_House("birdville")
dirty = Dirt_Pile('dirty')
yard = Yard('yard')

aquarium.add_animal(betta)

print(aquarium)