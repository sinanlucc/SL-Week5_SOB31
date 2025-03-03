# Calculating Grades (ok, let me think about this one)
changes have been made
# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #SL Added "int" with " ( "

exam_three = int(input("Input exam grade three: "))  #SL Changed variable name exam_3 to "exam_three" and str() to int()

grades = [exam_one, exam_two, exam_three] #SL Added missing commas
sum_grades = 0 # SL Changed variable name 'sum' to "sum_grades" avoiding built-in function
for grade in grades: # SL Fixed 'grade' to "grades"
  sum_grades += grade # SL Changed sum operation into short way

avg = round(sum_grades / len(grades)) # SL Fixed misspelled variable 'grdes' to 'grades'
                                      # & added 'round' function to round the average
if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:  # SL Added missing colon (:)
    letter_grade = "B"
elif avg >=70 and avg < 80:   # SL Fixed 'avg > 69' to 'avg >= 70'
    letter_grade = "C"        # SL Fixed quote error ("C') to ("C")
elif avg >= 60 and avg < 70:  # SL Fixed range 'avg<= 69' to 'avg>=60' and 'avg >= 65' to 'avg<70'
    letter_grade = "D"
else:                         # SL Changed 'elif:' to 'else:' for final condition
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg)) # SL Made to outside loop i.e. to print once

print("Grade: " + letter_grade)

if letter_grade == "F":         # SL Changed 'letter-grade is "F"' to 'letter_grade == "F"'
    print("Student is failing.") # SL Added parentheses() for print
else:
    print("Student is passing.") # SL Added parentheses() for print


# Edited by Sinan Luckman