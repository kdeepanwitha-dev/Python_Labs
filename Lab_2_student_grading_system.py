import os

FILENAME = "grades.txt"

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def add_student():
    try:
        name = input("Enter Student Name: ").strip()
        roll = input("Enter Roll Number: ").strip()

        print("\nEnter marks for 5 subjects:")
        marks = []
        subjects = ["Maths", "Science", "English", "Computer", "Social"]

        for subject in subjects:
            mark = float(input(f"{subject}: "))
            if mark < 0 or mark > 100:
                print("Invalid marks! Marks should be between 0 and 100.")
                return
            marks.append(mark)

        total = sum(marks)
        average = total / len(marks)
        grade = calculate_grade(average)

        # Save to file
        with open(FILENAME, "a") as file:
            file.write(f"{roll},{name},{total},{average:.2f},{grade}\n")

        print("\n----- Result -----")
        print(f"Name       : {name}")
        print(f"Roll No    : {roll}")
        print(f"Total      : {total}")
        print(f"Average    : {average:.2f}")
        print(f"Grade      : {grade}")
        print("Record saved successfully!\n")

    except ValueError:
        print("Error: Please enter valid numeric marks.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")


def display_records():
    try:
        with open(FILENAME, "r") as file:
            records = file.readlines()

            if not records:
                print("No student records found.\n")
                return

            print("\n" + "=" * 70)
            print(f"{'Roll No':<12} {'Name':<20} {'Total':<10} {'Average':<10} {'Grade':<8}")
            print("=" * 70)

            for line in records:
                data = line.strip().split(",")
                if len(data) == 5:
                    roll, name, total, average, grade = data
                    print(f"{roll:<12} {name:<20} {total:<10} {average:<10} {grade:<8}")

            print("=" * 70 + "\n")

    except FileNotFoundError:
        print("No records found. File does not exist yet.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")


def main():
    while True:
        print("===== Student Grading System =====")
        print("1. Add Student & Calculate Grade")
        print("2. Display All Records")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_records()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2 or 3.\n")


if __name__ == "__main__":
    main()