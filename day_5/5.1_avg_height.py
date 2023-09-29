# average_height

from statistics import mean

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


# # Write your code below this row 👇

# # without_loop
length = len(student_heights)
total = sum(student_heights)

print(length)
print(total)
average = total / length
print(round(average))


# with loop

total_height = 0
for height in student_heights:
    total_height = height + total_height
print(total_height)


# number_of_students = 0
for student in student_heights:
    number_of_students = number_of_students + 1
print(number_of_students)


average_height = round(total_height / number_of_students)
print(average_height)

# with_function

print(mean(student_heights))
