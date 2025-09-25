# Written By jacob Tang

# Question 1
'''
def pyramid_volume(base, height):
    volume = (base**2 * height) / 3
    return volume

print(f"The volume of the pyramid is {pyramid_volume(3,4)}")


# Question 8 
# 

def pool_times(grade, time):

    # Convert K -> 0
    pool_time = ""
    if grade == "k":
        grade = 0

    # Checks grade is K or between 1-3 
    if 0 <= int(grade) <= 3:
        if(time == "Morning"):
            pool_time = "9AM"
        else:
            pool_time = "1PM"

    elif (4 <= int(grade) <= 8):
        if(time == "Morning"):
            pool_time = "10AM"
        else:
            pool_time = "2PM"

    elif (9 <= int(grade) <= 12):
        if(time == "Morning"):
            pool_time = "11AM"
        else:
            pool_time = "3PM"

    return pool_time



print(f"Pool Time is : {pool_times("k", "Morning")}")


# Question 11 

def convert_knuts(knuts):
    # Knuts , Sickle , Galleons
    # 1 galleon == 493 Knuts!
    # 1 sikcle = 29 Knuts


    # 1. For the number of knuts how many galleon scan i buy ?
    galleons = knuts // (493)
    remaining_knuts = knuts - (galleons *  493)

    # 2. Remaining Knuts, how many sickles can i buy ?
    sickles = remaining_knuts // 29

    # 3. How many remaining Knuts after buying sickles ?
    remaining_knuts = remaining_knuts - (sickles * 29)

    output = ""

    if galleons > 0: 
        output += f"Galleons: {galleons} " 
    if sickles > 0: 
        output += f"Sickles: {sickles} "  
    if knuts > 0 :
        output += f"Knuts: {remaining_knuts} "
    
    

    return output

print(convert_knuts(32))


# Question 14
from random import randint

def guess_num(user_guess):
    output = ""
    value = randint(0,9)

    if user_guess == "even":
        if value % 2 == 0:
            output = "Correct"
        else:
            output = "Incorrect"
    elif user_guess == "odd":
        if value % 2 != 0:
            output = "Correct"
        else:
            output = "Incorrect"

    return output

user_input = input("Guess the random number , odd or even :")
print(f"The guess is: {guess_num(user_input)}")
'''



# Function holds the logic ! 
# Takes in temperature and checks if it is fever 
def is_fever(temperature):

    # How can we extract the F and C ? Hint word[-1]
    unit = temperature[-1]

    # If it is F -> 98.6 is a fever 
    if unit == "F":
        # "99F" -> "99"
        if float(temperature[:-1]) > 98.6:
            return True
        else:
            return False

    # If it is a C - > 37 is a fever 
    elif unit == "C":
        # "37C" -> "37"
        if float(temperature[:-1]) > 37:
            return True
        else:
            return False

# Input and print should be outside of the function
user_input = input("Enter a temperature in F or C ")
print(f"Is fever ? {is_fever(user_input)}")
