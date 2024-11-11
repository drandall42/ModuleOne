class myFruit():
    def __init__(self, name, shape, sweet, colour):
        self.name = name
        self.shape = shape
        self.sweet = sweet
        self.colour = colour

def printFruit(fruit):
    print(f"Your fruit is {'sweet' if fruit.sweet == 'True' else 'not sweet'}")
    print(f"Your fruit is {fruit.shape}")
    print(f"Your fruit is {fruit.colour}")
    print(f"You chose ------> {fruit.name}")

    