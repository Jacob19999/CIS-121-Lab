# Written By jacob Tang

# Not have print or input in your function 
# Should only contain Logic
def pool_time(input_grade, input_time):
    pool_time = ""

    # How can i change K - > 0 
    if input_grade.lower() == "k":
        input_grade = 0

    # first slot -> 0 -3
    if 0 <= int(input_grade) <= 3:
        if input_time.lower() == "morning":
            pool_time = "9AM"
        else:
            pool_time = "1PM"

    # Second slot - 4 -8
    elif 4 <= int(input_grade) <= 8:
        if input_time.lower() == "morning":
            pool_time = "10AM"
        else:
            pool_time = "2PM"

     # Third 9 -12
    elif 9 <= int(input_grade) <= 12:
        if input_time.lower() == "morning":
            pool_time = "11AM"
        else:
            pool_time = "3PM"

    return pool_time

# Outside of the function
input_grade = input("Enter a grade : ")
input_time = input("Enter a Time: ")

print(f"The pool time is : {pool_time(input_grade, input_time)}")


