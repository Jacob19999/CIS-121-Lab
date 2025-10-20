'''

# Question 15 Week 7

def total_donations(donations_dict):

    total_donations = 0

    for amount in donations_dict.values():
        total_donations += amount
    
    return total_donations

print(total_donations({'mike': 500, 'john':200}))

lst = {'mike': 500, 'john':200}
print((lst.values()))


# Question 7

def ascending_order(num1, num2 = 5, num3 = 25):

    a , b, c = num1, num2, num3

    if a > b:
        a, b = b, a
    if a > c: 
        a, c = c, a
    if b > c:
        b, c = c, b
    return [a, b, c]

print(ascending_order(50))

# Question 15


# Question 15
# Helper Function
def is_negative(num):
    if num < 0:
        return True
    else:
        return False
    
def is_negative(num):
    return num < 0


# Helper Function
def is_odd(num):
    return num % 2 != 0


# Main Function
def report_negative_odd(lyst):
    result_lyst = []
    for num in lyst:
       if is_negative(num) and is_odd(num):
           result_lyst.append(num)
    return result_lyst

'''

dict_temp={}

word = "paypalishiring"
row = 4
lim = 0
j = 0

for i in range(0, len(word)):
    if i > row-1:
        dict_temp[j] = word[lim : lim + row - 1]




            

dict = {0 : ["p", "a", "y", "p"], 1 : ["-1", "l","a","-1"], 2: ["i", "s", "h", "i"], 3: ["-1","i","r","-1"], 4: ["n","g"]}
st=""
counter=0

for j in range(0, len(dict)- 1):
    for i in dict.values():
        if i[counter] != "-1":
            st += i[counter]
    counter +=1


print(st)

















# Question 9
def get_indices(list_of_nums, value = 0):
    pos = []
    for i in range(0, len(list_of_nums)):
        if value == list_of_nums[i]:
            pos.append(i)
    return pos

# Question 10
def find_factors(num = 36):
    factors = []
    for i in range(1, num+1):
        factors.append
    return factors

# Question 13
def is_vowel(letter):
    return letter.lower() in "aeiou"

def report_vowels(word):
    vowels = []
    for letter in word:
        if is_vowel(letter):
            vowels.append(letter)
    return vowels

# Question 4
def find_winner(p1 = "rock", p2 = "rock"):
    # If the same for both players
    if (p1 == p2):
        return "It is a tie"
    elif (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
        return "Player 1 wins"
    else:
        return "Player 2 Wins"


def skip_letter(word):
    word_lst = []
    for i , letter in enumerate(word):
        if i % 2 ==1:
            word_lst += letter
    return word_lst

print(skip_letter("counterattack"))



