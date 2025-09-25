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
