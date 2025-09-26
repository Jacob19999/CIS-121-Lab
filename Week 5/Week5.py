# Written By jacob Tang

import math

'''
# Question 8

def pool_time(user_grade, user_time):
    time_output = ""

    # Question : How can we allow "K" a string 
    # to be compared with an integer 1-3 
    # Perhaps K-> Grade 0?

    if user_grade == "K":
        user_grade == 0

    if 0 <= int(user_grade) <= 3:
        if user_time == "Morning":
            time_output = "9am"
        else:
            time_output = "1pm"
    # Continue ....


    return time_output

input_grade = input("Enter Grade : ")
input_time = input("Enter Time : ")

print(f"The Pool Time is : {pool_time(input_grade, input_time)}")


# Question 11

def convert_knuts(knuts):
    output = ""

    # How much is a galleon in terms of knuts 
    # 29 * 17 = 493 knuts / Galleon
    # Lets say i have 544 knuts , how many galleons can i afford
    # 544 // 493 = 1
    galleon = knuts // 493

    # After buying 1 galleon , how many knuts do i have left ?
    # 544 - 493 = 51 
    remaining_knuts = knuts - (galleon * 493)

    # WIth 51 how many sickles can i buy ?
    # Just one sickle
    # 51 - 29 = 22
    sickles = remaining_knuts // 29

    # 544 - > 1 Galleon , 1 sicke , and 22 Knuts
    remaining_knuts = remaining_knuts - (sickles * 29)

    if galleon > 0:
        output = output + f"Galleon: {galleon} "
    if sickles > 0:
        output = output + f"sickles: {sickles} "
    if remaining_knuts > 0:
        output = output + f"knuts: {remaining_knuts} "

    return output

user_input = int(input("Enter number of Knuts ")) 
print(f"For {user_input} knuts i can buy: {convert_knuts(user_input)}")

'''

def is_fever(input):
    # 1. Find out if the input is in F or C
    # temp = "98F"
    # temp[-1] -> F
    unit = input[-1]

    # 2 . Extract the temperature 
    # temp[:-1] - > 98
    temperature = int(input[:-1])

    output = False
    if unit == "F":
         # 3. Is > 98.6 F a Fever ?
        if temperature > 98.6 :
            output = True
    
    elif unit == "C":
        # 4. If > 37.0 C a Fever ?
        if temperature > 37 :
            output = True
            
    return output

user_input = input("Enter a temperature 00F or 00C: ")
print(f"is fever {is_fever(user_input)}")
    





