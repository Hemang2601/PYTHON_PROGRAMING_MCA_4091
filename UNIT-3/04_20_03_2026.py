class demo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def call_methods(self):
        self.d1 = self.demo1()
        self.d1.getvalue(self.a, self.b)
        self.d1.calculate()

    class demo1:
        def getvalue(self, a, b):
            self.first = a
            self.second = b

        def calculate(self):
            print(f'{self.first} + {self.second} = {self.first + self.second}')


d = demo(int(input('Enter Value of A : ')), int(input('Enter Value of B : ')) )
d.call_methods()