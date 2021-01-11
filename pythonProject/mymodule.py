class MyNumbers:
    global x
    x = 300
    def __init__(self):
        self.a = 0
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        self.a += 1
        if (self.a > 5):
            raise StopIteration
        else:
            return self.a
    def showX(self):
        print(x)