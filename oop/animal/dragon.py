from animal import Animal

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name,health)
        self.health = 170

    def fly(self):
        print "Flying..."
        self.health -=10
        return self
