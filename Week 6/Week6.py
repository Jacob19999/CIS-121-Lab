
# Work on Question:
# 5 , 9 , 19 




# Question 9
# Function takes in a list of cards
def count(list_of_cards):

    # We need to keep track of points
    points = 0
    
    # Complete the code

    # Iterating through each card:
    for card in list_of_cards:
        # Check each card to compute points
        # OR if str(card) in ["2", "3", "4", "5", "6"]:
        # OR if card in [2, 3, 4, 5, 6]:
        if card in range(2,6):
            points += 1
        elif str(card) in ["10", "j","q","k", "a"]:
            points -= 1
        
    return points

# Create the list of cards.
deck1 = [5, 9, 10, 3, "j", "a", 4, 8, 5]
deck2 = [ "a", "a", "k", "q", "q", "j"]

print(f"Total Points Deck 1: {count(deck1)}")
print(f"Total Points Deck 1: {count(deck2)}")


# Examples :
# is acronym("abc", ["alice", "bob", "charlie"] ) = true
# is acronym("ab", ["apple", "banana", "cat"]) = false
# is acronym("ab", ["apple", "", "cat"]) = false

# Hints: 

# QUestion 19 
def is_acronym(s, words):

    combined_letters = ""

    if len(s) != len(words):
        return False

    for word in words:

        if word == "":
            return False
        
        combined_letters += word[0]
        
    if s != combined_letters:
        return False
    
    return True


words_ = ["alice", "bob", "charlie"]
s = "abc"
print(is_acronym(s, words_))




































# Question 5:
'''
def hailstone_seq(number):
    # Create an empty List , use number as starting
    output_list = [number]
    # Code it here !
    while number > 1:
        # While Loop till 1
        if number % 2 == 0:
            # Is even 
            number /= 2
            # number = number / 2
        else:
            # Is Odd
            number = (3 * number) + 1
        
        # Add the result to the ouput list.
        output_list.append(number)

    return output_list

print(f" {hailstone_seq(25)} ")
print(f"Total Points Deck 2: {count(deck2)}")




# Question 19


# Examples :
# is acronym("abc", ["alice", "bob", "charlie"] ) = true
# is acronym("ab", ["apple", "banana", "cat"]) = false
# is acronym("ab", ["apple", "", "cat"]) = false

# Hints: 

# QUestion 19 
def is_acronym(s, words):

    combined_letters = ""

    # is length of s is different from the length of words , false
    # len(s) != len(words): -> stop and return false
    if len(s) != len(words):
        return False

    # How can i iterate through each word, and extract the first letter
    # for word in words:
    for word in words:
        
        # Check if a word is blank 
        # if word == "" -> stop and return false
        if word == "":
            return False
        
        # Extract first letter
        # fist_letter = word[0] 
        first_letter = word[0]

        # combine the extracted letters and compare with string s
        # s += fist_letter
        # Example: 
        # Alice = a
        # Bob = b
        # charlie = c
        combined_letters += first_letter

        # Them compare each word
        # "abc" == "abc"
    if combined_letters != s:
        return False

    return True


words_ = ["alice", "bob", "charlie"]
s = "abc"
print(is_acronym(s, words_))

'''



