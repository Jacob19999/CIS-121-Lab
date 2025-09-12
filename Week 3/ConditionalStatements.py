# Created by Jacob Tang

'''
# Question 3
light_color = input("Enter a light color: ")

if light_color == "green":
    print("Go")
elif light_color == "yellow":
    print("Yield")
elif light_color == "red":
    print("stop")

# Question 4
age = int(input("Enter a Age: "))
athleticism_goal = input("Enter a Goal: ")

if athleticism_goal == "Below Average":
    if 20 <= age <= 39:
        print("73-93")
    elif 40 <= age <= 59:
        print("72-94")
    elif 60 <= age <= 79:
        print("71-97")
elif athleticism_goal == "Above Average":
    if 20 <= age <= 39:
        print("47-72")
    elif 40 <= age <= 59:
        print("46-71")
    elif 60 <= age <= 79:
        print("45-70")

# Or 

if 20 <= age <= 39:
    if athleticism_goal == "Above Average":
        print("47-72.")
    elif athleticism_goal == "Below Average":
        print("73-93.")
    else:
        print("Invalid goal")
elif 40 <= age <= 59:
    if athleticism_goal == "Above Average":
        print("46-71.")
    elif athleticism_goal == "Below Average":
        print("72-94.")
    else:
        print("Invalid goal")
elif 60 <= age <= 79:
    if athleticism_goal == "Above Average":
        print("45-70.")
    elif athleticism_goal == "Below Average":
        print("71-97.")
    else:
        print("Invalid goal")
else:
    print("Age out of range")

# Question 5

# Optiminal Way 
int1 = int(input("Enter first Number: "))
int2 = int(input("Enter second Number: "))
int3 = int(input("Enter third Number: "))

nums = [int1, int2, int3]

for _ in range(2):
    if nums[0] > nums[1]:
        nums[0], nums[1] = nums[1], nums[0]
    if nums[1] > nums[2]:
        nums[1], nums[2] = nums[2], nums[1]

print(nums[0], nums[1], nums[2])

# What you should do for this class

if int1 <= int2 <= int3:
    print(int1, int2, int3)
elif int1 <= int3 <= int2:
    print(int1, int3, int2)
elif int2 <= int1 <= int3:
    print(int2, int1, int3)
elif int2 <= int3 <= int1:
    print(int2, int3, int1)
elif int3 <= int1 <= int2:
    print(int3, int1, int2)
else:
    print(int3, int2, int1)



# Question 6 Similar to 5

# Question 7
knuts = int(input("Enter amount in knuts: "))

galleons = knuts // (29 * 17)
knuts_remaining = knuts % (29 * 17)

sickles = knuts_remaining // 29
knuts_final = knuts_remaining % 29

output = ""
if galleons > 0:
    output.append(f"{galleons} galleon{'s' if galleons > 1 else ''}")
if sickles > 0:
    output.append(f"{sickles} sickle{'s' if sickles > 1 else ''}")
if knuts_final > 0:
    output.append(f"{knuts_final} knuts")
print(output)


# Question 8
a = float(input("Pick a number: "))
b = float(input("Pick another number: "))
c = float(input("Pick another number: "))

if a >= b and a >= c:
    print("The largest number is", a)
elif b >= a and b >= c:
    print("The largest number is", b)
else:
    print("The largest number is", c)

# Question 9 Limilar as question 8

# Question 10 
race = input("Enter race: ").title()
class_ = input("Enter class: ").title()  # Using class_ to avoid keyword conflict

health_points = -1

if race == "Elf":
    if class_ == "Warrior":
        health_points = 150
    elif class_ == "Bard":
        health_points = 75
    elif class_ == "Wizard":
        health_points = 25
elif race == "Ogre":
    if class_ == "Warrior":
        health_points = 200
    elif class_ == "Bard":
        health_points = 100
    elif class_ == "Wizard":
        health_points = 50

print("Health points:", health_points)

# Question 11

from random import randint
value = randint(0, 1)

guess = input("Guess heads or tails: ").lower()

if guess == "heads" and value == 0:
    print("Correct!")
elif guess == "tails" and value == 1:
    print("Correct!")
else:
    print("Incorrect!")

# Question 12
a = int(input("Pick a number: "))
b = int(input("Pick another number: "))
c = int(input("Pick another number: "))

if a == b == c:
    print("You entered the same number 3 times.")
elif a == b or a == c or b == c:
    print("You entered the same number 2 times.")
else:
    print("You entered the same number 0 times.")

    '''