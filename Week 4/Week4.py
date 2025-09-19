# Week 4

# Question 1
'''
larger_num = int(input("Enter the larger Number : "))
smaller_num = int(input("Enter the larger Number : "))

num = 0
while larger_num / 2  > smaller_num:
    larger_num /= 2
    num += 1

print(f"Number of times halved: {num} ")

'''



# Question 2

# Using a For loop iterate every character

word = input("Enter word ")
result_word = ""
pos = 0
num = 0

print("Option 1")
for letter in word:
   
    print(f"Loop Count : {num}")
    num+=1
    
    if (pos % 2 == 1) :
        result_word += word[pos]
    pos +=1

print(f"Result word: {result_word}")

print("Option 2")
# Starting pos, ending pos, step size
num2 = 0
result_word = ""
for index in range (1 , len(word), 2):
    print(f"Loop Count : {num2}")
    num2 += 1
    result_word += word[index]
print(f"Result word: {result_word}")

























