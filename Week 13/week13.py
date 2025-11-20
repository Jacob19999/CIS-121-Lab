import random 

# Define the file , quizint.txt and "w" which is write as txt_file
with open("Week 13/QuizInts.txt", "w") as txt_file:
    #Iterate through 0 - 100
    for i in range(100):
        # For each iteration, generate random num
        num = random.randint(50,200)
        # Wrie to the txtfile
        txt_file.write(str(num) + "\n")


# Question 7
total_visitor = 0
num_of_days = 0

with open("Week 13/LibraryVisits.csv", "r") as lib_visits:
    for _row in lib_visits:
        # CSV - comma separated value
        values = _row.split(",")
        # Parsing of a int value "191/n" -> 191 
        total_visitor += int(values[1])
        num_of_days += 1

print(f"Average visitors over {num_of_days} days is { total_visitor / num_of_days}")