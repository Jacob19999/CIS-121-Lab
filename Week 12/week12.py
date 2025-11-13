class RGBColor:
    # For each parameter (0 - 255)
    def __init__(self, r,g,b):
        self.r = r
        self.g = g
        self.b = b
    
    def __add__(self, color2):
        color3 = RGBColor(0, 0, 0)
        color3.r = (self.r + color2.r ) / 2
        color3.g = (self.g + color2.g ) / 2
        color3.b = (self.b + color2.b ) / 2
        return color3

    def __str__(self):
        return f"RGB Values: ({self.r}, {self.g}, {self.b})"

c1 = RGBColor(170, 150, 200)
c2 = RGBColor(30, 100, 60)
c3 = c1 + c2
print("Color 1 = " , c1)
print("Color 2 = " , c2)
print("Color 3 = " , c3)










