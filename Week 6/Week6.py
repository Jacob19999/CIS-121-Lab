
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

# Question 9
# Function takes in a list of cards
def count(list_of_cards):

    points = 0
    for card in list_of_cards:
        if str(card) in ['2','3', '4', "5", "6"]:
            points += 1
        elif str(card) in ['10','j', 'q' , 'k' , 'a']:
            points -= 1
        
    return points

# Create the list of cards.
deck1 = [5, 9, 10, 3, "j", "a", 4, 8, 5]
deck2 = [ "a", "a", "k", "q", "q", "j"]

print(f"Total Points Deck 1: {count(deck1)}")
print(f"Total Points Deck 2: {count(deck2)}")
'''

# Question 19


# Examples :
# is acronym("abc", ["alice", "bob", "charlie"] ) = true
# is acronym("ab", ["apple", "banana", "cat"]) = false
# is acronym("ab", ["apple", "", "cat"]) = false

# Hints: 

def is_acronym(s, words):

    combined_letters = ""
    
    if len(s) != len(words):
        return False

    for word in words:
        print(word)

        if word == "":
            return False
        
        first_letter = word[0]
        combined_letters += first_letter

    if combined_letters != s:
        return False
        
    return True


words_ = ["alice", "bob", "charlie"]
s = "abc"
print(is_acronym(s, words_))



def is_acronym(s, words):
    if len(s) != len(words):
        return False
    acronym = ""
    for word in words:
        if len(word) == 0:
            return False
        acronym += word[0]
    return s == acronym

print(is_acronym("abc", ["alice", "bob", "charlie"]))
print(is_acronym("a", ["an", "apple"]))
print(is_acronym("ngguoy", ["never", "gonna", "give", "up", "on", "you"]))
print(is_acronym("ab", ["apple", "banana", "cat"]))
print(is_acronym("ab", ["apple", "", "cat"]))





