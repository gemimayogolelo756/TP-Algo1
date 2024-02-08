class Fraction : 
    def __init__(self,num,den):
        assert den >  0
        self.num = num
        self.den = den
    def __str__(self):
        if self.den == 1:
            return str(self.num)
        else:
            return f"{self.num}/{self.den}"
    def __eq__(self,other):
        if (other,Fraction):  
            return self.num*other.den ==self.den*other.num
        return False
F1 = Fraction(3,4)
F2 = Fraction(-8,1)
F3 = Fraction(2,3)
F4 = Fraction(21,28)
print(F1)
print(F2)
print(F3)
print(F4)
print(F1.__eq__(F2))
print(F1.__eq__(F3))
print(F2.__eq__(F3))
print(F2.__eq__(F4))
print(F3.__eq__(F4))
print(F1.__eq__(F4))
### yogolelo lubumba gemima


        