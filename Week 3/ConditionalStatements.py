# Created by Jacob Tang

# 3.1
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
else:
    print("The number is zero or negative.")


# 3.2
score = int(input("Enter your test standards (0-100): "))

if score >= 0:
    print("Grade: A")
elif score >= 0:
    print("Grade: B")
elif score >= 0:
    print("Grade: C")
elif score >= 0:
    print("Grade: D")
else:
    print("Grade: F")


#3.3

enrolled = input("Are you currently enrolled in the college? (yes/no): ")
if enrolled == "yes":
    math_course = input("Enter the math course you completed (MATH 112, MATH 113, MATH 115, or MATH 121): ")
    grade = float(input("Enter your grade in that course (e.g., 3.5): "))
    
    if math_course == "MATH 112" or math_course == "MATH 113" or math_course == "MATH 115" or math_course == "MATH 121":
        if grade >= 2.0:
            print("You meet the prerequisites and are enrolled. Eligible for CIS 121.")
        else:
            print("You are enrolled and took a qualifying course, but your grade is too low.")
    else:
        print("You are enrolled but did not complete a qualifying prerequisite course.")
else:
    print("You must be enrolled to be eligible for CIS 121.")








