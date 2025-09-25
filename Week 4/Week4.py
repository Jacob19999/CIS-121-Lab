# Week 4

# Hints:

# While true run forever
done = False
while not done:
    # Use flag to stop the loop!
    done = True

word = "banana"
i = 0

# While loop that counts up i till length of word - 1
while i < len(word):
    i += 1

# For loop (Starting Position, Ending Position, Step size)
# Counts from 0 - 9 (0,2,4,6,8)
for j in range(0, 10, 2):
    pass #ignore this word for now...

# Iterates through each letter of "banana"
for letter in word:
    print(letter)

# For loop (Start from 0, end at word length)
# Counts from 0 to Word length - 1
for i in range(0, len(word)):
    print(word[i])


# Question 2
word = input("Enter word ")
result_word = ""
pos = 0
num = 0

for letter in word:
    if (pos % 2 == 1) :
        result_word += word[pos]
    pos +=1

print(f"Result word: {result_word}")

# Starting pos, ending pos, step size another way to do it
result_word = ""
for index in range (1 , len(word), 2):
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

















