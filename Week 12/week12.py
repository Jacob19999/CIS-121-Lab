
class RationalNumber:
    def __init__(self, _numerator , _denominator):
        self.a = _numerator
        self.b = _denominator
    
    'operator overloading +'
    def __add__(self, other_fraction : 'RationalNumber'):
        new_numberator = 0
        new_denominator = 0
        if self.b == other_fraction.b:
            new_numberator = self.a + other_fraction.a
        else:
            new_denominator = self.b * other_fraction.b
            new_numberator = (self.a * other_fraction.b) + (other_fraction.a * self.b)

        fraction3 = RationalNumber(new_numberator, new_denominator)

        return fraction3
    
    def __str__(self):
        return f"{self.a} / {self.b}"


fraction1 = RationalNumber(1 , 3)
fraction2 = RationalNumber(1 , 2)
fraction3 = fraction1 + fraction2
print(fraction3)
