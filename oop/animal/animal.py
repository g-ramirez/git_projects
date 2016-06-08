class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        print "Walking..."
        self.health -=1
        return self

    def run(self):
        print "Running..."
        self.health -=5
        return self

    def displyHealth(self):
        print "Name: {}".format(self.name)
        print "Health: {}".format(self.health)
