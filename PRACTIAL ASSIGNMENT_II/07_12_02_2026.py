def calculate_percentage(marks):
    if not marks:
        return 0
    total = sum(marks)
    percentage = (total / (len(marks) * 100)) * 100
    return percentage

def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F (Fail)"

student_marks = []

while True:
    print("--- Student Result System ---")
    print("1. Enter Marks")
    print("2. Calculate Percentage")
    print("3. Assign Grade")
    print("4. Show Full Report")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        num_subjects = int(input("How many subjects? "))
        student_marks = []
        for i in range(num_subjects):
            m = float(input(f"Enter marks for subject {i + 1}: "))
            student_marks.append(m)
        print("Marks saved successfully!\n")

    elif choice == "2":
        if not student_marks:
            print("Please enter marks first!\n")
        else:
            perc = calculate_percentage(student_marks)
            print(f"Total Percentage: {perc:.2f}%\n")

    elif choice == "3":
        if not student_marks:
            print("Please enter marks first!\n")
        else:
            perc = calculate_percentage(student_marks)
            grade = assign_grade(perc)
            print(f"Final Grade: {grade}\n")

    elif choice == "4":
        if not student_marks:
            print("No data found.\n")
        else:
            perc = calculate_percentage(student_marks)
            print("-" * 25)
            print(f"Total Marks: {sum(student_marks)}")
            print(f"Percentage:  {perc:.2f}%")
            print(f"Grade:       {assign_grade(perc)}")
            print("-" * 25 + "\n")

    elif choice == "5":
        print("Closing System...")
        break
    else:
        print("Invalid choice, try again.\n")