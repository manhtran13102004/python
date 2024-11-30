class Animal:
    def __init__(self, species):
        self.species = species
    
class Dog(Animal):
    def __init__(self, species, dog_species):
        super().__init__(species)
        self.dog_species = dog_species
        
    def __str__(self):
        return f"The {self.species} species is {self.dog_species}"
    
d1 = Dog("dog", "chihuahua")
print(d1)    