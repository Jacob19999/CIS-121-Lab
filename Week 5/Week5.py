# Written By jacob Tang

# Not have print or input in your function 
# Should only contain Logic
'''

def pool_time(input_grade, input_time):
    pool_time = ""

    if input_grade.lower() == "k":
        input_grade = 0
    
    # first slot -> 0 -3
    if 0 <= int(input_grade) <= 3:
        if input_time.lower() == "morning":
            pool_time = "9AM"
        else:
            pool_time = "1PM"

    # Second slot - 4 -8
    elif 4 <= int(input_grade) <= 8:
        if input_time.lower() == "morning":
            pool_time = "10AM"
        else:
            pool_time = "2PM"

     # Third 9 -12
    elif 9 <= int(input_grade) <= 12:
        if input_time.lower() == "morning":
            pool_time = "11AM"
        else:
            pool_time = "3PM"
    return pool_time

# Outside of the function
input_grade = input("Enter a grade : ")
input_time = input("Enter a Time: ")

print(f"The pool time is : {pool_time(input_grade, input_time)}")



'''


def covert_knuts(knuts):
    output = ""
    # How many kunts is a Galleons worth ?
    # 29 * 17 = 493

    # 544 Knuts , how many galleons can i buy ?
    # 544 // 493 = 1

    galleons = knuts // 493

    # After buying 1 galleon , how many knuts remaining 
    # 544 % 493 = 51
    remaining_knuts = knuts % 493

    # 51 Knuts how many sickles can i buy ?
    # 51 knuts // 29 = 1
    sickles = remaining_knuts // 29

    # remaining knuts = 51 - (29 * 1 ) = 22
    remaining_knuts = remaining_knuts % 29

    if galleons > 0:
        output = f"Galleons : {galleons} "
    if sickles > 0:
        output += f"sickles : {sickles} "
    if remaining_knuts > 0:
        output += f"knuts : {remaining_knuts} "

    return output

input_knuts = int(input("Enter the number of knuts : "))
print(f"{covert_knuts(input_knuts)}")


# Question 11 


def convert_knuts(knuts):
    output = ""
    # Logic 

    # What is the price of one galleon in terms of kunts -> 29 * 17 = 493
    # 544 knuts -> 1 galleon
    galleons = knuts // 493 

    # How many Sickles can i afford with the remaining ?
    
    # Remianing -> 544 - 493 = 51
    remaining_knuts = knuts - (galleons * 493)

    # Since 1 sickle => 29 knuts 
    # 51 remaining -> 1 sickle
    sickle = remaining_knuts // 29

    # How many do i have left after buying 1 galleoon and 1 sickle ?
    # 544 - 493 - 29 = 22 
    remaining_knuts = remaining_knuts - (sickle * 29)

    if galleons > 0:
        output = f"Galleon: {galleons} "
    if sickle > 0:
        output += f"sickle: {sickle} "
    if remaining_knuts > 0:
        output += f"Knuts: {remaining_knuts} "

    return output

input_knuts = int(input("Enter the number of Knuts :"))
print(f"Number of each item i can buy : {convert_knuts(input_knuts)}")






def is_fever(input_temp):

    output = False

    # Check the last character and if F or C
    # temp = "98F" 
    # temp[-1] => F
    unit = input_temp[-1]

    # How do we extract the temperature
    # temp = "98F"
    # int(temp[:-1]) = 98
    temp = int(input_temp[:-1])

    if unit == "F":
        if temp > 98.6:
            output = True
    
    elif unit == "C":
        if temp > 37:
            output = True
    
    return output


userinput = input("Enter a temp 00F , 00C : ")
print(f"This temp {userinput } is fever ? {is_fever(userinput)}")
