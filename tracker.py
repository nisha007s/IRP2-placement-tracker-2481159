# Placement Readiness Tracker - IRP-II Assignment
# Each student is stored as a dictionary inside a list

students = [
    {"name": "Nisha Sehrawat",  "roll_no": "101", "aptitude": 88, "verbal": 82, "coding": 90},  # A
    {"name": "Arjun Singh",  "roll_no": "102", "aptitude": 65, "verbal": 70, "coding": 60},  # B
    {"name": "Sneha Gupta",  "roll_no": "103", "aptitude": 45, "verbal": 50, "coding": 40},  # C
    {"name": "Karan Malik",  "roll_no": "104", "aptitude": 30, "verbal": 35, "coding": 25},  # Needs practice
    {"name": "Pooja Yadav",  "roll_no": "105", "aptitude": 78, "verbal": 85, "coding": 80},  # A
]


def read_score(subject):
    """Keep asking until the user enters a whole number from 0 to 100."""
    while True:
        try:
            score = int(input(f"{subject} score (0-100): "))   # convert text to int
        except ValueError:
            print("Enter a whole number.")
            continue
        if 0 <= score <= 100:
            return score
        print("Score must be between 0 and 100.")


def add_student(students):
    """Take one new student's details from the user and add them to the list."""
    print("Enter one student's practice scores.")
    name = input("Name: ")
    roll_no = input("Roll number: ")          # kept as text to keep leading zeros
    new_student = {
        "name": name,
        "roll_no": roll_no,
        "aptitude": read_score("Aptitude"),
        "verbal": read_score("Verbal"),
        "coding": read_score("Coding"),
    }
    students.append(new_student)


def average(student):
    """Return the mean of the three scores."""
    return (student["aptitude"] + student["verbal"] + student["coding"]) / 3


def grade(avg):
    """Return a grade based on the average."""
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Needs practice"


def top_scorer(students):
    """Return the student with the highest average."""
    return max(students, key=average)


def needs_practice(students, limit=40):
    """Return students whose average is below the limit (default 40)."""
    return [s for s in students if average(s) < limit]



def print_table(students):
    """Print all students in a neat table using a loop."""
    print("\nResults")
    print(f"{'Roll':<6}{'Name':<16}{'Apt':>5}{'Verb':>6}{'Code':>6}{'Avg':>8}  Grade")
    print("-" * 60)
    for s in students:
        avg = average(s)
        print(f"{s['roll_no']:<6}{s['name']:<16}{s['aptitude']:>5}{s['verbal']:>6}"
              f"{s['coding']:>6}{avg:>8.2f}  {grade(avg)}")


def main():
    print("Placement Readiness Tracker")
    add_student(students)
    print_table(students)

    best = top_scorer(students)
    print(f"\nTop scorer: {best['name']} ({average(best):.2f})")

    weak = needs_practice(students)
    print("Needs extra practice (average below 40):",
          ", ".join(s["name"] for s in weak) if weak else "None")


if __name__ == "__main__":
    main()