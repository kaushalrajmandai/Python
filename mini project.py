name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
math_marks = int(input("Enter Maths marks: "))
science_marks = int(input("Enter Science marks: "))
english_marks = int(input("Enter English marks: "))

# --- Calculation Section ---
total = math_marks + science_marks + english_marks
average = total / 3

# Determine Result (Assuming 40 is the passing mark)
if average >= 35:
    result = "PASS"
else:
    result = "FAIL"

# --- Output Section ---
print("\n------- Student Report Card ---------")
print("Name    : " + name)
print("Roll No : " + roll_no)
print("Total   : " + str(total))
print("Average : " + str(average))
print("Result  : " + result)
print("-----------------------------------")