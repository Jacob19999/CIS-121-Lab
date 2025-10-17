lyst = {"physics": 82, "History": 65, "Biology": 95}


def min_grade_key(exam):
    return min(exam, key=exam.get)

print(min_grade_key(lyst))