'''
# Random example students came up with!
class Costumes:
    # This is the first thing that runs.
    def __init__(self, name = "Matt"):
        self.name = name
        self.color = "unknown"
        self.size = "unknown"
        self.price = 0
        self.spookieness = 0
    
    # Gets and sets
    def get_color(self):
        return self.color

    def set_color(self, value):
        self.color = value 
    
    def get_size(self):
        return self.size
    
    def get_size_uk(self):
        return self.size + 4
    
    def set_size(self, value):
        if 0 <= value <= 20:
            self.size = value

    def get_price(self):
        return self.price
    
    def set_price(self,value):
        if value >= 0:
            self.price = value

    def get_spookieness(self):
        if 0 <= self.spookieness < 5:
            return "Youre not scaring anyone !" 
        elif 5 <= self.spookieness < 10:
            return "Ugh okay i guess its scary? "
        elif 10 <= self.spookieness < 20:
            return "F********* Dang "  
        elif 0 >= self.spookieness:
            return "So pleasent !" 
        else:
            return "try again next halloween"

    def set_spookieness(self, value):
        self.set_spookieness = value
    
    def haaaaa(self, increaseBy):
        self.spookieness += increaseBy
        print(self)

    # to string
    def __str__(self):
        return f"{self.name} and its size is {self.size} and priced at {self.price} because {self.get_spookieness()}"


costume1 = Costumes()
costume1.set_color("brownish")
costume1.set_size(6)
costume1.set_price(1000000)
costume1.set_spookieness(-10)

listofCostumes = []
listofCostumes.append(costume1)

for costume in listofCostumes:
    print(costume)

# Question 1
class Product:
    # This will run first as we create the clas
    def __init__(self, input_name):
        # private class variables
        self.name = input_name
        self.price = 0
        self.quantity = 0
    
    # Get Method
    def get_price(self):
        return self.price
    
    # Gets Price in Canadian dollors :(
    def get_price_cad(self):
        return self.price * 1.40
    
    # Set Method
    def set_price(self, value):
        if value > 0:
            self.price = value
    # Get Method
    def get_quantity(self):
        return self.quantity
    # Set Method
    def set_quantity(self, value):
        if 0 <= value <99:
            self.quantity = value
    # Build in print method 
    def __str__(self):
        return f"The product is {self.name} and priced at {self.price} we have {self.quantity}"

# Create the product with name
apple_iphone = Product("Iphone 17 Pro Max")
apple_watch = Product("Apple Watch Series 7")
# set the product price
apple_iphone.set_price(1499)
apple_watch.set_price(499)
# Create the product quantity
apple_iphone.set_quantity(5)
apple_watch.set_quantity(5)
# Prints product
print(apple_iphone)
print(apple_watch)

# Question 6
class Student:
    def __init__(self):
        self.name = "Unknown"
        self.major = "Unknown"
        self.gpa = 0
    
    def get_name(self):
        return self.name
    def set_name(self,value):
        self.name = value

    def get_major(self):
        return self.major
    def set_major(self, value):
        self.major = value
    
    def get_gpa(self):
        return self.gpa
    def set_gpa(self, value):
        if 0 <= value <=4.0:
            self.gpa = value
    
    def introduce(self):
        return f"Hi, i'm {self.name}. I'm studying {self.major}"
    
    def study_for_exam(self):
        if self.gpa < 4.0:
            self.gpa += 0.2

student1 = Student()
student1.set_name = "Evan Linder"
student1.set_major = "Computer Science"
student1.set_gpa = 3.8
student1.study_for_exam()

print(student1.introduce())
print(student1.get_gpa())






class Candy:
    def __init__(self):
        self.name = "uhknown"
        self.flavour = "unknowm"
        self.shape = "unknown"
        self.size = 0
        self.price = 0

    # get and set
    def get_name(self):
        return self.name
    def set_name(self, value):
        self.name = value

    def get_price(self):
        return self.price
    def set_price(self, value):
        if 0 <= value < 1000:
            self.price = value

    def get_shape(self):
        return self.shape
    def set_shape(self,value):
        self.shape = value
    
    def get_size(self):
        return self.size
    def set_size(self, value):
        self.size = value

    def get_flavour(self):
        return self.flavour
    def set_flavour(self,value):
        self.flavour = value

    def reaction(self):
        if 0 < self.size < 5:
            return "try again next time , its too small !!"
        elif 5 < self.size < 10:
            return "Ehhh i guess its okay "
        else:
            return "WOW !!!! "

    # To String
    def __str__(self):
        return f"{self.name} its {self.flavour} cost {self.price} and is of size and shape: {self.size}, {self.shape} {self.reaction()}"

bagOfCandies = []

candy1 = Candy()
candy1.set_name("Kitkat")
candy1.set_shape("Ractangle")
candy1.set_size(10)
candy1.set_flavour("Chocolat")
candy1.set_price(499.99)

bagOfCandies.append(candy1)

for candy in bagOfCandies:
    print(candy)




class Movie:
    def __init__(self):
        self.title = "Unknown"
        self.genres = []
        self.spookieness = 0
        self.duration = 0

    # Gets and Sets
    def get_title(self):
        return self.title
    def set_title(self, value):
        self.title = value 

    def get_genre(self):
        output = ""
        for genre in self.genres:
            output += f" {genre}, "
        return output
    def set_genre(self, value):
        self.genres.append(value)
    
    def get_duration(self):
        return self.duration
    def set_duration(self, value):
        if 0 < value <= 10:
            self.duration = value
    
    def get_spookieness(self):
        return self.spookieness
    def set_spookieness(self,value):
        if 0 <= value <= 10:
            self.spookieness = value
    
    # A method 
    def get_reaction(self):
        if 0 <= self.spookieness < 3:
            return "Youre not scaring anyone !" 
        elif 3 <= self.spookieness < 7:
            return "Ugh okay i guess its scary? "
        elif 7 <= self.spookieness < 10:
            return "F********* call 911 !! "  
        else:
            return "idk"
    # To string 
    def __str__(self):
        return f"{self.title} of genere {self.get_genre()} durition is {self.duration} and spookiness is {self.get_spookieness()} reaction : {self.get_reaction()}"
    
movie1 = Movie()
movie1.set_title("Scream")
movie1.set_genre("Scary")
movie1.set_duration(1.75)
movie1.set_spookieness(4)

print(movie1)

'''

class Monster:

    def __init__(self, _name):
        self.name = _name
        self.size = -1
        self.num_of_teeth = -1
        self.power = -1

    # Get and Set
    def get_name(self):
        return self.name
    
    def get_size(self):
        return self.size
    def set_size(self, value):
        if value > 0:
            self.size = value
        
    def get_num_of_teeth(self):
        return self.num_of_teeth
    def set_num_of_teeth(self, value):
        if value >= 0:
            self.num_of_teeth = value
    
    def get_power(self):
        return self.power
    def set_power(self, value):
        if value > 0:
            self.power = value
    
    def scare(self):
        if 80 > self.power > 50:
            return "Very Scary"
        elif self.power < 10:
            return "Cute monster"
        elif 10 < self.power < 50:
            return "Moderately scary monster"
        else:
            return "RUN"
        
    def __str__(self):
        return f"Stats: Name: {self.get_name()}, size: {self.get_size()}, power: {self.get_power()} . It also have {self.get_num_of_teeth()} so it is {self.scare()}"
    
moster1 = Monster("Krish")
moster1.set_num_of_teeth(30)
moster1.set_power(1)
moster1.set_size(0.1)

print(moster1)