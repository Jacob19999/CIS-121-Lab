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




# Question 2

def is_fever(input_temp):
    output = False

    # 1. How can we extract the unit ? F or C
    unit = input_temp[-1]

    # 2. How can we extract the temperature ?
    temperature = int(input_temp[:-1])

    # 3. If it is F , > 98.6 = fever
    if unit == "F" and temperature > 98.6:
        output = True

    # 4. If it is C , > 37.0 = fever
    elif unit == "C" and temperature > 37:
        output = True

    return output

userinput = input("Enter a temp 00F , 00C : ")
print(f"This temp {userinput } is fever ? {is_fever(userinput)}")



def hamming_distance(str1, str2):

    count = 0

    if len(str1) != len(str2) :
        # Dont run if words are not same length
        return 0
    
    # Literate through each string , since both strings are same
    for letterPos in range(len(str1)):
        # If a letter is different , then we +1 
        if str1[letterPos] != str2[letterPos]:
            count += 1
    # Done ! Profit
    return count


input1 = input("String 1 : ")
input2 = input("String 2 : ")
print(f"Distance = {hamming_distance(input1, input2)}")

'''
# Question 8

def last_letters(sentence):
    encode = ""

    # 1. How to iterature through the characters

    for pos in range(0, len(sentence) - 1):
        # 2. How can we know the last letter of each word ?
        # "wingardium levios makes objects float "

        if sentence[pos + 1] == " ":
            encode += sentence[pos]

    # 3. How do we store the last characters and output it .
    return encode + sentence[-1]

user_input = input("Enter a spell : ")
print(f"Encoded Spell is {last_letters(user_input)}")
