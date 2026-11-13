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