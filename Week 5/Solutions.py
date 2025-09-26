import math

# Question 1 

def pyramid_volume(b, h):
    return (b ** 2 * h) / 3

# Question 2
def cone_volume(r, h):
    return (math.pi * r ** 2 * h) / 3

def total_score(two_pointers, three_pointers):
    return 2 * two_pointers + 3 * three_pointers

#print(pyramid_volume(2,5))
#print(cone_volume(5,5))
#print(total_score(10,20))

# Question 3
def total_score(aces, winning_shots):
    return 2 * aces + winning_shots

# Question 4
def leg_counter(chickens, cows, pigs):
    return 2 * chickens + 4 * cows + 4 * pigs

# Question 5
def battery_counter(e_dolls, rc_cars, robo_dogs):
    return 2 * e_dolls + 4 * rc_cars + 6 * robo_dogs

# Question 6
def resting_rate(age, athl_goal):
    if 20 <= age <= 39:
        if athl_goal == "Above Average":
            return "47-72"
        elif athl_goal == "Below Average":
            return "73-93"
    elif 40 <= age <= 59:
        if athl_goal == "Above Average":
            return "46-71"
        elif athl_goal == "Below Average":
            return "72-94"
    elif 60 <= age <= 79:
        if athl_goal == "Above Average":
            return "45-70"
        elif athl_goal == "Below Average":
            return "71-97"

def pool_time(grade, time):
    if grade == 'k' or grade == 1 or grade == 2 or grade == 3:
        if time == "Morning":
            return "11AM"
        elif time == "Afternoon":
            return "1 PM"
    elif grade == 4 or grade == 5 or grade == 6 or grade == 7 or grade == 8:
        if time == "Morning":
            return "10 AM"
        elif time == "Afternoon":
            return "2 PM"
    elif grade == 9 or grade == 10 or grade == 11 or grade == 12:
        if time == "Morning":
            return "11 AM"
        elif time == "Afternoon":
            return "3 PM"

def traffic_light(light_color):
    if light_color == "red":
        return "Stop"
    elif light_color == "Green":
        return "Go"
    elif light_color == "Yellow":
        return "Yield"

def access_rights(user_role):
    if user_role == "user":
        return "limited"
    elif user_role == "guest":
        return "view"
    elif user_role == "admin":
        return "full"

def convert_knuts(knuts):
    galleons = knuts // (29 * 17)
    remaining_knuts = knuts % (29 * 17)
    sickles = remaining_knuts // 29
    knuts_rem = remaining_knuts % 29
    result = ""
    
    if galleons > 0:
        result += f"{galleons} galleon "
    if sickles > 0:
        result += f"{sickles} sickles "
    if knuts_rem > 0:
        result += f"{knuts_rem} knuts"
    return result
12
def convert_bronze(bronze_coins):
    gold = bronze_coins // (20 * 15)
    remaining_bronze = bronze_coins % (20 * 15)
    silver = remaining_bronze // 20
    bronze_rem = remaining_bronze % 20
    result = ""

    if gold > 0:
        result += f"{gold} gold "
    if silver > 0:
        result += f"{silver} silver "
    if bronze_rem > 0:
        result += f"{bronze_rem} bronze"
    return result



# Strings

# Question 1
def is_fever(temp):
    unit = temp[-1]
    num = float(temp[:-1])

    if unit == 'F':
        if num > 98.6:
            return True
        else: 
            return False
    elif unit == 'C':
        if num > 37:
            return True
        else: 
            return False

print(is_fever("36C"))

# Question 2
def is_boiling(temp):
    unit = temp[-1]
    num = float(temp[:-1])
    if unit == 'F':
        return num >= 212
    elif unit == 'C':
        return num >= 100
    
print(is_boiling("101C"))

# Question 3
def hamming_distance(str1, str2):
    count = 0
    for letterPos in range(len(str1)):
        if str1[letterPos] != str2[letterPos]:
            count += 1
    return count

# Question 4
def is_isogram(word):
    seen = ""
    for char in word:
        if char in seen:
            return False
        seen += char
    return True

# Question 5
def get_drink_ID(flavor, capacity):
    return flavor[:3] + str(capacity)


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
