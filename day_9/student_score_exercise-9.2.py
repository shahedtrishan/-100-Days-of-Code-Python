student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grade = {}

# scores = student_scores["Harry", "Ron", "Hermione", "Draco", "Neville"]
# print(scores)

for key in student_scores:
    scores = student_scores[key]
    # print(scores)
    if 91 <= scores and scores <= 100:
        student_grade[key] = "Outstanding"
    elif 81 <= scores and scores <= 90:
        student_grade[key] = "Exceeds Expectations"
    elif 71 <= scores and scores <= 80:
        student_grade[key] = "Acceptable"
    elif scores <= 70:
        student_grade[key] = "Fail"
    else:
        print("Invalid score")

print(student_grade)
