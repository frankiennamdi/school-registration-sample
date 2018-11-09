from model.quiz import Quiz
import copy


class CourseClass:
    ''' Class for a course that is taught by a teacher and '''
    def __init__(self, course, session, year, teacher):
        self.course = course
        self.session = session
        self.year = year
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_quiz(self, questions):
        for student in self.students:
            student.assign_quiz(self, Quiz(copy.deepcopy(questions)))

    def __str__(self):

        return "\nSession: %s\nYear: %s%s\nTeacher:%s\nStudents:%s" % (
            self.session, self.year, str(self.course), str(self.teacher),
            "\n".join(str(student) for student in self.students))

    def __hash__(self):
        return hash((self.session, self.year, self.course))

    def __eq__(self, other):
        return (self.session, self.year, self.teacher,
                self.course) == (other.session, other.year, other.teacher,
                                 other.course)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not (self == other)
