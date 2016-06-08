from animal import Animal

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        print "Petting..."
        self.health +=5
        return self
