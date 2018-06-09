class GradeCalculator(object):

    def __init__(self):
        self._average = 0

    def calculate_grades(self, subjects = []):
        total = 0
        for subject in subjects:
            print("{}: {}".format(subject.name, str(subject.grade)))
            total += subject.grade

        self._average = total / len(subjects)
        return self._average

    def get_euivalent_marks(self):
        if self._average >= 95: return 'A'
        elif self._average >= 85: return 'B'
        elif self._average >= 75: return 'C'
        else: return 'F'

    @property
    def average(self):
        return self._average