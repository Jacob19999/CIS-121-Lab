import math


# Inputs
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
h = float(input("Enter Height: "))

area = ((a + b) / 2) * h

print(f"The area is {area}")
































import math

a = float(input("Value of a: "))
b = float(input("Value of b: "))
h = float(input("Value of h: "))

result = ((a + b) / 2) * h

print(f"Area is {result}")









































'''
import math

a = float(input("Enter the value of a:"))
b = float(input("Enter the value of b: "))
h = float(input("Enter the value of h: "))

area = ((a + b) / 2) * h

print(f"The area is = {area}" )



# Question 1
a = int(input("Enter a: "))
b = int(input("Enter b: "))
h = int(input("Enter h: "))

area = ((a + b) / 2) * h
print(f"area is {area}")

# Question 2
r = int(input("Enter radius: "))
volume = (4 / 3) * math.pi * (r**3)
print(f"volume is {volume}")

# question 3....
radius = int(input("Enter the radius of the circle: "))
area = math.pi * math.pow(radius, 2)
print(f"Area = {area} m^2")




years = 5.2
remaining = years - int(years)

total_days_remaining = remaining * 365.25

months = int(total_days_remaining / 30)
    
days = round(total_days_remaining - (months * 30))

print(int(years), months, days)


'''