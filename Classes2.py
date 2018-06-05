class Fraction:

    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom

    def __str__(self): #without this, it will not print fraction
        return str(self.num)+"/"+str(self.den)
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den
        return Fraction(newnum,newden)
    
    def __mul__(self,otherfraction):
        newnum = self.num*otherfraction.num
        newden = self.den*otherfraction.den
        return Fraction(newnum,newden)
    
    def __truediv__(self,otherfraction):
        newnum = self.num*otherfraction.den
        newden = self.den*otherfraction.num
        return Fraction(newnum,newden)

    def __sub__(self,otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den*otherfraction.den
        return Fraction(newnum,newden)
    

myf = Fraction(3,5)
print(myf)
print(type(myf))
myf.__str__()

f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1+f2
f4 = f1*f2
f5 = f1/f2
f6 = f1-f2

print(f3)
print(type(f4))
print(f4)
print(f5)
print(f6)

#Self-check:
# we want to implement the div, mul, etc. as user friendly as possible.
# thats why we just wanted to do f1-f2 etc
#everything in python is an object. All these operators are
#are just methods. because everything in python is an object is that
# what implements these methods are objects. we want to use the + instead of a .
# for example:
(2).__add__(2)
# is the same as
2+2


# recall that self is referring to the current fraction,
# while the other parameter is referring to the other fraction
