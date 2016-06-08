import animal, dog, dragon

animal1 = animal.Animal("animal", 100)
animal1.walk().walk().walk().run().run().displyHealth()
print "Animal done..."
print

dog1 = dog.Dog("doggie", 150)
dog1.walk().walk().walk().run().run().pet().displyHealth()
print "Doggie done..."
print

dragon1 = dragon.Dragon("Dragonie", 170)
dragon1.walk().walk().walk().run().run().fly().fly().displyHealth()
print "Dragonie done..."
print

try:
    print "Entering try block..."
    animal1.fly()
    print "Animal was able to fly (that's bad)"
    animal1.pet()
    print "Animal was able to be petted (that's bad)"
except:
    print "You should see this"    
