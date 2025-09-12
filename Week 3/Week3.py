# Created by Jacob Tang On sept 12 2025

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
'''
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