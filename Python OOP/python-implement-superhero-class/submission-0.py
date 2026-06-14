class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name 
        self.power = power 
        self.health = health



# TODO: Create Superhero instances

superhero_1 = SuperHero("Batman","Intelligence",100)
superhero_2= SuperHero("Superman","Strength",150)

print(superhero_1.name)
print(superhero_1.power)
print(superhero_1.health)
print(superhero_2.name)
print(superhero_2.power)
print(superhero_2.health)

# TODO: Print out the attributes of each superhero
