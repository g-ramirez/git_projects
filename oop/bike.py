class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print "Price: {}".format(self.price)
        print "Maximum Speed: {}".format(self.max_speed)
        print "Total Miles: {}miles".format(self.miles)

    def ride(self):
        print "Riding..."
        self.miles +=10

    def reverse(self):
        print "Reversing..."
        self.miles -=5

bike1 = Bike(200, "25mph")
bike2 = Bike(100, "10mph")
bike3 = Bike(50, "500mph")

#Have the first instance ride three times, reverse once and have it displayInfo().
print "bike 1 doing its thing..."
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()
print "done"
print

#Have the second instance ride twice, reverse twice and have it displayInfo()
print "bike 2 doing its thing..."
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
print "done"
print

#Have the third instance reverse three times and displayInfo().
print "bike 3 doing its thing"
bike3.ride()
bike3.ride()
bike3.ride()
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
print "done"
print
