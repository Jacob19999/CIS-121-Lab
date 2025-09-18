# Jacob Tang

'''

larger_num = int(input("Enter the larger Number : "))
smaller_num = int(input("Enter the larger Number : "))

num = 0
while larger_num > smaller_num:
    larger_num /= 2
    num += 1

print(f"Number of times halved: {num} ")



# Question 2

word = input("Enter a word: ")
result = ""
# First start point, Ending Point, step szie
for i in range(1 , len(word) - 1,2):
    result += word[i]

print(f"Output = {result}")

'''

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