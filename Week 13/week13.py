import random

# Option 1
rand_nums = ""
quiz_int_file = open("Week 13/QuizInts.txt" , "w")

for i in range(100):
    rand_num = random.randint(50,200)
    rand_nums += str(rand_num) + "\n"

quiz_int_file.write(rand_nums)
quiz_int_file.close()

# Option 2
with open("Week 13/QuizInts.txt" , "w") as quiz_int_file:
    for i in range(100):
        rand_num = random.randint(50,200)
        rand_nums += str(rand_num) + "\n"
    quiz_int_file.write(rand_nums)


# Question 7
total_visitor_count = 0
days = 0
with open("Week 13/LibraryVisits.csv") as visits:
    for row in visits:
        row_items = row.split(",")
        if row_items[0] != "Date":
            total_visitor_count += int(row_items[1])
            days += 1

print(f"Average Visitor COunt is {total_visitor_count/days}")


