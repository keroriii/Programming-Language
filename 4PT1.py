# student information
first_name = "Kyne"
age = 20

# student score and pass/fail status
student_score = 70.1  # Initially an integer
student_score = float(student_score)  # Convert to float

# if the student passed, failed, or has not taken the exam
if student_score >= 69.5:
    passed_status = True  # Passed
elif student_score < 69.5:
    passed_status = False  # Failed
else:
    passed_status = None  # Not taken

# Print student details
print("Student Information:")
print(f"Name: {first_name}")
print(f"Age: {age}")
print(f"Score: {student_score}")
print(f"Passed: {passed_status}")
