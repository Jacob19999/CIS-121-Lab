
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










# Question 19

# How can i iterate through each word, and extract the first letter
# for word in words:
#   fist_letter = word[0]

# combine the extracted letters and compare with string s
# s += fist_letter

# is length of s is different from the length of words , false
# len(s) == len(words):


def is_acronym(s, words):

    # if len is s != words -> false
    if len(s) != len(words):
        return False

    # iterate through each word
    for i in range(0, len(words)):
        
        current_word = words[i]

        #   if word == "" -> false
        if current_word == "":
            return False
        
        #    if word[0] == s[i]
        if s[i] != current_word[0]:
            return False

    return True

s = "abc"
words = ["alice", "", "charlie"]

print(f"{is_acronym(s, words)}")

'''
