print("===== STUDENT GRADE CALCULATOR =====")

# Taking marks as input
maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
computer = float(input("Enter Computer Science marks: "))
english = float(input("Enter English marks: "))

# Calculating total and percentage
total = maths + physics + chemistry + computer + english
percentage = total / 5

# Calculating grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Displaying result
print("\n===== RESULT =====")
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)