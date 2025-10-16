
# Question 4
def get_name(techid_dict):
    list_of_name = []
    # How to iterate through the dict?
    for key in techid_dict:
        # How do we extract the name?
        name = techid_dict[key]
        # How to add names into a list?
        list_of_name.append(name)

    return list_of_name

dict = {"01234" : "Evan" , "012341" : "Jacob", "012342" : "Matt"}
#print(get_name(dict))


# Question 5
def find_oldest(age_dict):
    oldest_person = ""
    max_age = -1
    # Iterate through the dict
    for curr_name in age_dict:
        # Extract the age of the current person
        curr_age = age_dict[curr_name] 
        # Compare current persons age with max age
        if curr_age > max_age:
            # If current age is larger, update max age
            max_age = curr_age
            oldest_person = curr_name
    # Return the oldest age
    return oldest_person

# Question 6
def letter_count(word):
    # Create a empty Dict to store letters and their count
    letter_count_dict = {}
    # Iterate through each letter in the word
    for each_letter in word:
        # For each letter, we check if the letter is in the dict or not
        if each_letter not in letter_count_dict:
            # If not, we set the count as 1
            letter_count_dict[each_letter] = 1
        else:
            # If it is , then we increment 
            letter_count_dict[each_letter] += 1

    # Output the letter count dict
    return letter_count_dict





# Question 9a

recipt = {}

recipt["Side Salad"] = 6
recipt["Chicken Parm"] = 12
recipt["Cookie"] = 3

print(recipt)

# Question 9b
def get_total_cost(receipt):
    total_cost = 0
    # Iterate through each item in the receipt
    for each_item in receipt:
        # Get the cost of each item
        cost = receipt[each_item]
        # Sum up the cost of each item.
        total_cost += cost

    return total_cost

#print(get_total_cost(recipt))








dict1 = {"01234" : "Evan" , "01234" : "Jacob", "01234" : "Matt"}
for techid in dict1:
    name = dict1[techid]
    print(name)


