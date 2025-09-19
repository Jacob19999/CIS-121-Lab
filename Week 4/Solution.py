# By Jacob Tang

'''
# Hints:

# While true run forever
while True:
    # Use break to stop the loop!
    break

word = "banana"
i = 0

# While loop that counts up i till length of word - 1
while i < len(word):
    i += 1

# For loop (Starting Position, Ending Position, Step size)
for j in range(0, 10, 1):
    break

# Iterates through each letter of "banana"
for letter in word:
    print(letter)

# For loop (Start from 0, end at word length)
for i in range(0, len(word)):
    print(word[i])

    
larger_num = int(input("Enter the larger Number : "))
smaller_num = int(input("Enter the larger Number : "))

num = 0
while larger_num / 2 > smaller_num:
    larger_num /= 2
    num += 1

print(f"Number of times halved: {num} ")
# Question 1
larger_num = int(input("Enter the larger Number : "))
smaller_num = int(input("Enter the larger Number : "))
count = 0

while larger_num / 2 > smaller_num:
    larger_num /= 2
    count += 1

print(f"Number of times halved: {count} ")



# Question 2
num2 = 0
result_word = ""
for index in range (1 , len(word) - 1, 2):
    result_word += word[index]
print(f"Result word: {result_word}")





# Question 2

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



# Question 4
word = ""

# While loop that runs forever
while True:
    # Read the user input
    user_in = input("Enter a letter: ")
    # if the user typed "done" we stop !
    if user_in == "done":
        break
    else:
        # Else lets add letter into the word
        word += user_in

# Print out the final word
print(f"The final word is {word}")


# Question 5

start = 50
end = 517

# Assume 50-517 Inclusive

# Start with 51 and stop before 518, take steps of 2
for i in range(start + 1, end + 1, 2):
    print(i)


# Question 1
larger = int(input("Enter larger Number: "))
smaller = int(input("Enter smaller Number: "))

count = 0
current = larger

while current > smaller:
    current = current / 2
    count += 1
        
print(f"The Count is : {count}")

# Question 2
word = input("Enter a word: ")
output = ""

for i in range(1,len(word) , 2):
    output += word[i]
    
print(f"The result word is {output}")


# Question 3
num = 38
while num <= 1050:
    print(num)
    num += 2

num = 37 + 1
for i in range(num,1050 , 2):    
    print(i)

# Question 4
word = ""
while True:
    entry = input("Enter a letter: ")
    if entry == "done":
        break
    word += entry
print(word)

# Question 5
total = 0
num = 51
while num <= 517:
    total += num
    num += 2

print(f"The Total is : {total}")

total = 0
for i in range(51, 518, 2):
    total += i

print(f"The Total is : {total}")






# Question 6

total = 0
while True:
    num = int(input("Enter an integer: "))
    if num < 0:
        break
    total += num
print(f"The Total is : {total}")

# Question 7
n = 25
print(f"{n}")
end=" "
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(f"{n}")
    end=" "

# Question 8
num = int(input("Enter a number: "))
factor = 1
while factor <= num:
    if num % factor == 0:
        print(factor)
    factor += 1

# Question 9
width = int(input("Enter width: "))
length = int(input("Enter length: "))
pattern = input("Enter pattern: ")
row = 0
while row < length:
    print(pattern * width)
    row += 1

# Question 10
largest_even = -1
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    if num % 2 == 0:
        if num > largest_even:
            largest_even = num
print(largest_even)

# Question 11
n = int(input("Enter a number: "))
total = 0
i = 1
while i <= n:
    total += i * i
    i += 1
print(total)

'''