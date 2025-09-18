# Created by Jacob Tang


# Question 5 Hint

'''

# Array version 
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

# Option 2 Using If statements !
If i have 3 numbers, how many different ways
we can rearragne them ?

1,2,3
1,3,2
2,1,3
2,3,1
3,1,2
3,2,1


if int1 <= int2 <= int3:
    print(int1, int2, int3)
elif int1 <= int3 <= int2:
    print(int1, int3, int2)
.
.
.
.
.

'''


# Question 7
knuts = int(input("Enter amount in knuts: "))

# Find if we can buy any galleons
galleons = knuts // (29 * 17)
knuts_remaining = knuts % (29 * 17)

# See if we can buy Sickles
sickles = knuts_remaining // 29
knuts_final = knuts_remaining % 29

message = ""
if galleons > 0:
    message += (f"Galleons : {galleons}")
if sickles > 0:
    message += (f" Sickles : {sickles} ")
if knuts_remaining > 0:
    message += (f" Knuts : {knuts_final}")

print(message)
