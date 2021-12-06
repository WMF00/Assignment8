
class Bird(object):

    # instance attribute
    def __init__(self, name, species, movement):
        self.name = name
        self.species = species
        self.movement = movement

    def display(self):
        print("My name is {}".format(self.name))
        print("I am a {}".format(self.species))
        print("I move by {}".format(self.movement))


bird1 = input("Enter a name for the first bird: ")
print("Your first birds name is ", bird1)
bird2 = input("Enter a name for the second bird:  ")
print("Your second birds name is ", bird2)

bird1 = Bird(bird1, "bird", "flying")
bird2 = Bird(bird2, "bird", "flying")

bird1.display()
bird2.display()







