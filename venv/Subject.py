class Subject(object):

    def __init__(self, name):
        self._name = name
        self._grade = 0


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        self._grade = new_grade