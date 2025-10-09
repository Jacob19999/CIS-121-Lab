# Question 4


def get_name(my_dict):
    # 0. Empty List to store names!
    names = []
    # 1. How to iterate through the dictionary ?
    for key in my_dict:
        # 2. How do we access the value with the key ?
        name =  my_dict[key]
        # 3. How do you put the names in a list ?
        names.append(name)
    return names

names_dict = {"123": "Matt Priem" , "456": "Evan Linder", "789": "Jacob" }
#print(get_name(names_dict))

# Question 5
def find_oldest(persons):
    oldest_name = ""
    max_age = -1 

    # How do you iterate through the dict ? 
    for name in persons:
        age = persons[name]

        # How do you find the oldest age ?
        if age > max_age:
            max_age = age
            # How do you get the name ?
            oldest_name = name

    return oldest_name

persons = {"Emma" : 71 , "Jack" : 45 ,"Olivia" : 82 , "Liam" : 39}
#print(find_oldest(persons))

# Question 6
def letter_count(word):
    count_dict = {}
    
    # How do we iterate through the letters in the word?
    for letter in word:
        if letter not in count_dict:
            # If letter is not in dict , add letter to dict
            count_dict[letter] = 1
        else:
             # If letter is already there , incrememnt value 
            count_dict[letter] += 1

    return count_dict

print(letter_count("mississippi"))

