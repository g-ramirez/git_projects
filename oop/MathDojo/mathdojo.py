class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *params):
        for item in params:
            if type(item) == int:
                self.result += item
            else:
                self.result += sum(item)
        return self

    def subtract(self, *params):
        for item in params:
            if type(item) == int:
                self.result -= item
            else:
                self.result -= sum(item)
        return self
