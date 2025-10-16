# 1. Game: heads or tails
from random import randint

def toss_coin(guess=0):
    value = randint(0, 1)
    if value == guess:
        return "Correct!"
    else:
        return "Incorrect!"
    
# 2. Game: Odd or Even
from random import randint

def guess(guess="even"):
    value = randint(0, 9)
    is_even = value % 2 == 0
    guessed_even = guess.lower() == "even"
    if (is_even and guessed_even) or (not is_even and not guessed_even):
        return "Correct!"
    else:
        return "Incorrect!"

# 3. Count duplicates
def count_duplicates(num1=0, num2=0, num3=0):
    if num1 == num2 == num3:
        return "There are 3 of the same number"
    elif num1 == num2 or num1 == num3 or num2 == num3:
        return "There are 2 of the same number"
    else:
        return "Each number is unique"
    
# 4. Rock, Paper, Scissors
def find_winner(player1="Rock", player2="Rock"):
    p1 = player1.lower()
    p2 = player2.lower()
    if p1 == p2:
        return "It’s a tie!"
    elif (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# 5. Luke's relations
def find_relation(name=""):
    relations = {
        "Darth Vader": "Father",
        "Leia": "Sister",
        "Han": "Brother in law",
        "R2D2": "Droid"
    }
    return relations.get(name, "Unknown")

# 6. Hailstone Sequence
def hailstone_seq(n=40):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    print(", ".join(map(str, sequence)))
# 7. Ascending order
def ascending_order(num1, num2=5, num3=25):
    a, b, c = num1, num2, num3
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return [a, b, c]

# 8. Descending order
def descending_order(num1, num2=15, num3=5):
    a, b, c = num1, num2, num3
    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if b < c:
        b, c = c, b
    return [a, b, c]

# 9. Get indices
def get_indices(lst, value=0):
    indices = []
    for i in range(len(lst)):
        if lst[i] == value:
            indices.append(i)
    return indices

# 10. Find factors
def find_factors(num=36):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    print(", ".join(map(str, factors)))

# 11. List of multiples
def list_of_multiples(num, length=5):
    multiples = []
    for i in range(1, length + 1):
        multiples.append(num * i)
    return multiples

# 12. Is even and report evens
def is_even(num):
    return num % 2 == 0

def report_evens(lst):
    evens = []
    for num in lst:
        if is_even(num):
            evens.append(num)
    return evens
# 13. Is vowel and report vowels
def is_vowel(letter):
    return letter.lower() in 'aeiou'

def report_vowels(s):
    vowels = []
    for char in s:
        if is_vowel(char):
            vowels.append(char)
    return vowels

# 13. Is vowel and report vowels
def is_vowel(letter):
    return letter.lower() in 'aeiou'

def report_vowels(s):
    vowels = []
    for char in s:
        if is_vowel(char):
            vowels.append(char)
    return vowels

# 15. Is negative, is odd, report negative odds
def is_negative(num):
    return num < 0

def is_odd(num):
    return num % 2 != 0

def report_negative_odds(lst):
    neg_odds = []
    for num in lst:
        if is_negative(num) and is_odd(num):
            neg_odds.append(num)
    return neg_odds