
class RationalNumber:
    def __init__(self, _numerator = 1 , _denominator = 1):
        self.numerator = _numerator
        self.denominator = _denominator
    
    def __add__(self, other_fraction):
        new_numerator = 0
        new_denominator = 0 
        ' if the denominator is the same !'
        if self.denominator == other_fraction.denominator:
            new_numerator = self.numerator + other_fraction.numerator
            new_denominator = self.denominator
        else:
            'if denominator is different , calculate new denominator'
            new_denominator = self.denominator * other_fraction.denominator
            '1/3 + 1/2'
            '2/6 + 3/6'
            '5/6'
            new_numerator = (self.numerator * other_fraction.denominator) +  (other_fraction.numerator * self.denominator)
        
        return RationalNumber(new_numerator, new_denominator)
    
    def __str__(self):
        return f"{self.numerator} / {self.denominator}"
    
fraction1 = RationalNumber(1, 3)
fraction2 = RationalNumber(1 , 2)
fraction3 = fraction1 + fraction2
print(fraction3)