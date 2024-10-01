class Complex():
    def __init__(self,real,img):
        self.real = real
        self.img = img
        # newImg =  (self.real + self.img)

    def __add__(self,other):
        newReal  = self.real + other.real
        newImg = self.img + other.img
        return Complex(newReal ,newImg)

    def __sub__(self,other):
        newReal  = self.real + other.real
        newImg = self.img - other.img
        return Complex(newReal ,newImg)

    def __str__(self):
        return f'{self.real} + {self.img}i'

num = Complex(4,6)
num2 = Complex(5,7)
res = num - num2
print(res)