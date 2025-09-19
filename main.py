attendance_percentage = float(input("What is your attendence percentage?: "))
assignment_submitted = input("Do you submitted your assignment? (yes/no): ").lower()

if attendance_percentage >= 75 and assignment_submitted == "yes":
    print("Allowed to take exam")
else:
    print("Not allowed")