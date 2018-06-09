import sys
from Subject import Subject
from GradeCalculator import GradeCalculator

math = Subject("Mathematics")
english = Subject("English")
history = Subject("History")
science = Subject("Science")
physical_education = Subject("Physical Education")

subjects = [math, english, history, science, physical_education]

for subject in subjects:
    try:
        subject.grade = float(input("Enter grade for {}: ".format(str(subject.name))))
    except ValueError:
        print("Unacceptable input.\nTerminating...")
        sys.exit(1)

grade_calculator = GradeCalculator()
grade_calculator.calculate_grades(subjects)
print("Average grade: {} Mark: {}.".format(str(grade_calculator.average), grade_calculator.get_euivalent_marks()))