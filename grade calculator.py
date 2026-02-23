try:
    num_subjects = int(input("How many subjects? "))

    if num_subjects <= 0:
        print("Must have at least one subject.")
    else:
        total_marks = 0
        max_possible = 0

        for i in range(num_subjects):
            subject_name = input(f"\nSubject {i+1} name: ")
            marks_obtained = float(input(f"Marks obtained in {subject_name}: "))
            max_marks = float(input(f"Max marks for {subject_name}: "))

            # basic validation
            if marks_obtained < 0 or marks_obtained > max_marks:
                print("Invalid marks entered, skipping this subject.")
                continue

            total_marks += marks_obtained
            max_possible += max_marks

        if max_possible == 0:
            print("No valid subjects entered.")
        else:
            percentage = (total_marks / max_possible) * 100

            # assign grade based on percentage ranges
            if percentage >= 90:
                grade = "A+"
                remark = "Outstanding!"
            elif percentage >= 80:
                grade = "A"
                remark = "Excellent!"
            elif percentage >= 70:
                grade = "B"
                remark = "Good"
            elif percentage >= 60:
                grade = "C"
                remark = "Average"
            elif percentage >= 50:
                grade = "D"
                remark = "Pass"
            else:
                grade = "F"
                remark = "Fail - Need to improve"

            print("\n--- Result Card ---")
            print(f"Total Marks  : {total_marks} / {max_possible}")
            print(f"Percentage   : {percentage:.2f}%")
            print(f"Grade        : {grade}")
            print(f"Remark       : {remark}")

except ValueError:
    print("Please enter valid numbers!")