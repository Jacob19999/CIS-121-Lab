# Created By Jacob Tang

# Question 3
light_color =  input("ENter a light color: ").lower()


if light_color == "green":
    print("Go")
elif light_color == "yellow":
    print("Yield")
elif light_color == "red":
    print("Stop")
else:
    print("Invalid color")

# Question 5 Hint

int1 = int(input("Enter first Number: "))
int2 = int(input("Enter second Number: "))
int3 = int(input("Enter third Number: "))

# Using arrays (Not covered yet)
nums = [int1, int2, int3]

for _ in range(2):
    if nums[0] > nums[1]:
        nums[0], nums[1] = nums[1], nums[0]
    if nums[1] > nums[2]:
        nums[1], nums[2] = nums[2], nums[1]

print(nums[0], nums[1], nums[2])

nums.sort() # Built in function

# If statements for all possibilities
'''
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
