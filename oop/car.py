class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 15
        else:
            self.tax = 12

    def display_all(self):
        print ("Price: ${}".format(self.price))
        print ("Speed: {}".format(self.speed))
        print ("Fuel: {}".format(self.fuel))
        print ("Mileage: {}mpg".format(self.mileage))
        print ("Tax: {}%".format(self.tax))

car1 = Car(500, "35mph", "Full", 100)
car2 = Car(12000, "135mph", "Full", 700)

car1.display_all()
print
car2.display_all()
