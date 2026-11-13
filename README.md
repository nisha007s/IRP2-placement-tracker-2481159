# Placement Readiness Tracker

A command-line Python tool for the department placement cell. It records
students' practice-test scores (aptitude, verbal, coding), calculates each
student's average and grade, finds the top scorer and flags students who
need extra practice.

**Course:** Industry Readiness Programme-II (CSE2596)
**Student:** Nisha Sehrawat | URN: 2481159

## Files

- `tracker.py` - main tracker (Tasks 1 and 2)
- `runner_up.py` - runner-up score coding problem (Task 3)

## How to run

Requires Python 3.

```
python tracker.py
python runner_up.py
```

## Sample output (tracker.py)

```
Results
Roll  Name              Apt  Verb  Code     Avg  Grade
------------------------------------------------------------
101   Nisha Sehrawat     88    82    90   86.67  A
102   Arjun Singh        65    70    60   65.00  B
103   Sneha Gupta        45    50    40   45.00  C
104   Karan Malik        30    35    25   30.00  Needs practice
105   Pooja Yadav        78    85    80   81.00  A
106   Aman Verma         91    87    94   90.67  A

Top scorer: Aman Verma (90.67)
Needs extra practice (average below 40): Karan Malik
```

## Sample output (runner_up.py)

```
Input:
5
70 85 85 60 90
Output:
85
```
