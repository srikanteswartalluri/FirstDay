class Student:
    'Student class '
    studentCount = 0 #class variable

    #constructor
    def __init__(self, n, g, s):
        self.name = n
        self.grade = g
        self.score = s
        Student.studentCount += 1 # Student.studentCount = Student.studentCount + 1

    #can this student be promoted
    def canPromote(self):
        if self.score > 30:
            return True
        else:
            return False

    def getScore(self):
        return self.score




